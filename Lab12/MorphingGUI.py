# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MorphingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(829, 745)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(30, 40, 171, 25))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(500, 40, 171, 25))
        self.toolButton_2.setObjectName("toolButton_2")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(330, 300, 131, 22))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 680, 92, 27))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 80, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(500, 80, 256, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(240, 420, 256, 201))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 300, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(580, 300, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(320, 640, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 41, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 390, 41, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(740, 390, 41, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(770, 370, 41, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 370, 661, 20))
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "Load Starting Image..."))
        self.toolButton_2.setText(_translate("Dialog", "Load Ending Image..."))
        self.checkBox.setText(_translate("Dialog", "Show Triangles"))
        self.pushButton.setText(_translate("Dialog", "Blend"))
        self.label.setText(_translate("Dialog", "Starting Image"))
        self.label_2.setText(_translate("Dialog", "Ending Image"))
        self.label_3.setText(_translate("Dialog", "Blending Result"))
        self.label_4.setText(_translate("Dialog", "Alpha"))
        self.label_5.setText(_translate("Dialog", "0.0"))
        self.label_6.setText(_translate("Dialog", "1.0"))

