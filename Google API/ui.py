import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog
import product
from enum import Enum
import sentiment
import classification

class destination(Enum):
    A=1
    B=2
    C=3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 250)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.GetIntlineEdit = QtWidgets.QLineEdit(Form)
        self.GetIntlineEdit.setGeometry(QtCore.QRect(160, 30, 180, 31))
        self.GetIntlineEdit.setText("")
        self.GetIntlineEdit.setObjectName("GetIntlineEdit")
        self.GetstrlineEdit = QtWidgets.QLineEdit(Form)
        self.GetstrlineEdit.setGeometry(QtCore.QRect(160, 80, 180, 31))
        self.GetstrlineEdit.setObjectName("GetstrlineEdit")
        self.GetItemlineEdit = QtWidgets.QLineEdit(Form)
        self.GetItemlineEdit.setGeometry(QtCore.QRect(160, 130, 180, 31))
        self.GetItemlineEdit.setObjectName("GetItemlineEdit")
        self.getIntButton = QtWidgets.QPushButton(Form)
        self.getIntButton.setGeometry(QtCore.QRect(30, 30, 120, 31))
        self.getIntButton.setObjectName("getIntButton")
        self.getStrButton = QtWidgets.QPushButton(Form)
        self.getStrButton.setGeometry(QtCore.QRect(30, 80, 120, 31))
        self.getStrButton.setObjectName("getStrButton")
        self.getItemButton = QtWidgets.QPushButton(Form)
        self.getItemButton.setGeometry(QtCore.QRect(30, 130, 120, 31))
        self.getItemButton.setObjectName("getItemButton")
        self.clickButton = QtWidgets.QPushButton(Form)
        self.clickButton.setGeometry(QtCore.QRect(141, 185, 100, 41))
        self.clickButton.setObjectName("clickButton")
        self.display = QtWidgets.QTextEdit(Form)
        self.display.setGeometry(QtCore.QRect(390, 30, 150, 150))
        self.display.setObjectName("display")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MiniProject"))
        self.getIntButton.setText(_translate("Form", "N input"))
        self.getStrButton.setText(_translate("Form", "Choose your label"))
        self.getItemButton.setText(_translate("Form", "Top OR Bottom"))
        self.clickButton.setText(_translate("Form", "Start"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.getIntButton.clicked.connect(self.getInt)
        self.getStrButton.clicked.connect(self.getStr)
        self.getItemButton.clicked.connect(self.getItem)
        self.clickButton.clicked.connect(self.start)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, 'Integer input dialog', 'Input the N number you want')
        if ok and num:
           self.GetIntlineEdit.setText(str(num))
        self.num=num

    def getStr(self):
        labels=('/Travel/Tourists Destinations','none')
        label, ok=QInputDialog.getItem(self, "select input dialog", 'Choose your label', labels, 0, False)
        if ok and label:
            self.GetstrlineEdit.setText(str(label))
        self.label=str(label)

    def getItem(self):
        items=('Top', 'Bottom')
        item, ok=QInputDialog.getItem(self, "select input dialog", 'Choose top OR bottom', items, 0, False)
        if ok and item:
            self.GetItemlineEdit.setText(str(item))
        self.choice=str(item)
    def start(self):
        top_num=self.num
        score_list=[]
        for name,member in destination.__members__.items():
            score_list.append(classification.split_txt("C:/Users/Vincent/Desktop/MiniProject/Google API/tweets/{}.txt".format(name),"{}".format(name)))
        score_list.sort()
        sss=""
        for s in score_list:
            sss=sss+'\n'+str(s)
        self.display.setText(sss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())