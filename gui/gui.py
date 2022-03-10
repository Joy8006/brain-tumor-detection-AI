# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from fileinput import filename
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow
import sys
import cv2
from keras.models import load_model
import numpy as np
from PIL import Image


model = load_model('BrainTumor10Epochs.h5')


class Ui_MainWindow(QMainWindow):

    def importFiles(self):
        global fileName
        x = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Machine Learnings\\ML_Projects\\brain-tumor-detection-AI\\Data\\pred', 'Images (*.png, *.jpg)')
        fileName = x[0]
        self.image.setPixmap(QtGui.QPixmap(fileName))
        
        return fileName


    def result(self):
        
        image = cv2.imread(fileName)
        img = Image.fromarray(image)
        image = img.resize((64,64))
        image = np.array(image)
        input_image = np.expand_dims(image, axis=0)
        prediction = model.predict(input_image)
        if(prediction[0]==0):
            self.image.setText("Congratulations!! You are safe..")
            # self.image.adjustSize()
            
            self.image.setStyleSheet("color: rgb(0, 255, 0);\n")
        elif(prediction[0]==1):
            self.image.setText("Sorry to say but you have brain tumor..")
            # self.image.adjustSize()
            self.image.setStyleSheet("color: rgb(255, 0, 0);\n")
        else:
            self.image.setText("Please provide another clear mri!!")
            # self.image.adjustSize()
            self.image.setStyleSheet("color: rgb(255, 0, 0);\n")
        print(prediction[0])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 100, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setGeometry(QtCore.QRect(225, 160, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.importButton.setFont(font)
        self.importButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.importButton.setStyleSheet("background-color: rgb(16, 75, 23);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"")
        self.importButton.setCheckable(False)
        self.importButton.setFlat(False)
        self.importButton.setObjectName("importButton")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(190, 220, 400, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(10)
        self.image.setFont(font)
        self.image.setText("")
        
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        # self.image.setPixmap(QtGui.QPixmap())
        self.resultButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultButton.setGeometry(QtCore.QRect(430, 160, 110, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultButton.setFont(font)
        self.resultButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 85, 14);\n"
"border-radius: 15px;")
        self.resultButton.setObjectName("resultButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.importButton.clicked.connect(self.importFiles)
        self.resultButton.clicked.connect(self.result)
        
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Brain Tumor Detection AI"))
        self.label.setText(_translate("MainWindow", "Brain Tumor Detection System"))
        self.label.adjustSize()
        self.importButton.setText(_translate("MainWindow", "Select files"))
        self.resultButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
