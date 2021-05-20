from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ajuda_dialog
import sobre_dialog
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 301)
        Form.setMinimumSize(QSize(331, 301))
        Form.setMaximumSize(QSize(331, 301))
        Form.setStyleSheet("background-color: rgb(255, 255, 255)")
        Form.setWindowIcon(QIcon("calculadora.png"))
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(10, 40, 311, 51))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label.setStyleSheet('color: rgb(0,0,0)')
        self.label.setFrameShape(QFrame.Box)
        self.pushButton_enter = QPushButton(Form, clicked= lambda: self.remove_it())
        self.pushButton_enter.setGeometry(QRect(10, 110, 151, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_enter.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_clear = QPushButton(Form, clicked= lambda: self.press_it("Clear"))
        self.pushButton_clear.setGeometry(QRect(170, 110, 151, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_7 = QPushButton(Form, clicked= lambda: self.press_it("7"))
        self.pushButton_7.setGeometry(QRect(10, 150, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QPushButton(Form, clicked= lambda: self.press_it("8"))
        self.pushButton_8.setGeometry(QRect(90, 150, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QPushButton(Form, clicked= lambda: self.press_it("9"))
        self.pushButton_9.setGeometry(QRect(170, 150, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_mais = QPushButton(Form, clicked= lambda: self.press_it("+"))
        self.pushButton_mais.setGeometry(QRect(250, 150, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_mais.setFont(font)
        self.pushButton_mais.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_mais.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_mais.setObjectName("pushButton_mais")
        self.pushButton_zpz = QPushButton(Form, clicked= lambda: self.press_it("00"))
        self.pushButton_zpz.setGeometry(QRect(90, 240, 71, 51))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_zpz.setFont(font)
        self.pushButton_zpz.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_zpz.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_4 = QPushButton(Form, clicked= lambda: self.press_it("4"))
        self.pushButton_4.setGeometry(QRect(10, 180, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"     
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QPushButton(Form, clicked= lambda: self.press_it("5"))
        self.pushButton_5.setGeometry(QRect(90, 180, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QPushButton(Form, clicked= lambda: self.press_it("6"))
        self.pushButton_6.setGeometry(QRect(170, 180, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_menos = QPushButton(Form, clicked= lambda: self.press_it("-"))
        self.pushButton_menos.setGeometry(QRect(250, 180, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_menos.setFont(font)
        self.pushButton_menos.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menos.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_menos.setObjectName("pushButton_menos")
        self.pushButton_1 = QPushButton(Form, clicked= lambda: self.press_it("1"))
        self.pushButton_1.setGeometry(QRect(10, 210, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QPushButton(Form, clicked= lambda: self.press_it("2"))
        self.pushButton_2.setGeometry(QRect(90, 210, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(Form, clicked= lambda: self.press_it("3"))
        self.pushButton_3.setGeometry(QRect(170, 210, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_vezes = QPushButton(Form, clicked= lambda: self.press_it("*"))
        self.pushButton_vezes.setGeometry(QRect(250, 210, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_vezes.setFont(font)
        self.pushButton_vezes.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_vezes.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_vezes.setObjectName("pushButton_vezes")
        self.pushButton_divi = QPushButton(Form, clicked= lambda: self.press_it("/"))
        self.pushButton_divi.setGeometry(QRect(250, 240, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_divi.setFont(font)
        self.pushButton_divi.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_divi.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_divi.setObjectName("pushButton_divi")
        self.pushButton_0 = QPushButton(Form, clicked= lambda: self.press_it("0"))
        self.pushButton_0.setGeometry(QRect(10, 240, 71, 51))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_igual = QPushButton(Form, clicked= lambda: self.math_it())
        self.pushButton_igual.setGeometry(QRect(170, 270, 151, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_igual.setFont(font)
        self.pushButton_igual.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_igual.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_ponto = QPushButton(Form, clicked= lambda: self.dot_it())
        self.pushButton_ponto.setGeometry(QRect(170, 240, 71, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_ponto.setFont(font)
        self.pushButton_ponto.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_ponto.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_lua = QPushButton(Form)
        self.pushButton_lua.setGeometry(QRect(10, 10, 16, 16))
        self.pushButton_lua.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_lua.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")                                 #######################################
        self.pushButton_lua.clicked.connect(self.tema_escuro)
        self.pushButton_lua.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("lua.png"))
        self.pushButton_lua.setIcon(icon)
        self.pushButton_lua.setIconSize(QSize(32, 32))
        self.pushButton_lua.setObjectName("pushButton_lua")
        self.pushButton_sol = QPushButton(Form)
        self.pushButton_sol.setGeometry(QRect(40, 10, 16, 16))
        self.pushButton_sol.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sol.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_sol.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("sol.png"))
        self.pushButton_sol.setIcon(icon1)
        self.pushButton_sol.setIconSize(QSize(18, 18))
        self.pushButton_sol.setObjectName("pushButton_sol")
        self.pushButton_sol.clicked.connect(self.tema_claro)
        self.pushButton_sobre = QPushButton(Form)
        self.pushButton_sobre.setGeometry(QRect(270, 10, 51, 16))
        font = QFont()
        font.setPointSize(7)
        self.pushButton_sobre.setFont(font)
        self.pushButton_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sobre.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_sobre.setObjectName("pushButton_sobre")
        self.pushButton_sobre.clicked.connect(self.chama_tela_sobre)
        self.pushButton_ajuda = QPushButton(Form)
        self.pushButton_ajuda.setGeometry(QRect(210, 10, 51, 16))
        font = QFont()
        font.setPointSize(7)
        self.pushButton_ajuda.setFont(font)
        self.pushButton_ajuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_ajuda.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_ajuda.clicked.connect(self.chama_tela_ajuda)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)


    def remove_it(self):
        screen = self.label.text()
        screen = screen[:-1]
        self.label.setText(screen)

    def math_it(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("0")
            QMessageBox.warning(QMessageBox(), 'ERROR', 'NÃO FOI POSSIVEL REALIZAR ESTA OPERAÇÃO')

    def dot_it(self):
        screen = self.label.text()
        if screen[-1] == ".":
            pass
        else:
            self.label.setText(f'{screen}.')


    def press_it(self, pressed):
        if pressed == "Clear":
            self.label.setText("0")
        else:
            # CHECAGEM DA INICIAÇÃO 0 E DELETAÇÃO DO ZERO
            if self.label.text() == "0":
                self.label.setText("")
            self.label.setText(f'{self.label.text()}{pressed}')


    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator P1102"))
        self.label.setText(_translate("Form", "0"))
        self.pushButton_enter.setText(_translate("Form", "<<"))
        self.pushButton_enter.setShortcut(_translate("Form", "Backspace"))
        self.pushButton_clear.setText(_translate("Form", "Limpar"))
        self.pushButton_clear.setShortcut(_translate("Form", "F1"))
        self.pushButton_ponto.setText(_translate("Form", "."))
        self.pushButton_ponto.setShortcut(_translate("Form", "."))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_7.setShortcut(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_8.setShortcut(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_9.setShortcut(_translate("Form", "9"))
        self.pushButton_igual.setText(_translate("Form", "="))
        self.pushButton_igual.setShortcut(_translate("Form", "Enter"))
        self.pushButton_zpz.setText(_translate("Form", "00"))
        self.pushButton_zpz.setShortcut(_translate("Form", "Z"))
        self.pushButton_mais.setText(_translate("Form", "+"))
        self.pushButton_mais.setShortcut(_translate("Form", "+"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_4.setShortcut(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_5.setShortcut(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_6.setShortcut(_translate("Form", "6"))
        self.pushButton_menos.setText(_translate("Form", "-"))
        self.pushButton_menos.setShortcut(_translate("Form", "-"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_1.setShortcut(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_2.setShortcut(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_3.setShortcut(_translate("Form", "3"))
        self.pushButton_vezes.setText(_translate("Form", "x"))
        self.pushButton_vezes.setShortcut(_translate("Form", "*"))
        self.pushButton_divi.setText(_translate("Form", "÷"))
        self.pushButton_divi.setShortcut(_translate("Form", "/"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_0.setShortcut(_translate("Form", "0"))
        self.pushButton_sobre.setText(_translate("Form", "SOBRE"))
        self.pushButton_sobre.setShortcut(_translate("Form", "F2"))
        self.pushButton_ajuda.setText(_translate("Form", "AJUDA"))
        self.pushButton_ajuda.setShortcut(_translate("Form", "F5"))
        self.pushButton_lua.setShortcut(_translate("Form", "F3"))
        self.pushButton_sol.setShortcut(_translate("Form", "F4"))

    def tema_escuro(self):
        Form.setStyleSheet('background-color: rgb(0,0,0)')
        self.label.setStyleSheet('color: rgb(255,255,255)')
        self.pushButton_ponto.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_lua.setStyleSheet("QPushButton {\n"
        "    color:rgb(13,13,13);\n"
        "    background-color: rgb(165,165,165);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(120,120,120);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(140,140,140);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(13,13,13);\n"
        "}\n"
        "")
        self.pushButton_sol.setStyleSheet("QPushButton {\n"
        "    color:rgb(13,13,13);\n"
        "    background-color: rgb(165,165,165);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(120,120,120);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(140,140,140);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(13,13,13);\n"
        "}\n"
        "")
        self.pushButton_sobre.setStyleSheet("QPushButton {\n"
        "    color:rgb(13,13,13);\n"
        "    background-color: rgb(165,165,165);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(120,120,120);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(140,140,140);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(13,13,13);\n"
        "}\n"
        "")
        self.pushButton_ajuda.setStyleSheet("QPushButton {\n"
        "    color:rgb(13,13,13);\n"
        "    background-color: rgb(165,165,165);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(120,120,120);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(140,140,140);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(13,13,13);\n"
        "}\n"
        "")
        self.pushButton_enter.setStyleSheet("QPushButton {\n"
        "    color:rgb(13,13,13);\n"
        "    background-color: rgb(165,165,165);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(120,120,120);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(140,140,140);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(13,13,13);\n"
        "}\n"
        "")
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
        "    color:rgb(13,13,13);\n"
        "    background-color: rgb(165,165,165);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(120,120,120);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(140,140,140);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(13,13,13);\n"
        "}\n"
        "")
        self.pushButton_mais.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(254,159,10);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(254,180,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(254,200,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_menos.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(254,159,10);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(254,180,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(254,200,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_vezes.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(254,159,10);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(254,180,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(254,200,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_divi.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(254,159,10);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(254,180,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(254,200,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_0.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_zpz.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_1.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_4.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
         "}\n"
        "")
        self.pushButton_5.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_6.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_7.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_igual.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(254,159,10);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(254,180,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(254,200,20);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_8.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "")
        self.pushButton_9.setStyleSheet("QPushButton {\n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(90,90,90);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(70,70,70);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "")

    def tema_claro(self):
        Form.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label.setStyleSheet('color: rgb(0,0,0)')
        self.pushButton_ponto.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_igual.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_enter.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_0.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_zpz.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_1.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_ajuda.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_4.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_5.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_6.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_7.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_8.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_9.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(219,219,219);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_mais.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_menos.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_vezes.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_divi.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_lua.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_sol.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")
        self.pushButton_sobre.setStyleSheet("QPushButton {\n"
        "    color:rgb(0,0,0);\n"
        "    background-color: rgb(190,190,190);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(30,215,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30,245,95);\n"
        "    /*border: 2px solid rgb(255,0,0);*/\n"
        "    color: rgb(0,0,0);\n"
        "}\n"
        "")

    def chama_tela_ajuda(self):
        self.janela = QDialog()
        self.tela = ajuda_dialog.Ui_Dialog()
        self.tela.setupUi(self.janela)
        self.janela.show()

    def chama_tela_sobre(self):
        self.janela = QDialog()
        self.tela = sobre_dialog.Ui_Dialog()
        self.tela.setupUi(self.janela)
        self.janela.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
