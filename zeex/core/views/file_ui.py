# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created: Sun Dec  4 16:04:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FileWindow(object):
    def setupUi(self, FileWindow):
        FileWindow.setObjectName("FileWindow")
        FileWindow.resize(758, 571)
        self.centralwidget = QtGui.QWidget(FileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 741, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        FileWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FileWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        FileWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FileWindow)
        self.statusbar.setObjectName("statusbar")
        FileWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(FileWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDelete = QtGui.QAction(FileWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionMergePurge = QtGui.QAction(FileWindow)
        self.actionMergePurge.setObjectName("actionMergePurge")
        self.actionSuppress = QtGui.QAction(FileWindow)
        self.actionSuppress.setObjectName("actionSuppress")
        self.actionRename = QtGui.QAction(FileWindow)
        self.actionRename.setObjectName("actionRename")
        self.actionExecuteScript = QtGui.QAction(FileWindow)
        self.actionExecuteScript.setObjectName("actionExecuteScript")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionDelete)
        self.menuAction.addAction(self.actionMergePurge)
        self.menuAction.addAction(self.actionSuppress)
        self.menuAction.addAction(self.actionRename)
        self.menuAction.addAction(self.actionExecuteScript)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(FileWindow)
        QtCore.QMetaObject.connectSlotsByName(FileWindow)

    def retranslateUi(self, FileWindow):
        FileWindow.setWindowTitle(QtGui.QApplication.translate("FileWindow", "MyFile", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FileWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QtGui.QApplication.translate("FileWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("FileWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("FileWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergePurge.setText(QtGui.QApplication.translate("FileWindow", "Merge/Purge", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuppress.setText(QtGui.QApplication.translate("FileWindow", "Suppress", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setText(QtGui.QApplication.translate("FileWindow", "Rename Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExecuteScript.setText(QtGui.QApplication.translate("FileWindow", "Execute Script", None, QtGui.QApplication.UnicodeUTF8))

