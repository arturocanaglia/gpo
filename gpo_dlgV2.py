# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rosa/bin/Py/Gui/gpo_dlgV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GPO(object):
    def setupUi(self, GPO):
        GPO.setObjectName("GPO")
        GPO.resize(627, 257)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GPO.sizePolicy().hasHeightForWidth())
        GPO.setSizePolicy(sizePolicy)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/rosa/bin/Py/Gui/../../../../../usr/share/icons/AdwaitaLegacy/32x32/legacy/dialog-password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("/home/rosa/bin/Py/Gui/../../../../../usr/share/icons/AdwaitaLegacy/32x32/legacy/dialog-password.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        GPO.setWindowIcon(icon)
        #GPO.setModal(False)
        self.label = QtWidgets.QLabel(GPO)
        self.label.setGeometry(QtCore.QRect(30, 20, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(GPO)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 17))
        self.label_2.setObjectName("label_2")
        self.cmbUrl = QtWidgets.QComboBox(GPO)
        self.cmbUrl.setEnabled(True)
        self.cmbUrl.setGeometry(QtCore.QRect(30, 120, 231, 31))
        self.cmbUrl.setEditable(True)
        self.cmbUrl.setObjectName("cmbUrl")
        self.btnCrea = QtWidgets.QPushButton(GPO)
        self.btnCrea.setGeometry(QtCore.QRect(510, 40, 80, 31))
        self.btnCrea.setObjectName("btnCrea")
        self.btnCopy = QtWidgets.QPushButton(GPO)
        self.btnCopy.setGeometry(QtCore.QRect(510, 120, 80, 31))
        self.btnCopy.setObjectName("btnCopy")
        self.btnSal = QtWidgets.QPushButton(GPO)
        self.btnSal.setGeometry(QtCore.QRect(190, 190, 71, 31))
        self.btnSal.setObjectName("btnSal")
        self.label_3 = QtWidgets.QLabel(GPO)
        self.label_3.setGeometry(QtCore.QRect(270, 20, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(GPO)
        self.label_4.setGeometry(QtCore.QRect(270, 100, 81, 17))
        self.label_4.setObjectName("label_4")
        self.btnChiudi = QtWidgets.QPushButton(GPO)
        self.btnChiudi.setGeometry(QtCore.QRect(510, 190, 81, 31))
        self.btnChiudi.setObjectName("btnChiudi")
        self.line = QtWidgets.QFrame(GPO)
        self.line.setGeometry(QtCore.QRect(30, 80, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnPulisci = QtWidgets.QPushButton(GPO)
        self.btnPulisci.setGeometry(QtCore.QRect(30, 190, 71, 31))
        self.btnPulisci.setObjectName("btnPulisci")
        self.lblUrl = QtWidgets.QLineEdit(GPO)
        self.lblUrl.setGeometry(QtCore.QRect(30, 40, 231, 31))
        self.lblUrl.setObjectName("lblUrl")
        self.lblPwd = QtWidgets.QLineEdit(GPO)
        self.lblPwd.setGeometry(QtCore.QRect(270, 40, 231, 31))
        self.lblPwd.setObjectName("lblPwd")
        self.lblPwdSav = QtWidgets.QLineEdit(GPO)
        self.lblPwdSav.setGeometry(QtCore.QRect(270, 120, 231, 31))
        self.lblPwdSav.setReadOnly(False)
        self.lblPwdSav.setObjectName("lblPwdSav")
        self.lbUti = QtWidgets.QLineEdit(GPO)
        self.lbUti.setGeometry(QtCore.QRect(270, 190, 231, 31))
        self.lbUti.setReadOnly(False)
        self.lbUti.setObjectName("lbUti")
        self.label_5 = QtWidgets.QLabel(GPO)
        self.label_5.setGeometry(QtCore.QRect(270, 170, 81, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(GPO)
        QtCore.QMetaObject.connectSlotsByName(GPO)

    def retranslateUi(self, GPO):
        _translate = QtCore.QCoreApplication.translate
        GPO.setWindowTitle(_translate("GPO", "Gestione Password"))
        self.label.setText(_translate("GPO", "Url"))
        self.label_2.setText(_translate("GPO", "Utente"))
        self.btnCrea.setText(_translate("GPO", "Crea"))
        self.btnCopy.setText(_translate("GPO", "Copia"))
        self.btnSal.setText(_translate("GPO", "Salva"))
        self.label_3.setText(_translate("GPO", "Password"))
        self.label_4.setText(_translate("GPO", "Password"))
        self.btnChiudi.setText(_translate("GPO", "Chiudi"))
        self.btnPulisci.setText(_translate("GPO", "Pulisci"))
        self.label_5.setText(_translate("GPO", "Utente"))
