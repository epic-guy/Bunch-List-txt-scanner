# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication,QHeaderView
import os,sys,time


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.data={}
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 468)
        
        self.choose = QtWidgets.QPushButton(Dialog)
        self.choose.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.choose.setObjectName("choose")
        self.choose.clicked.connect(self.accept)
        
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(20, 20, 231, 41))
        self.title.setObjectName("title")
        
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(380, 90, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        
        self.search_2 = QtWidgets.QPushButton(Dialog)
        self.search_2.setGeometry(QtCore.QRect(380, 140, 71, 21))
        self.search_2.setObjectName("search_2")
        self.search_2.clicked.connect(self.search)
        
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(330, 90, 51, 21))
        self.status.setObjectName("status")
        
        self.hor = QtWidgets.QFrame(Dialog)
        self.hor.setGeometry(QtCore.QRect(20, 120, 531, 20))
        self.hor.setFrameShape(QtWidgets.QFrame.HLine)
        self.hor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hor.setObjectName("hor")
        
        self.inp = QtWidgets.QLineEdit(Dialog)
        self.inp.setGeometry(QtCore.QRect(120, 140, 251, 21))
        self.inp.setObjectName("inp")
        
        self.tableView = QtWidgets.QTableWidget(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 170, 521, 221))
        self.tableView.setObjectName("tableView")
        
        self.quit = QtWidgets.QPushButton(Dialog)
        self.quit.setGeometry(QtCore.QRect(460, 420, 75, 23))
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.close)
        
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(370, 420, 75, 23))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.Saved)
        
        self.fshow = QtWidgets.QLineEdit(Dialog)
        self.fshow.setEnabled(False)
        self.fshow.setGeometry(QtCore.QRect(20, 90, 131, 21))
        self.fshow.setObjectName("fshow")
        
        self.search = QtWidgets.QLabel(Dialog)
        self.search.setGeometry(QtCore.QRect(30, 140, 81, 21))
        self.search.setObjectName("search")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 400, 191, 31))
        self.label.setObjectName("label")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowIcon(QtGui.QIcon('icon2.png'))
        Dialog.setWindowTitle(_translate("Dialog", "List Scanner"))
        self.choose.setText(_translate("Dialog", "Choose File"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">List Scanner:</span></p></body></html>"))
        self.search_2.setText(_translate("Dialog", "Search"))
        self.status.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Status:</span></p></body></html>"))
        self.quit.setText(_translate("Dialog", "Quit"))
        self.save.setText(_translate("Dialog", "Save Results"))
        self.search.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Search Text:</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Matches Found: 0"))


    def accept(self):
        self.Filename=None
        self.fname=None
        dlg = QtWidgets.QFileDialog()
        fname = dlg.getOpenFileName(None, 'Open file', "", "Text Files (*.txt);;All Files (*)")
        if '' not in fname:
            fname = fname[0]
            fname, Filename = os.path.split(os.path.abspath(fname))
            print(fname)
            print(Filename)
            self.fshow.setText(Filename)
            c=0
            with open(fname+'\\'+Filename,'r') as f:
                for i in f.readlines():
                    txt=i.split(':')
                    self.progressBar.setProperty("value", c)
                    self.data[txt[0].split('@')[0]]=(txt[0],txt[1])
                    c+=1
        else:
            print("Try Again")

    def search(self):
        a=self.inp.text()
        self.disp=[]
        for i in self.data.keys():
            if a in i:
                #print("Email ID:",self.data[i][0])
                #print("Password:",self.data[i][1])
                self.disp.append((self.data[i][0],self.data[i][1]))
        header_labels = ['E-Mails',"Passwords"]
        self.label.setText("Matches Found: "+str(len(self.disp)))
        if self.disp != []:
            #self.tableView.setRowCount(len(self.disp))
            self.tableView.setColumnCount(2)
            self.tableView.setHorizontalHeaderLabels(header_labels)
            header = self.tableView.horizontalHeader() 
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            for row in self.disp:
                inx = self.disp.index(row)
                self.tableView.insertRow(inx)
                self.tableView.setItem(inx,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableView.setItem(inx,1,QtWidgets.QTableWidgetItem(str(row[1].strip("\n"))))
        else:
            QtWidgets.QMessageBox.question(None, 'Error', "Enter Something to search for!", QtWidgets.QMessageBox.Ok)
    def Saved(self):
        name=str(time.time())+'.csv'
        with open(name,'w+') as f:
            f.write("Email,Password\n")
            for i in self.disp:
                f.write(f"{i[0]},{i[1]}\n")
        QtWidgets.QMessageBox.question(None, 'Saved', "Saved  Successfully as "+name, QtWidgets.QMessageBox.Ok)

    def close(self):
        sys.exit()
      
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Trans = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Trans)
    Trans.show()
    sys.exit(app.exec_())
