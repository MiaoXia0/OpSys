from math import log
from typing import List
import pandas as pd
from pdModel import pandasModel
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from MainUi import Ui_MainWindow
from DialogProcCrea import Ui_DiaProcCrea
from DialogProcClo import Ui_DiaClo
from DialogProcBlo import Ui_DiaBlo
from DialogPageCrea import Ui_DiaPage
from DialogPageWrite import Ui_DiaWrite

procdf = pd.DataFrame(columns=['进程名', 'PID', '进程状态', '内容', '所需时间'])
pagedf = pd.DataFrame(columns=['页号', '主存块号', '辅存块号', '是否在主存', '是否修改'])  # 界面显示用表


class PCB:  # 进程控制块
    def __init__(self, name, pid, content, statu):
        self.name: str = name
        self.pid: int = pid
        self.content: str = content
        self.status: str = statu
        self.time: int = len(content)  # 内容长度决定运行时间 单位为秒


timeslices = 5  # 时间片数
timeslice = 2  # 时间片大小
NOW = 0  # 当前进程数
MAX = 10  # 最大进程数
ready_list: List = []  # 预备进程列表
running_list: List = []  # 运行进程
blocked_list: List = []  # 阻塞进程
runned_list: List = []  # 执行完毕的进程


class Page:  # 页
    def __init__(self, lnumber: int, pnumber: int, dnumber: int, flag: int):
        self.lnumber: int = lnumber  # 页号
        self.flag: int = flag  # 是否在主存中
        self.pnumber: int = pnumber  # 内存块号
        self.write = 0  # 是否被修改过
        self.dnumber: int = dnumber  # 辅存块号


