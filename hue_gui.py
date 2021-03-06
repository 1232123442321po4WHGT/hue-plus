# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hue-gui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.channel1Check = QtWidgets.QCheckBox(self.centralwidget)
        self.channel1Check.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.channel1Check.setChecked(True)
        self.channel1Check.setObjectName("channel1Check")
        self.channel2Check = QtWidgets.QCheckBox(self.centralwidget)
        self.channel2Check.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.channel2Check.setChecked(True)
        self.channel2Check.setObjectName("channel2Check")
        self.modeWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.modeWidget.setGeometry(QtCore.QRect(10, 50, 921, 451))
        self.modeWidget.setObjectName("modeWidget")
        self.presetTab = QtWidgets.QWidget()
        self.presetTab.setObjectName("presetTab")
        self.presetModeWidget = QtWidgets.QTabWidget(self.presetTab)
        self.presetModeWidget.setGeometry(QtCore.QRect(6, 9, 901, 411))
        self.presetModeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.presetModeWidget.setObjectName("presetModeWidget")
        self.fixedTab = QtWidgets.QWidget()
        self.fixedTab.setObjectName("fixedTab")
        self.groupBox = QtWidgets.QGroupBox(self.fixedTab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox.setObjectName("groupBox")
        self.fixedList = QtWidgets.QListWidget(self.groupBox)
        self.fixedList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.fixedList.setObjectName("fixedList")
        self.fixedAdd = QtWidgets.QPushButton(self.groupBox)
        self.fixedAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.fixedAdd.setObjectName("fixedAdd")
        self.fixedDelete = QtWidgets.QPushButton(self.groupBox)
        self.fixedDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.fixedDelete.setObjectName("fixedDelete")
        self.presetModeWidget.addTab(self.fixedTab, "")
        self.breathingTab = QtWidgets.QWidget()
        self.breathingTab.setObjectName("breathingTab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.breathingTab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.breathingList = QtWidgets.QListWidget(self.groupBox_2)
        self.breathingList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.breathingList.setObjectName("breathingList")
        self.breathingAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.breathingAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.breathingAdd.setObjectName("breathingAdd")
        self.breathingDelete = QtWidgets.QPushButton(self.groupBox_2)
        self.breathingDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.breathingDelete.setObjectName("breathingDelete")
        self.groupBox_11 = QtWidgets.QGroupBox(self.breathingTab)
        self.groupBox_11.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_11.setObjectName("groupBox_11")
        self.breathingSpeed = QtWidgets.QSlider(self.groupBox_11)
        self.breathingSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.breathingSpeed.setMaximum(4)
        self.breathingSpeed.setProperty("value", 2)
        self.breathingSpeed.setOrientation(QtCore.Qt.Vertical)
        self.breathingSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.breathingSpeed.setObjectName("breathingSpeed")
        self.label_2 = QtWidgets.QLabel(self.groupBox_11)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_11)
        self.label_4.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_11)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_5.setObjectName("label_5")
        self.presetModeWidget.addTab(self.breathingTab, "")
        self.fadingTab = QtWidgets.QWidget()
        self.fadingTab.setObjectName("fadingTab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.fadingTab)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_3.setObjectName("groupBox_3")
        self.fadingList = QtWidgets.QListWidget(self.groupBox_3)
        self.fadingList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.fadingList.setObjectName("fadingList")
        self.fadingAdd = QtWidgets.QPushButton(self.groupBox_3)
        self.fadingAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.fadingAdd.setObjectName("fadingAdd")
        self.fadingDelete = QtWidgets.QPushButton(self.groupBox_3)
        self.fadingDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.fadingDelete.setObjectName("fadingDelete")
        self.groupBox_12 = QtWidgets.QGroupBox(self.fadingTab)
        self.groupBox_12.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_12.setObjectName("groupBox_12")
        self.fadingSpeed = QtWidgets.QSlider(self.groupBox_12)
        self.fadingSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.fadingSpeed.setMaximum(4)
        self.fadingSpeed.setProperty("value", 2)
        self.fadingSpeed.setOrientation(QtCore.Qt.Vertical)
        self.fadingSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.fadingSpeed.setObjectName("fadingSpeed")
        self.label_9 = QtWidgets.QLabel(self.groupBox_12)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_12)
        self.label_10.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_12)
        self.label_11.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_11.setObjectName("label_11")
        self.presetModeWidget.addTab(self.fadingTab, "")
        self.marqueeTab = QtWidgets.QWidget()
        self.marqueeTab.setObjectName("marqueeTab")
        self.groupBox_4 = QtWidgets.QGroupBox(self.marqueeTab)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_4.setObjectName("groupBox_4")
        self.marqueeList = QtWidgets.QListWidget(self.groupBox_4)
        self.marqueeList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.marqueeList.setObjectName("marqueeList")
        self.marqueeAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.marqueeAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.marqueeAdd.setObjectName("marqueeAdd")
        self.marqueeDelete = QtWidgets.QPushButton(self.groupBox_4)
        self.marqueeDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.marqueeDelete.setObjectName("marqueeDelete")
        self.groupBox_13 = QtWidgets.QGroupBox(self.marqueeTab)
        self.groupBox_13.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_13.setObjectName("groupBox_13")
        self.marqueeSpeed = QtWidgets.QSlider(self.groupBox_13)
        self.marqueeSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.marqueeSpeed.setMaximum(4)
        self.marqueeSpeed.setProperty("value", 2)
        self.marqueeSpeed.setOrientation(QtCore.Qt.Vertical)
        self.marqueeSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.marqueeSpeed.setObjectName("marqueeSpeed")
        self.label_15 = QtWidgets.QLabel(self.groupBox_13)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_13)
        self.label_16.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_13)
        self.label_17.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_17.setObjectName("label_17")
        self.marqueeSize = QtWidgets.QSlider(self.groupBox_13)
        self.marqueeSize.setGeometry(QtCore.QRect(185, 70, 31, 160))
        self.marqueeSize.setMaximum(3)
        self.marqueeSize.setProperty("value", 2)
        self.marqueeSize.setOrientation(QtCore.Qt.Vertical)
        self.marqueeSize.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.marqueeSize.setObjectName("marqueeSize")
        self.label_18 = QtWidgets.QLabel(self.groupBox_13)
        self.label_18.setGeometry(QtCore.QRect(240, 210, 62, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_13)
        self.label_19.setGeometry(QtCore.QRect(180, 40, 62, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_13)
        self.label_20.setGeometry(QtCore.QRect(240, 60, 62, 20))
        self.label_20.setObjectName("label_20")
        self.marqueeBackwards = QtWidgets.QCheckBox(self.groupBox_13)
        self.marqueeBackwards.setGeometry(QtCore.QRect(20, 260, 89, 26))
        self.marqueeBackwards.setObjectName("marqueeBackwards")
        self.presetModeWidget.addTab(self.marqueeTab, "")
        self.coverMarqueeTab = QtWidgets.QWidget()
        self.coverMarqueeTab.setObjectName("coverMarqueeTab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.coverMarqueeTab)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_5.setObjectName("groupBox_5")
        self.coverMarqueeList = QtWidgets.QListWidget(self.groupBox_5)
        self.coverMarqueeList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.coverMarqueeList.setObjectName("coverMarqueeList")
        self.coverMarqueeAdd = QtWidgets.QPushButton(self.groupBox_5)
        self.coverMarqueeAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.coverMarqueeAdd.setObjectName("coverMarqueeAdd")
        self.coverMarqueeDelete = QtWidgets.QPushButton(self.groupBox_5)
        self.coverMarqueeDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.coverMarqueeDelete.setObjectName("coverMarqueeDelete")
        self.groupBox_15 = QtWidgets.QGroupBox(self.coverMarqueeTab)
        self.groupBox_15.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_15.setObjectName("groupBox_15")
        self.coverMarqueeSpeed = QtWidgets.QSlider(self.groupBox_15)
        self.coverMarqueeSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.coverMarqueeSpeed.setMaximum(4)
        self.coverMarqueeSpeed.setProperty("value", 2)
        self.coverMarqueeSpeed.setOrientation(QtCore.Qt.Vertical)
        self.coverMarqueeSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.coverMarqueeSpeed.setObjectName("coverMarqueeSpeed")
        self.label_27 = QtWidgets.QLabel(self.groupBox_15)
        self.label_27.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_15)
        self.label_28.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_15)
        self.label_29.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_29.setObjectName("label_29")
        self.coverMarqueeBackwards = QtWidgets.QCheckBox(self.groupBox_15)
        self.coverMarqueeBackwards.setGeometry(QtCore.QRect(20, 260, 89, 26))
        self.coverMarqueeBackwards.setObjectName("coverMarqueeBackwards")
        self.presetModeWidget.addTab(self.coverMarqueeTab, "")
        self.pulseTab = QtWidgets.QWidget()
        self.pulseTab.setObjectName("pulseTab")
        self.groupBox_6 = QtWidgets.QGroupBox(self.pulseTab)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pulseList = QtWidgets.QListWidget(self.groupBox_6)
        self.pulseList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.pulseList.setObjectName("pulseList")
        self.pulseAdd = QtWidgets.QPushButton(self.groupBox_6)
        self.pulseAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.pulseAdd.setObjectName("pulseAdd")
        self.pulseDelete = QtWidgets.QPushButton(self.groupBox_6)
        self.pulseDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.pulseDelete.setObjectName("pulseDelete")
        self.groupBox_16 = QtWidgets.QGroupBox(self.pulseTab)
        self.groupBox_16.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_16.setObjectName("groupBox_16")
        self.pulseSpeed = QtWidgets.QSlider(self.groupBox_16)
        self.pulseSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.pulseSpeed.setMaximum(4)
        self.pulseSpeed.setProperty("value", 2)
        self.pulseSpeed.setOrientation(QtCore.Qt.Vertical)
        self.pulseSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.pulseSpeed.setObjectName("pulseSpeed")
        self.label_33 = QtWidgets.QLabel(self.groupBox_16)
        self.label_33.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_16)
        self.label_34.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox_16)
        self.label_35.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_35.setObjectName("label_35")
        self.presetModeWidget.addTab(self.pulseTab, "")
        self.spectrumTab = QtWidgets.QWidget()
        self.spectrumTab.setObjectName("spectrumTab")
        self.groupBox_17 = QtWidgets.QGroupBox(self.spectrumTab)
        self.groupBox_17.setGeometry(QtCore.QRect(0, 0, 321, 361))
        self.groupBox_17.setObjectName("groupBox_17")
        self.spectrumSpeed = QtWidgets.QSlider(self.groupBox_17)
        self.spectrumSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.spectrumSpeed.setMaximum(4)
        self.spectrumSpeed.setProperty("value", 2)
        self.spectrumSpeed.setOrientation(QtCore.Qt.Vertical)
        self.spectrumSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.spectrumSpeed.setObjectName("spectrumSpeed")
        self.label_39 = QtWidgets.QLabel(self.groupBox_17)
        self.label_39.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_17)
        self.label_40.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_17)
        self.label_41.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_41.setObjectName("label_41")
        self.spectrumBackwards = QtWidgets.QCheckBox(self.groupBox_17)
        self.spectrumBackwards.setGeometry(QtCore.QRect(20, 260, 89, 26))
        self.spectrumBackwards.setObjectName("spectrumBackwards")
        self.presetModeWidget.addTab(self.spectrumTab, "")
        self.alternatingTab = QtWidgets.QWidget()
        self.alternatingTab.setObjectName("alternatingTab")
        self.groupBox_7 = QtWidgets.QGroupBox(self.alternatingTab)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_7.setObjectName("groupBox_7")
        self.alternatingList = QtWidgets.QListWidget(self.groupBox_7)
        self.alternatingList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.alternatingList.setObjectName("alternatingList")
        self.alternatingAdd = QtWidgets.QPushButton(self.groupBox_7)
        self.alternatingAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.alternatingAdd.setObjectName("alternatingAdd")
        self.alternatingDelete = QtWidgets.QPushButton(self.groupBox_7)
        self.alternatingDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.alternatingDelete.setObjectName("alternatingDelete")
        self.groupBox_18 = QtWidgets.QGroupBox(self.alternatingTab)
        self.groupBox_18.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_18.setObjectName("groupBox_18")
        self.alternatingSpeed = QtWidgets.QSlider(self.groupBox_18)
        self.alternatingSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.alternatingSpeed.setMaximum(4)
        self.alternatingSpeed.setProperty("value", 2)
        self.alternatingSpeed.setOrientation(QtCore.Qt.Vertical)
        self.alternatingSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.alternatingSpeed.setObjectName("alternatingSpeed")
        self.label_45 = QtWidgets.QLabel(self.groupBox_18)
        self.label_45.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_18)
        self.label_46.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.groupBox_18)
        self.label_47.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_47.setObjectName("label_47")
        self.alternatingSize = QtWidgets.QSlider(self.groupBox_18)
        self.alternatingSize.setGeometry(QtCore.QRect(185, 70, 31, 160))
        self.alternatingSize.setMaximum(3)
        self.alternatingSize.setProperty("value", 2)
        self.alternatingSize.setOrientation(QtCore.Qt.Vertical)
        self.alternatingSize.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.alternatingSize.setObjectName("alternatingSize")
        self.label_48 = QtWidgets.QLabel(self.groupBox_18)
        self.label_48.setGeometry(QtCore.QRect(240, 210, 62, 20))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.groupBox_18)
        self.label_49.setGeometry(QtCore.QRect(180, 40, 62, 20))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_18)
        self.label_50.setGeometry(QtCore.QRect(240, 60, 62, 20))
        self.label_50.setObjectName("label_50")
        self.alternatingBackwards = QtWidgets.QCheckBox(self.groupBox_18)
        self.alternatingBackwards.setGeometry(QtCore.QRect(20, 260, 89, 26))
        self.alternatingBackwards.setObjectName("alternatingBackwards")
        self.alternatingMoving = QtWidgets.QCheckBox(self.groupBox_18)
        self.alternatingMoving.setGeometry(QtCore.QRect(20, 290, 89, 26))
        self.alternatingMoving.setObjectName("alternatingMoving")
        self.presetModeWidget.addTab(self.alternatingTab, "")
        self.candleTab = QtWidgets.QWidget()
        self.candleTab.setObjectName("candleTab")
        self.groupBox_8 = QtWidgets.QGroupBox(self.candleTab)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_8.setObjectName("groupBox_8")
        self.candleList = QtWidgets.QListWidget(self.groupBox_8)
        self.candleList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.candleList.setObjectName("candleList")
        self.candleAdd = QtWidgets.QPushButton(self.groupBox_8)
        self.candleAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.candleAdd.setObjectName("candleAdd")
        self.candleDelete = QtWidgets.QPushButton(self.groupBox_8)
        self.candleDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.candleDelete.setObjectName("candleDelete")
        self.presetModeWidget.addTab(self.candleTab, "")
        self.wingsTab = QtWidgets.QWidget()
        self.wingsTab.setObjectName("wingsTab")
        self.groupBox_9 = QtWidgets.QGroupBox(self.wingsTab)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox_9.setObjectName("groupBox_9")
        self.wingsList = QtWidgets.QListWidget(self.groupBox_9)
        self.wingsList.setGeometry(QtCore.QRect(10, 50, 111, 291))
        self.wingsList.setObjectName("wingsList")
        self.wingsAdd = QtWidgets.QPushButton(self.groupBox_9)
        self.wingsAdd.setGeometry(QtCore.QRect(130, 50, 83, 28))
        self.wingsAdd.setObjectName("wingsAdd")
        self.wingsDelete = QtWidgets.QPushButton(self.groupBox_9)
        self.wingsDelete.setGeometry(QtCore.QRect(130, 90, 83, 28))
        self.wingsDelete.setObjectName("wingsDelete")
        self.groupBox_20 = QtWidgets.QGroupBox(self.wingsTab)
        self.groupBox_20.setGeometry(QtCore.QRect(240, 0, 321, 361))
        self.groupBox_20.setObjectName("groupBox_20")
        self.wingsSpeed = QtWidgets.QSlider(self.groupBox_20)
        self.wingsSpeed.setGeometry(QtCore.QRect(15, 70, 31, 160))
        self.wingsSpeed.setMaximum(4)
        self.wingsSpeed.setProperty("value", 2)
        self.wingsSpeed.setOrientation(QtCore.Qt.Vertical)
        self.wingsSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.wingsSpeed.setObjectName("wingsSpeed")
        self.label_57 = QtWidgets.QLabel(self.groupBox_20)
        self.label_57.setGeometry(QtCore.QRect(10, 40, 62, 20))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_20)
        self.label_58.setGeometry(QtCore.QRect(70, 60, 62, 20))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_20)
        self.label_59.setGeometry(QtCore.QRect(70, 210, 62, 20))
        self.label_59.setObjectName("label_59")
        self.presetModeWidget.addTab(self.wingsTab, "")
        self.modeWidget.addTab(self.presetTab, "")
        self.applyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.applyBtn.setGeometry(QtCore.QRect(310, 510, 101, 41))
        self.applyBtn.setObjectName("applyBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 62, 20))
        self.label.setObjectName("label")
        self.portTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.portTxt.setGeometry(QtCore.QRect(150, 20, 113, 28))
        self.portTxt.setObjectName("portTxt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.modeWidget.setCurrentIndex(0)
        self.presetModeWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.channel1Check, self.channel2Check)
        MainWindow.setTabOrder(self.channel2Check, self.modeWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.channel1Check.setText(_translate("MainWindow", "Channel 1"))
        self.channel2Check.setText(_translate("MainWindow", "Channel 2"))
        self.groupBox.setTitle(_translate("MainWindow", "Colors"))
        self.fixedAdd.setText(_translate("MainWindow", "Add color"))
        self.fixedDelete.setText(_translate("MainWindow", "Delete color"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.fixedTab), _translate("MainWindow", "Fixed"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Colors"))
        self.breathingAdd.setText(_translate("MainWindow", "Add color"))
        self.breathingDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Other"))
        self.label_2.setText(_translate("MainWindow", "Speed"))
        self.label_4.setText(_translate("MainWindow", "Fastest"))
        self.label_5.setText(_translate("MainWindow", "Slowest"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.breathingTab), _translate("MainWindow", "Breathing"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Colors"))
        self.fadingAdd.setText(_translate("MainWindow", "Add color"))
        self.fadingDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Other"))
        self.label_9.setText(_translate("MainWindow", "Speed"))
        self.label_10.setText(_translate("MainWindow", "Fastest"))
        self.label_11.setText(_translate("MainWindow", "Slowest"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.fadingTab), _translate("MainWindow", "Fading"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Colors"))
        self.marqueeAdd.setText(_translate("MainWindow", "Add color"))
        self.marqueeDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Other"))
        self.label_15.setText(_translate("MainWindow", "Speed"))
        self.label_16.setText(_translate("MainWindow", "Fastest"))
        self.label_17.setText(_translate("MainWindow", "Slowest"))
        self.label_18.setText(_translate("MainWindow", "Smaller"))
        self.label_19.setText(_translate("MainWindow", "Size"))
        self.label_20.setText(_translate("MainWindow", "Larger"))
        self.marqueeBackwards.setText(_translate("MainWindow", "Backwards"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.marqueeTab), _translate("MainWindow", "Marquee"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Colors"))
        self.coverMarqueeAdd.setText(_translate("MainWindow", "Add color"))
        self.coverMarqueeDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Other"))
        self.label_27.setText(_translate("MainWindow", "Speed"))
        self.label_28.setText(_translate("MainWindow", "Fastest"))
        self.label_29.setText(_translate("MainWindow", "Slowest"))
        self.coverMarqueeBackwards.setText(_translate("MainWindow", "Backwards"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.coverMarqueeTab), _translate("MainWindow", "Covering Marquee"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Colors"))
        self.pulseAdd.setText(_translate("MainWindow", "Add color"))
        self.pulseDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Other"))
        self.label_33.setText(_translate("MainWindow", "Speed"))
        self.label_34.setText(_translate("MainWindow", "Fastest"))
        self.label_35.setText(_translate("MainWindow", "Slowest"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.pulseTab), _translate("MainWindow", "Pulse"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Other"))
        self.label_39.setText(_translate("MainWindow", "Speed"))
        self.label_40.setText(_translate("MainWindow", "Fastest"))
        self.label_41.setText(_translate("MainWindow", "Slowest"))
        self.spectrumBackwards.setText(_translate("MainWindow", "Backwards"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.spectrumTab), _translate("MainWindow", "Spectrum"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Colors"))
        self.alternatingAdd.setText(_translate("MainWindow", "Add color"))
        self.alternatingDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Other"))
        self.label_45.setText(_translate("MainWindow", "Speed"))
        self.label_46.setText(_translate("MainWindow", "Fastest"))
        self.label_47.setText(_translate("MainWindow", "Slowest"))
        self.label_48.setText(_translate("MainWindow", "Smaller"))
        self.label_49.setText(_translate("MainWindow", "Size"))
        self.label_50.setText(_translate("MainWindow", "Larger"))
        self.alternatingBackwards.setText(_translate("MainWindow", "Backwards"))
        self.alternatingMoving.setText(_translate("MainWindow", "Moving"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.alternatingTab), _translate("MainWindow", "Alternating"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Colors"))
        self.candleAdd.setText(_translate("MainWindow", "Add color"))
        self.candleDelete.setText(_translate("MainWindow", "Delete color"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.candleTab), _translate("MainWindow", "Candle"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Colors"))
        self.wingsAdd.setText(_translate("MainWindow", "Add color"))
        self.wingsDelete.setText(_translate("MainWindow", "Delete color"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Other"))
        self.label_57.setText(_translate("MainWindow", "Speed"))
        self.label_58.setText(_translate("MainWindow", "Fastest"))
        self.label_59.setText(_translate("MainWindow", "Slowest"))
        self.presetModeWidget.setTabText(self.presetModeWidget.indexOf(self.wingsTab), _translate("MainWindow", "Wings"))
        self.modeWidget.setTabText(self.modeWidget.indexOf(self.presetTab), _translate("MainWindow", "Preset"))
        self.applyBtn.setText(_translate("MainWindow", "Apply"))
        self.label.setText(_translate("MainWindow", "Port:"))
        self.portTxt.setText(_translate("MainWindow", "/dev/ttyACM0"))

