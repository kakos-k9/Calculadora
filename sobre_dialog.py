from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)
        Dialog.setMinimumSize(QSize(450, 300))
        Dialog.setMaximumSize(QSize(450, 300))
        Dialog.setWindowIcon(QIcon('calculadora.png'))
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 81, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(10, 50, 275, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(10, 270, 188, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(10, 120, 400, 61))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sobre"))
        self.label.setText(_translate("Dialog", "Sobre"))
        self.label_2.setText(_translate("Dialog", "Calculator P1102  V2.0 Copyright © 2021 Kaique Afonso\n"
        "Todos os Direitos Reservados."))
        self.label_3.setText(_translate("Dialog", "kaiqueafonsoferreira21@gmail.com"))
        self.label_4.setText(_translate("Dialog", "\"Sem tradição não pode haver virtude, nem dignidade, nem independência,\n"
        " nem amor à glória. Sem tradição, cada um procura o júbilo material, os\n"
        " prazeres, o dinheiro, as posições e os cargos, porém jamais procura\n"
        " os caminhos do dever para com Deus e a pátria.\""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