pages: List[Page] = []  # 页表
p: List[int] = []  # 主存中的页号
memused: List[int] = []  # 使用的主存块
LenMem = 4  # 内存中最多页数
NumBlock = 4  # 内存中最多块数
m: int = 12  # 地址长度
n: int = 10  # 块内地址长度


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global procdf
        global pagedf
        self.ui.tableProc.setModel(pandasModel(procdf))
        self.ui.tablePages.setModel(pandasModel(pagedf))
        self.TimeSliceTimer = QTimer()  # 时间片调度隔一秒反复执行
        self.TimeSliceTimer.timeout.connect(self.TimeSliceRun)
        self.ui.actProcCre.triggered.connect(self.crea)
        self.ui.actProcRev.triggered.connect(self.clos)
        self.ui.btnProcCrea.clicked.connect(self.crea)
        self.ui.btnProcClos.clicked.connect(self.clos)
        self.ui.btnProc.clicked.connect(self.TimeSlice)
        self.ui.btnBlock.clicked.connect(self.bloc)
        self.ui.btnPageCrea.clicked.connect(self.pageAdd)
        self.ui.btnPage.clicked.connect(self.pageModify)
        self.ui.btnLenSet.clicked.connect(self.LenSet)

    def LenSet(self):  # 设置存储管理的信息
        lenmem = int(self.ui.lineLenMem.text())
        lenpag = int(self.ui.lineLenPage.text())
        lenblo = int(self.ui.lineLenBlo.text())
        global LenMem
        LenMem = int(lenmem / lenpag)
        self.ui.linePageNum.setText(str(LenMem))
        global NumBlock
        NumBlock = int(lenmem / lenblo)
        self.ui.lineBlockNum.setText(str(NumBlock))
        self.ui.lineLenAddr.setText(str(int(log(lenmem, 2))))
        global m
        m = log(lenmem, 2)
        global n
        n = log(lenblo, 2)

    def QuSet(self):  # 刷新队列显示
        self.ui.lineReady.setText('')
        self.ui.lineRunning.setText('')
        self.ui.lineBlocked.setText('')
        for i in ready_list:
            self.ui.lineReady.setText(self.ui.lineReady.text() + str(i['pid']) + ' ')
        for i in running_list:
            self.ui.lineRunning.setText(self.ui.lineRunning.text() + str(i['pid']) + ' ')
        for i in blocked_list:
            self.ui.lineBlocked.setText(self.ui.lineBlocked.text() + str(i['pid']) + ' ')

    def crea(self):  # 创建进程
        dia = QDialog(parent=self)
        uidia = Ui_DiaProcCrea()
        uidia.setupUi(dia)
        dia.exec()
        name = uidia.lineName.text()
        con = uidia.lineCon.text()
        pid = len(ready_list) + len(running_list) + len(blocked_list) + 1
        global NOW
        if NOW >= MAX:
            QMessageBox.warning(self, '创建进程', '内存不足！', QMessageBox.Close)
            return
        # TODO 申请资源
        if pid in ready_list:
            QMessageBox.warning(self, '创建进程', '进程已存在！', QMessageBox.Close)
            return
        pcb = PCB(name, pid, con, 'ready')
        ready_list.append({'pcb': pcb, 'pid': pid, 'run': False, 'runned': False, 'timeslice': 0})
        NOW += 1
        global procdf
        procdf = procdf.append({'进程名': name, 'PID': pid, '进程状态': 'ready', '内容': con, '所需时间': pcb.time},
                               ignore_index=True)

        modelProc = pandasModel(procdf)
        self.ui.tableProc.setModel(modelProc)
        self.QuSet()
        QMessageBox.information(self, '创建进程', '进程已创建', QMessageBox.Close)

    def clos(self):  # 进程撤销
        dia = QDialog(parent=self)
        uidia = Ui_DiaClo()
        uidia.setupUi(dia)
        dia.exec()
        pid = int(uidia.linePid.text())
        for i in ready_list:
            if i['pid'] == pid:
                ready_list.remove(i)
        global procdf
        procdf.drop(index=procdf.loc[procdf['PID'] == pid].index, inplace=True)
        modelProc = pandasModel(procdf)  # 刷新模型并重新绑定
        self.ui.tableProc.setModel(modelProc)
        self.QuSet()

    def bloc(self):  # 进程阻塞
        dia = QDialog(parent=self)
        uidia = Ui_DiaBlo()
        uidia.setupUi(dia)
        dia.exec()
        pid = int(uidia.linePid.text())
        global procdf
        sta = procdf.loc[procdf['PID'] == pid]['进程状态'].iloc[0]

        if sta == 'ready':
            pass
        elif sta == 'blocked':
            for i in blocked_list:
                if i['pid'] == pid:
                    running_list.append(i)
                    blocked_list.remove(i)

            procdf.loc[procdf['PID'] == pid] = procdf.loc[procdf['PID'] == pid].replace('blocked', 'running')
            modelProc = pandasModel(procdf)
            self.ui.tableProc.setModel(modelProc)

        elif sta == 'running':
            for i in running_list:
                if i['pid'] == pid:
                    blocked_list.append(i)
                    running_list.remove(i)

            procdf.loc[procdf['PID'] == pid] = procdf.loc[procdf['PID'] == pid].replace('running', 'blocked')
            modelProc = pandasModel(procdf)
            self.ui.tableProc.setModel(modelProc)

        self.QuSet()

    def TimeSliceRun(self):  # 时间片调度每一秒执行的操作
        global procdf
        global running_list
        global timeslices
        global runned_list
        for i in running_list:  # 分配时间片
            if timeslices > 0 and not i['runned'] and not i['run']:
                i['timeslice'] = timeslice
                i['run'] = True
                timeslices -= 1
                self.ui.lineTimeSlice.setText(str(timeslices))

        for i in running_list:  # 筛选执行完成的进程
            if i['pcb'].time == 0:
                i['timeslice'] = 0
                i['run'] = False
                i['runned'] = True
                timeslices += 1
                self.ui.lineTimeSlice.setText(str(timeslices))

        a = []
        for i in running_list:  # 时间片用完的重新排到队尾
            if i['pcb'].time > 0 and i['timeslice'] == 0 and i['run']:
                i['run'] = False
                a.append(i)
                timeslices += 1
                self.ui.lineTimeSlice.setText(str(timeslices))
                self.QuSet()
        for i in a:
            running_list.remove(i)
            running_list.append(i)

        for i in running_list:  # 执行一秒
            if not i['runned'] and i['run']:
                i['pcb'].time -= 1
                i['timeslice'] -= 1
                self.ui.lineTimeSlice.setText(str(timeslices))
                procdf.loc[procdf['PID'] == i['pid'], '所需时间'] = \
                    str(int(procdf.loc[procdf['PID'] == i['pid'], '所需时间'].iloc[0]) - 1)
                modelProc = pandasModel(procdf)
                self.ui.tableProc.setModel(modelProc)

        for i in running_list:  # 筛选执行完毕状态的程序更改信息
            if i['runned']:
                a = i
                running_list.remove(i)
                runned_list.append(a)
                procdf.loc[procdf['PID'] == i['pid']] = \
                    procdf.loc[procdf['PID'] == i['pid']].replace('running', 'runned')
                modelProc = pandasModel(procdf)
                self.ui.tableProc.setModel(modelProc)
                self.ui.lineTimeSlice.setText(str(timeslices))

    def TimeSlice(self):  # 开始时间片调度
        global timeslices
        global timeslice
        timeslices = int(self.ui.lineTimeSlice.text())
        timeslice = int(self.ui.lineSliceTime.text())
        for i in ready_list:
            running_list.append(i)
        while len(ready_list) > 0:
            ready_list.remove(ready_list[0])
        global procdf
        procdf.replace('ready', 'running', inplace=True)
        modelProc = pandasModel(procdf)
        self.ui.tableProc.setModel(modelProc)
        self.QuSet()
        self.TimeSliceTimer.start(1000)

    def listMemRefresh(self):  # 刷新在主存中的页号显示
        self.ui.lineInMem.setText('')
        for lnum in p:
            self.ui.lineInMem.setText(self.ui.lineInMem.text() + str(lnum) + ' ')

    def pageAdd(self):  # 页表添加页
        dia = QDialog()
        ui = Ui_DiaPage()
        ui.setupUi(dia)
        ui.checkBox.stateChanged.connect(ui.lineMain.setEnabled)
        dia.exec()
        lnumber = int(ui.linePage.text())
        if ui.checkBox.isChecked() and len(p) < LenMem:
            pnumber = int(ui.lineMain.text())
            p.append(lnumber)
            flag = 1
            memused.append(pnumber)
        else:
            if len(p) >= LenMem and ui.checkBox.isChecked():  # 选择了但主存满了
                QMessageBox.warning(self, '主存已满', '主存已满，未添加到主存！', QMessageBox.Close)
            pnumber = -1
            flag = 0
        dnumber = int(ui.lineExt.text())
        page = Page(lnumber, pnumber, dnumber, flag)
        pages.append(page)
        global pagedf
        pagedf = pagedf.append({'页号': lnumber,
                                '主存块号': pnumber,
                                '辅存块号': dnumber,
                                '是否在主存': flag,
                                '是否修改': 0},
                               ignore_index=True)
        modelPage = pandasModel(pagedf)  # 重新绑定数据
        self.ui.tablePages.setModel(modelPage)
        self.listMemRefresh()

    def pageInterrupt(self, lnumber):  # 先进先出
        for page in pages:
            if page.lnumber == lnumber:
                index = pages.index(page)

        j: int
        QMessageBox.information(self, '缺页中断', '发生缺页中断，页号%d' % lnumber, QMessageBox.Close)
        if len(p) == LenMem:  # 内存已满淘汰最后一个 加入当前页
            j = p[0]  # 最先进入内存的页号
            p.remove(p[0])
            p.append(lnumber)
            for page in pages:  # 获取最先进入内存的下标
                if page.lnumber == j:
                    indexj = pages.index(page)

            if indexj is None:
                return

            if pages[j].write == 1:
                QMessageBox.information(self, '消息', '将页%d写回磁盘第%d块\n' % (int(j), int(pages[indexj].dnumber)),
                                        QMessageBox.Close)
            pages[indexj].flag = 0
            pages[index].pnumber = pages[indexj].pnumber
            pages[index].flag = 1
            pages[index].write = 0
            pagedf.loc[pagedf['页号'] == lnumber, '主存块号'] = pages[indexj].pnumber
            self.ui.tablePages.setModel(pandasModel(pagedf))
            QMessageBox.information(self, '消息', '淘汰主存块%d中的页%d，从磁盘第%d块中调入页%d\n' % (int(pages[indexj].pnumber),
                                                                                  int(j),
                                                                                  int(pages[index].dnumber),
                                                                                  int(lnumber)),
                                    QMessageBox.Close)
            pagedf.loc[pagedf['页号'] == pages[indexj].pnumber, '主存块号'] = -1
            pages[indexj].pnumber = -1
        elif len(p) < LenMem:  # 主存未满，直接调入主存
            p.append(lnumber)
            global memused
            pnumber = 0
            for i in range(NumBlock):  # 块号从小到大分配未分配的内存块
                if i not in memused:
                    pnumber = i
                    break
            pages[index].pnumber = pnumber
            pages[index].flag = 1
            pages[index].write = 0
            memused.append(pnumber)
            pagedf.loc[pagedf['页号'] == lnumber, '主存块号'] = pnumber
            self.ui.tablePages.setModel(pandasModel(pagedf))
            QMessageBox.information(self, '消息', '从磁盘第%d块中调入页%d\n' % (int(pages[index].dnumber), int(lnumber)),
                                    QMessageBox.Close)
        pagedf.loc[pagedf['页号'] == lnumber, '是否在主存'] = 1
        self.ui.tablePages.setModel(pandasModel(pagedf))

        self.listMemRefresh()

    def pageModify(self):
        dia = QDialog()
        ui = Ui_DiaWrite()
        ui.setupUi(dia)
        dia.exec()
        laddress: int = int(ui.lineAddr.text(), 2)
        lnumber: int = int(laddress >> n)
        ad: int = int(laddress & int(pow(2, n) - 1))
        for page in pages:
            if page.lnumber == lnumber:
                index = pages.index(page)
        if index is None:
            return
        while True:
            if lnumber > LenMem:
                QMessageBox.warning(self, '错误', '不存在该页', QMessageBox.Close)
                return
            if pages[index].flag == 1:  # 在主存
                pnumber = pages[index].pnumber
                paddress: int = int(pnumber << n) | ad
                QMessageBox.information(self,
                                        '结果',
                                        '逻辑地址为%016d, 对应物理地址为%016d' % (
                                            int(str(bin(laddress)).split('b', 2)[1]),
                                            int(str(bin(paddress)).split('b', 2)[1])),
                                        QMessageBox.Close)
                if ui.radioWrite.isChecked():
                    pages[index].write = 1
                    global pagedf

                    pagedf.loc[pagedf['页号'] == lnumber, '是否修改'] = 1
                    self.ui.tablePages.setModel(pandasModel(pagedf))
                break  # 结束
            else:
                self.pageInterrupt(lnumber)  # 不在内存 缺页中断

        self.listMemRefresh()
