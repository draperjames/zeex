# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merge_purge.ui'
#
# Created: Thu Dec 15 19:35:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MergePurgeDialog(object):
    def setupUi(self, MergePurgeDialog):
        MergePurgeDialog.setObjectName("MergePurgeDialog")
        MergePurgeDialog.resize(740, 768)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MergePurgeDialog.sizePolicy().hasHeightForWidth())
        MergePurgeDialog.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtGui.QWidget(MergePurgeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 720, 740))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout_18 = QtGui.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.sortDropTab = QtGui.QWidget()
        self.sortDropTab.setObjectName("sortDropTab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.sortDropTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.sourcePathLabel = QtGui.QLabel(self.sortDropTab)
        self.sourcePathLabel.setObjectName("sourcePathLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.sourcePathLabel)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sourcePathSelectButton = QtGui.QPushButton(self.sortDropTab)
        self.sourcePathSelectButton.setObjectName("sourcePathSelectButton")
        self.gridLayout_2.addWidget(self.sourcePathSelectButton, 0, 1, 1, 1)
        self.sourcePathLineEdit = QtGui.QLineEdit(self.sortDropTab)
        self.sourcePathLineEdit.setObjectName("sourcePathLineEdit")
        self.gridLayout_2.addWidget(self.sourcePathLineEdit, 0, 0, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.gridLayout_2)
        self.destPathLabel = QtGui.QLabel(self.sortDropTab)
        self.destPathLabel.setObjectName("destPathLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.destPathLabel)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.destPathSelectButton = QtGui.QPushButton(self.sortDropTab)
        self.destPathSelectButton.setObjectName("destPathSelectButton")
        self.gridLayout_3.addWidget(self.destPathSelectButton, 0, 1, 1, 1)
        self.destPathLineEdit = QtGui.QLineEdit(self.sortDropTab)
        self.destPathLineEdit.setObjectName("destPathLineEdit")
        self.gridLayout_3.addWidget(self.destPathLineEdit, 0, 0, 1, 1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.gridLayout_3)
        self.sortOnLabel = QtGui.QLabel(self.sortDropTab)
        self.sortOnLabel.setObjectName("sortOnLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.sortOnLabel)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushGrid = QtGui.QGridLayout()
        self.pushGrid.setObjectName("pushGrid")
        self.sortOnRightView = QtGui.QListView(self.sortDropTab)
        self.sortOnRightView.setObjectName("sortOnRightView")
        self.pushGrid.addWidget(self.sortOnRightView, 0, 3, 1, 1)
        self.sortOnLeftView = QtGui.QListView(self.sortDropTab)
        self.sortOnLeftView.setObjectName("sortOnLeftView")
        self.pushGrid.addWidget(self.sortOnLeftView, 0, 0, 1, 1)
        self.btnGrid = QtGui.QGridLayout()
        self.btnGrid.setObjectName("btnGrid")
        self.sortOnRightButton = QtGui.QPushButton(self.sortDropTab)
        self.sortOnRightButton.setObjectName("sortOnRightButton")
        self.btnGrid.addWidget(self.sortOnRightButton, 0, 0, 1, 1)
        self.sortOnLeftButton = QtGui.QPushButton(self.sortDropTab)
        self.sortOnLeftButton.setObjectName("sortOnLeftButton")
        self.btnGrid.addWidget(self.sortOnLeftButton, 1, 0, 1, 1)
        self.pushGrid.addLayout(self.btnGrid, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.pushGrid, 0, 0, 1, 1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.gridLayout)
        self.sortAscLabel = QtGui.QLabel(self.sortDropTab)
        self.sortAscLabel.setObjectName("sortAscLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.sortAscLabel)
        self.pushGrid_2 = QtGui.QGridLayout()
        self.pushGrid_2.setObjectName("pushGrid_2")
        self.btnGrid_2 = QtGui.QGridLayout()
        self.btnGrid_2.setObjectName("btnGrid_2")
        self.sortAscRightButton = QtGui.QPushButton(self.sortDropTab)
        self.sortAscRightButton.setObjectName("sortAscRightButton")
        self.btnGrid_2.addWidget(self.sortAscRightButton, 0, 0, 1, 1)
        self.sortAscLeftButton = QtGui.QPushButton(self.sortDropTab)
        self.sortAscLeftButton.setObjectName("sortAscLeftButton")
        self.btnGrid_2.addWidget(self.sortAscLeftButton, 1, 0, 1, 1)
        self.pushGrid_2.addLayout(self.btnGrid_2, 0, 1, 1, 1)
        self.sortAscRightView = QtGui.QListView(self.sortDropTab)
        self.sortAscRightView.setObjectName("sortAscRightView")
        self.pushGrid_2.addWidget(self.sortAscRightView, 0, 2, 1, 1)
        self.sortAscLeftView = QtGui.QListView(self.sortDropTab)
        self.sortAscLeftView.setObjectName("sortAscLeftView")
        self.pushGrid_2.addWidget(self.sortAscLeftView, 0, 0, 1, 1)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.pushGrid_2)
        self.dedupeOnLabel = QtGui.QLabel(self.sortDropTab)
        self.dedupeOnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dedupeOnLabel.setOpenExternalLinks(False)
        self.dedupeOnLabel.setObjectName("dedupeOnLabel")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.dedupeOnLabel)
        self.pushGrid_3 = QtGui.QGridLayout()
        self.pushGrid_3.setObjectName("pushGrid_3")
        self.dedupeOnRightView = QtGui.QListView(self.sortDropTab)
        self.dedupeOnRightView.setObjectName("dedupeOnRightView")
        self.pushGrid_3.addWidget(self.dedupeOnRightView, 0, 2, 1, 1)
        self.btnGrid_3 = QtGui.QGridLayout()
        self.btnGrid_3.setObjectName("btnGrid_3")
        self.dedupeOnRightButton = QtGui.QPushButton(self.sortDropTab)
        self.dedupeOnRightButton.setObjectName("dedupeOnRightButton")
        self.btnGrid_3.addWidget(self.dedupeOnRightButton, 0, 0, 1, 1)
        self.dedupeOnLeftButton = QtGui.QPushButton(self.sortDropTab)
        self.dedupeOnLeftButton.setObjectName("dedupeOnLeftButton")
        self.btnGrid_3.addWidget(self.dedupeOnLeftButton, 1, 0, 1, 1)
        self.pushGrid_3.addLayout(self.btnGrid_3, 0, 1, 1, 1)
        self.dedupeOnLeftView = QtGui.QListView(self.sortDropTab)
        self.dedupeOnLeftView.setObjectName("dedupeOnLeftView")
        self.pushGrid_3.addWidget(self.dedupeOnLeftView, 0, 0, 1, 1)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.pushGrid_3)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.sortDropTab, "")
        self.mergeTab = QtGui.QWidget()
        self.mergeTab.setObjectName("mergeTab")
        self.gridLayoutWidget_7 = QtGui.QWidget(self.mergeTab)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(30, 30, 621, 621))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_14 = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.mergeFileTable = QtGui.QTableView(self.gridLayoutWidget_7)
        self.mergeFileTable.setObjectName("mergeFileTable")
        self.gridLayout_15.addWidget(self.mergeFileTable, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnAddMergeFile = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.btnAddMergeFile.setObjectName("btnAddMergeFile")
        self.horizontalLayout_5.addWidget(self.btnAddMergeFile)
        self.btnEditMergeFile = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.btnEditMergeFile.setObjectName("btnEditMergeFile")
        self.horizontalLayout_5.addWidget(self.btnEditMergeFile)
        self.btnMapMergeFields = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.btnMapMergeFields.setObjectName("btnMapMergeFields")
        self.horizontalLayout_5.addWidget(self.btnMapMergeFields)
        self.btnDeleteMergeFile = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.btnDeleteMergeFile.setObjectName("btnDeleteMergeFile")
        self.horizontalLayout_5.addWidget(self.btnDeleteMergeFile)
        self.gridLayout_15.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.btnBrowseMergeFile = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.btnBrowseMergeFile.setObjectName("btnBrowseMergeFile")
        self.gridLayout_16.addWidget(self.btnBrowseMergeFile, 0, 0, 1, 1)
        self.mergeFileLineEdit = QtGui.QLineEdit(self.gridLayoutWidget_7)
        self.mergeFileLineEdit.setObjectName("mergeFileLineEdit")
        self.gridLayout_16.addWidget(self.mergeFileLineEdit, 0, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_21 = QtGui.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QtGui.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.pushGrid_9 = QtGui.QGridLayout()
        self.pushGrid_9.setObjectName("pushGrid_9")
        self.gatherFieldsListViewLeft = QtGui.QListView(self.gridLayoutWidget_7)
        self.gatherFieldsListViewLeft.setObjectName("gatherFieldsListViewLeft")
        self.pushGrid_9.addWidget(self.gatherFieldsListViewLeft, 0, 0, 1, 1)
        self.btnGrid_9 = QtGui.QGridLayout()
        self.btnGrid_9.setObjectName("btnGrid_9")
        self.gatherFieldsButtonRight = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.gatherFieldsButtonRight.setObjectName("gatherFieldsButtonRight")
        self.btnGrid_9.addWidget(self.gatherFieldsButtonRight, 0, 0, 1, 1)
        self.gatherFieldsButtonLeft = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.gatherFieldsButtonLeft.setObjectName("gatherFieldsButtonLeft")
        self.btnGrid_9.addWidget(self.gatherFieldsButtonLeft, 1, 0, 1, 1)
        self.pushGrid_9.addLayout(self.btnGrid_9, 0, 1, 1, 1)
        self.gatherFieldsListViewRight = QtGui.QListView(self.gridLayoutWidget_7)
        self.gatherFieldsListViewRight.setObjectName("gatherFieldsListViewRight")
        self.pushGrid_9.addWidget(self.gatherFieldsListViewRight, 0, 2, 1, 1)
        self.gridLayout_20.addLayout(self.pushGrid_9, 0, 2, 1, 1)
        self.gatherFieldsLabel = QtGui.QLabel(self.gridLayoutWidget_7)
        self.gatherFieldsLabel.setObjectName("gatherFieldsLabel")
        self.gridLayout_20.addWidget(self.gatherFieldsLabel, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushGrid_8 = QtGui.QGridLayout()
        self.pushGrid_8.setObjectName("pushGrid_8")
        self.uniqueFieldsListViewLeft = QtGui.QListView(self.gridLayoutWidget_7)
        self.uniqueFieldsListViewLeft.setObjectName("uniqueFieldsListViewLeft")
        self.pushGrid_8.addWidget(self.uniqueFieldsListViewLeft, 0, 0, 1, 1)
        self.btnGrid_8 = QtGui.QGridLayout()
        self.btnGrid_8.setObjectName("btnGrid_8")
        self.uniqueFieldsPushButtonRight = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.uniqueFieldsPushButtonRight.setObjectName("uniqueFieldsPushButtonRight")
        self.btnGrid_8.addWidget(self.uniqueFieldsPushButtonRight, 0, 0, 1, 1)
        self.uniqueFieldsPushButtonLeft = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.uniqueFieldsPushButtonLeft.setObjectName("uniqueFieldsPushButtonLeft")
        self.btnGrid_8.addWidget(self.uniqueFieldsPushButtonLeft, 1, 0, 1, 1)
        self.pushGrid_8.addLayout(self.btnGrid_8, 0, 1, 1, 1)
        self.uniqueFieldsListViewRight = QtGui.QListView(self.gridLayoutWidget_7)
        self.uniqueFieldsListViewRight.setObjectName("uniqueFieldsListViewRight")
        self.pushGrid_8.addWidget(self.uniqueFieldsListViewRight, 0, 2, 1, 1)
        self.gridLayout_19.addLayout(self.pushGrid_8, 1, 1, 1, 1)
        self.uniqueFieldsLabel = QtGui.QLabel(self.gridLayoutWidget_7)
        self.uniqueFieldsLabel.setObjectName("uniqueFieldsLabel")
        self.gridLayout_19.addWidget(self.uniqueFieldsLabel, 1, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_19, 4, 0, 1, 1)
        self.gatherFieldsOverWriteCheckBox = QtGui.QCheckBox(self.gridLayoutWidget_7)
        self.gatherFieldsOverWriteCheckBox.setObjectName("gatherFieldsOverWriteCheckBox")
        self.gridLayout_21.addWidget(self.gatherFieldsOverWriteCheckBox, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem2, 3, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_21, 4, 0, 1, 1)
        self.gridLayout_22 = QtGui.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.primaryKeyComboBox = QtGui.QComboBox(self.gridLayoutWidget_7)
        self.primaryKeyComboBox.setObjectName("primaryKeyComboBox")
        self.gridLayout_22.addWidget(self.primaryKeyComboBox, 0, 1, 1, 1)
        self.primaryKeyLabel = QtGui.QLabel(self.gridLayoutWidget_7)
        self.primaryKeyLabel.setObjectName("primaryKeyLabel")
        self.gridLayout_22.addWidget(self.primaryKeyLabel, 0, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_22, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem3, 3, 0, 1, 1)
        self.tabWidget.addTab(self.mergeTab, "")
        self.suppressTab = QtGui.QWidget()
        self.suppressTab.setObjectName("suppressTab")
        self.gridLayoutWidget_5 = QtGui.QWidget(self.suppressTab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(30, 30, 621, 621))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_13 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btnBrowseSFile = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.btnBrowseSFile.setObjectName("btnBrowseSFile")
        self.gridLayout_5.addWidget(self.btnBrowseSFile, 0, 0, 1, 1)
        self.sFileLineEdit = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.sFileLineEdit.setObjectName("sFileLineEdit")
        self.gridLayout_5.addWidget(self.sFileLineEdit, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.sFileTable = QtGui.QTableView(self.gridLayoutWidget_5)
        self.sFileTable.setObjectName("sFileTable")
        self.gridLayout_6.addWidget(self.sFileTable, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddSFile = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.btnAddSFile.setObjectName("btnAddSFile")
        self.horizontalLayout_2.addWidget(self.btnAddSFile)
        self.btnEditSFile = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.btnEditSFile.setObjectName("btnEditSFile")
        self.horizontalLayout_2.addWidget(self.btnEditSFile)
        self.btnMapSFields = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.btnMapSFields.setObjectName("btnMapSFields")
        self.horizontalLayout_2.addWidget(self.btnMapSFields)
        self.btnDeleteSFile = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.btnDeleteSFile.setObjectName("btnDeleteSFile")
        self.horizontalLayout_2.addWidget(self.btnDeleteSFile)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_23 = QtGui.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.sFileStandardizeTableView = QtGui.QTableView(self.gridLayoutWidget_5)
        self.sFileStandardizeTableView.setObjectName("sFileStandardizeTableView")
        self.gridLayout_23.addWidget(self.sFileStandardizeTableView, 1, 0, 1, 1)
        self.sFileStandardizeLabel = QtGui.QLabel(self.gridLayoutWidget_5)
        self.sFileStandardizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sFileStandardizeLabel.setObjectName("sFileStandardizeLabel")
        self.gridLayout_23.addWidget(self.sFileStandardizeLabel, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_23, 2, 0, 1, 1)
        self.tabWidget.addTab(self.suppressTab, "")
        self.reviewTab = QtGui.QWidget()
        self.reviewTab.setObjectName("reviewTab")
        self.horizontalLayoutWidget = QtGui.QWidget(self.reviewTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 651))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reviewTableView = QtGui.QTableView(self.horizontalLayoutWidget)
        self.reviewTableView.setObjectName("reviewTableView")
        self.verticalLayout.addWidget(self.reviewTableView)
        self.tabWidget.addTab(self.reviewTab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_17 = QtGui.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.btnExecute = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnExecute.setObjectName("btnExecute")
        self.gridLayout_17.addWidget(self.btnExecute, 0, 0, 1, 1)
        self.btnReset = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout_17.addWidget(self.btnReset, 0, 1, 1, 1)
        self.btnExportTemplate = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnExportTemplate.setObjectName("btnExportTemplate")
        self.gridLayout_17.addWidget(self.btnExportTemplate, 0, 2, 1, 1)
        self.btnImportTemplate = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnImportTemplate.setObjectName("btnImportTemplate")
        self.gridLayout_17.addWidget(self.btnImportTemplate, 0, 3, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_17, 1, 0, 1, 1)

        self.retranslateUi(MergePurgeDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MergePurgeDialog)

    def retranslateUi(self, MergePurgeDialog):
        MergePurgeDialog.setWindowTitle(QtGui.QApplication.translate("MergePurgeDialog", "Merge/Purge", None, QtGui.QApplication.UnicodeUTF8))
        self.sourcePathLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Source Path", None, QtGui.QApplication.UnicodeUTF8))
        self.sourcePathSelectButton.setText(QtGui.QApplication.translate("MergePurgeDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.destPathLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Destination Path", None, QtGui.QApplication.UnicodeUTF8))
        self.destPathSelectButton.setText(QtGui.QApplication.translate("MergePurgeDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.sortOnLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Sort On", None, QtGui.QApplication.UnicodeUTF8))
        self.sortOnRightButton.setText(QtGui.QApplication.translate("MergePurgeDialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.sortOnLeftButton.setText(QtGui.QApplication.translate("MergePurgeDialog", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.sortAscLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Sort Ascending", None, QtGui.QApplication.UnicodeUTF8))
        self.sortAscRightButton.setText(QtGui.QApplication.translate("MergePurgeDialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.sortAscLeftButton.setText(QtGui.QApplication.translate("MergePurgeDialog", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.dedupeOnLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Dedupe On", None, QtGui.QApplication.UnicodeUTF8))
        self.dedupeOnRightButton.setText(QtGui.QApplication.translate("MergePurgeDialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.dedupeOnLeftButton.setText(QtGui.QApplication.translate("MergePurgeDialog", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sortDropTab), QtGui.QApplication.translate("MergePurgeDialog", "Sort/Dedupe", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddMergeFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditMergeFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMapMergeFields.setText(QtGui.QApplication.translate("MergePurgeDialog", "Map Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeleteMergeFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowseMergeFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.gatherFieldsButtonRight.setText(QtGui.QApplication.translate("MergePurgeDialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.gatherFieldsButtonLeft.setText(QtGui.QApplication.translate("MergePurgeDialog", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.gatherFieldsLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Fields to Gather", None, QtGui.QApplication.UnicodeUTF8))
        self.uniqueFieldsPushButtonRight.setText(QtGui.QApplication.translate("MergePurgeDialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.uniqueFieldsPushButtonLeft.setText(QtGui.QApplication.translate("MergePurgeDialog", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.uniqueFieldsLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Unique Fields     ", None, QtGui.QApplication.UnicodeUTF8))
        self.gatherFieldsOverWriteCheckBox.setText(QtGui.QApplication.translate("MergePurgeDialog", "Overwrite Existing Data", None, QtGui.QApplication.UnicodeUTF8))
        self.primaryKeyLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Primary Key", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mergeTab), QtGui.QApplication.translate("MergePurgeDialog", "Merge", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowseSFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddSFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditSFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMapSFields.setText(QtGui.QApplication.translate("MergePurgeDialog", "Map Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeleteSFile.setText(QtGui.QApplication.translate("MergePurgeDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.sFileStandardizeLabel.setText(QtGui.QApplication.translate("MergePurgeDialog", "Field Standardization", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.suppressTab), QtGui.QApplication.translate("MergePurgeDialog", "Purge", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reviewTab), QtGui.QApplication.translate("MergePurgeDialog", "Review", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExecute.setText(QtGui.QApplication.translate("MergePurgeDialog", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReset.setText(QtGui.QApplication.translate("MergePurgeDialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExportTemplate.setText(QtGui.QApplication.translate("MergePurgeDialog", "Export Template", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImportTemplate.setText(QtGui.QApplication.translate("MergePurgeDialog", "Import Template", None, QtGui.QApplication.UnicodeUTF8))

