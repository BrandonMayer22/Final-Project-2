from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import sys, res_rc


class Ui_Form_Login(object):
    """
    Class to set up the user interface for the login form.
    """

    def setupUi(self, Form_Login: QtWidgets.QWidget) -> None:
        """
        Sets up the UI elements for the login form.

        This includes creating and configuring various UI components such as buttons, labels, and input fields.
        The function also sets styles for different widgets and defines their layout on the form.

        Args:
            Form_Login (QtWidgets.QWidget): The main window (form) that will contain all the UI elements.
        """
        Form_Login.setObjectName("Form_Login")
        Form_Login.resize(597, 952)
        Form_Login.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form_Login.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.widget_Login = QtWidgets.QWidget(parent=Form_Login)
        self.widget_Login.setGeometry(QtCore.QRect(40, 10, 475, 940))
        self.widget_Login.setStyleSheet(
            "QPushButton#pushButton_Login {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, \n"
            "        stop:0 rgba(58, 32, 85, 219), \n"
            "        stop:1 rgba(207, 159, 36, 226));\n"
            "    color:rgba(255, 223, 186, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QPushButton#pushButton_Login:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, \n"
            "        stop:0 rgba(80, 50, 130, 255), \n"
            "        stop:1 rgba(255, 200, 50, 255));\n"
            "    color: rgba(255, 255, 255, 255);\n"
            "}\n"
            "QPushButton#pushButton_Login:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(150, 130, 20, 200);\n"
            "}\n"
            "QPushButton#pushButton_Signup {\n"
            "    background-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, \n"
            "        stop:0 rgba(58, 32, 85, 219), \n"
            "        stop:1 rgba(207, 159, 36, 226));\n"
            "    color:rgba(255, 223, 186, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QPushButton#pushButton_Signup:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, \n"
            "        stop:0 rgba(80, 50, 130, 255), \n"
            "        stop:1 rgba(255, 200, 50, 255));\n"
            "    color: rgba(255, 255, 255, 255);\n"
            "}\n"
            "QPushButton#pushButton_Signup:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(150, 130, 20, 200);\n"
            "}\n"
            "QPushButton#pushButton_SM1, #pushButton_SM2, #pushButton_SM3, #pushButton_SM4 {\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "    color:rgba(85, 98, 112, 255);\n"
            "}\n"
            "QPushButton#pushButton_SM1:hover, #pushButton_SM2:hover, #pushButton_SM3:hover, #pushButton_SM4:hover {\n"
            "    color: rgba(155, 168, 182, 220);\n"
            "}\n"
            "QPushButton#pushButton_SM1:pressed, #pushButton_SM2:pressed, #pushButton_SM3:pressed, #pushButton_SM4:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(115, 128, 142, 255);\n"
            "}"
        )

        self.widget_Login.setObjectName("widget_Login")
        self.label_Spacebg = QtWidgets.QLabel(parent=self.widget_Login)
        self.label_Spacebg.setGeometry(QtCore.QRect(30, 10, 414, 896))
        self.label_Spacebg.setAutoFillBackground(False)
        self.label_Spacebg.setStyleSheet(
            "background-image: url(:/Image/space2.png);\n" "border-radius: 20px;"
        )
        self.label_Spacebg.setText("")
        self.label_Spacebg.setObjectName("label_Spacebg")

        self.label_Spacebg2 = QtWidgets.QLabel(parent=self.widget_Login)
        self.label_Spacebg2.setGeometry(QtCore.QRect(30, 10, 414, 896))
        self.label_Spacebg2.setAutoFillBackground(False)
        self.label_Spacebg2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
            "border-radius: 20px;"
        )
        self.label_Spacebg2.setText("")
        self.label_Spacebg2.setObjectName("label_Spacebg2")

        self.label_Logo = QtWidgets.QLabel(parent=self.widget_Login)
        self.label_Logo.setGeometry(QtCore.QRect(110, 20, 250, 250))
        self.label_Logo.setStyleSheet(
            "background-image: url(:/Image/GALACTIC READS Yellow.png);"
        )
        self.label_Logo.setText("")
        self.label_Logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Logo.setObjectName("label_Logo")

        self.lineEdit_Email = QtWidgets.QLineEdit(parent=self.widget_Login)
        self.lineEdit_Email.setGeometry(QtCore.QRect(130, 300, 220, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)

        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setStyleSheet(
            "QLineEdit {\n"
            "    border: 2px solid rgba(255, 223, 186, 150); /* Golden border */\n"
            "    border-radius: 10px;\n"
            "    padding: 5px;\n"
            "    background: rgba(255, 255, 255, 230); /* Slight transparency */\n"
            "}\n"
            ""
        )
        self.lineEdit_Email.setClearButtonEnabled(False)
        self.lineEdit_Email.setObjectName("lineEdit_Email")

        self.lineEdit_Pass = QtWidgets.QLineEdit(parent=self.widget_Login)
        self.lineEdit_Pass.setGeometry(QtCore.QRect(130, 360, 220, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.lineEdit_Pass.setFont(font)
        self.lineEdit_Pass.setStyleSheet(
            "QLineEdit {\n"
            "    border: 2px solid rgba(255, 223, 186, 150); /* Golden border */\n"
            "    border-radius: 10px;\n"
            "    padding: 5px;\n"
            "    background: rgba(255, 255, 255, 230); /* Slight transparency */\n"
            "}"
        )
        self.lineEdit_Pass.setObjectName("lineEdit_Pass")
        self.lineEdit_Pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButton_Login = QtWidgets.QPushButton(parent=self.widget_Login)
        self.pushButton_Login.setGeometry(QtCore.QRect(130, 420, 100, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setStyleSheet("border-radius: 10px;\n" "")
        self.pushButton_Login.setObjectName("pushButton_Login")

        self.label_Forgot = QtWidgets.QLabel(parent=self.widget_Login)
        self.label_Forgot.setGeometry(QtCore.QRect(140, 460, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Forgot.setFont(font)
        self.label_Forgot.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_Forgot.setObjectName("label_Forgot")

        self.layoutWidget = QtWidgets.QWidget(parent=self.widget_Login)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 500, 140, 31))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_SM1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_SM1.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_SM1.setFont(font)
        self.pushButton_SM1.setObjectName("pushButton_SM1")
        self.horizontalLayout.addWidget(self.pushButton_SM1)

        self.pushButton_SM2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_SM2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_SM2.setFont(font)
        self.pushButton_SM2.setObjectName("pushButton_SM2")
        self.horizontalLayout.addWidget(self.pushButton_SM2)

        self.pushButton_SM3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_SM3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_SM3.setFont(font)
        self.pushButton_SM3.setObjectName("pushButton_SM3")
        self.horizontalLayout.addWidget(self.pushButton_SM3)

        self.pushButton_SM4 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_SM4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_SM4.setFont(font)
        self.pushButton_SM4.setObjectName("pushButton_SM4")
        self.horizontalLayout.addWidget(self.pushButton_SM4)

        self.layoutWidget1 = QtWidgets.QWidget(parent=self.widget_Login)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 20, 51, 511))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_PlanetsLeft = QtWidgets.QVBoxLayout(self.layoutWidget1)

        self.verticalLayout_PlanetsLeft.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_PlanetsLeft.setObjectName("verticalLayout_PlanetsLeft")
        self.label_P1 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_P1.setMaximumSize(QtCore.QSize(50, 50))
        self.label_P1.setStyleSheet("background-image: url(:/Image/Planet1.png);")
        self.label_P1.setText("")
        self.label_P1.setObjectName("label_P1")
        self.verticalLayout_PlanetsLeft.addWidget(self.label_P1)
        self.label_P2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_P2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_P2.setStyleSheet("background-image: url(:/Image/Planet2.png);")
        self.label_P2.setText("")
        self.label_P2.setObjectName("label_P2")
        self.verticalLayout_PlanetsLeft.addWidget(self.label_P2)
        self.label_P5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_P5.setMaximumSize(QtCore.QSize(45, 45))
        self.label_P5.setStyleSheet("background-image: url(:/Image/Planet5.png);")
        self.label_P5.setText("")
        self.label_P5.setObjectName("label_P5")
        self.verticalLayout_PlanetsLeft.addWidget(self.label_P5)
        self.label_P7 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_P7.setMinimumSize(QtCore.QSize(40, 39))
        self.label_P7.setMaximumSize(QtCore.QSize(40, 39))
        self.label_P7.setStyleSheet("background-image: url(:/Image/Planet7.png);")
        self.label_P7.setText("")
        self.label_P7.setObjectName("label_P7")
        self.verticalLayout_PlanetsLeft.addWidget(self.label_P7)
        self.label_P9 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_P9.setMinimumSize(QtCore.QSize(30, 30))
        self.label_P9.setMaximumSize(QtCore.QSize(30, 30))
        self.label_P9.setStyleSheet("background-image: url(:/Image/Planet9.png);")
        self.label_P9.setText("")
        self.label_P9.setObjectName("label_P9")
        self.verticalLayout_PlanetsLeft.addWidget(self.label_P9)

        self.layoutWidget2 = QtWidgets.QWidget(parent=self.widget_Login)
        self.layoutWidget2.setGeometry(QtCore.QRect(370, 20, 51, 511))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_PlanetsRight = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_PlanetsRight.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_PlanetsRight.setObjectName("verticalLayout_PlanetsRight")
        self.label_P3 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_P3.setMaximumSize(QtCore.QSize(50, 50))
        self.label_P3.setStyleSheet("background-image: url(:/Image/Planet4.png);")
        self.label_P3.setText("")
        self.label_P3.setObjectName("label_P3")
        self.verticalLayout_PlanetsRight.addWidget(self.label_P3)
        self.label_P4 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_P4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_P4.setStyleSheet("background-image: url(:/Image/Planet3.png);")
        self.label_P4.setText("")
        self.label_P4.setObjectName("label_P4")
        self.verticalLayout_PlanetsRight.addWidget(self.label_P4)
        self.label_P6 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_P6.setMaximumSize(QtCore.QSize(45, 45))
        self.label_P6.setStyleSheet("background-image: url(:/Image/Planet6.png);")
        self.label_P6.setText("")
        self.label_P6.setObjectName("label_P6")
        self.verticalLayout_PlanetsRight.addWidget(self.label_P6)
        self.label_P8 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_P8.setMinimumSize(QtCore.QSize(40, 39))
        self.label_P8.setMaximumSize(QtCore.QSize(40, 39))
        self.label_P8.setStyleSheet("background-image: url(:/Image/Planet8.png);")
        self.label_P8.setText("")
        self.label_P8.setObjectName("label_P8")
        self.verticalLayout_PlanetsRight.addWidget(self.label_P8)
        self.label_P10 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_P10.setMinimumSize(QtCore.QSize(28, 30))
        self.label_P10.setMaximumSize(QtCore.QSize(30, 30))
        self.label_P10.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_P10.setStyleSheet("background-image: url(:/Image/Planet10.png);")
        self.label_P10.setText("")
        self.label_P10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_P10.setObjectName("label_P10")
        self.verticalLayout_PlanetsRight.addWidget(self.label_P10)

        self.layoutWidget3 = QtWidgets.QWidget(parent=self.widget_Login)
        self.layoutWidget3.setGeometry(QtCore.QRect(80, 570, 311, 311))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")

        self.label_Disp1 = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_Disp1.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "background-image: url(:/Image/Display1.jpg);\n"
            "border-radius: 7px;"
        )
        self.label_Disp1.setText("")
        self.label_Disp1.setObjectName("label_Disp1")
        self.gridLayout.addWidget(self.label_Disp1, 0, 0, 1, 1)

        self.label_Disp3 = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_Disp3.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "background-image: url(:/Image/Display3.jpg);\n"
            "border-radius: 7px;"
        )
        self.label_Disp3.setText("")
        self.label_Disp3.setObjectName("label_Disp3")
        self.gridLayout.addWidget(self.label_Disp3, 0, 1, 1, 1)

        self.label_Disp4 = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_Disp4.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "background-image: url(:/Image/Display5.jpg);\n"
            "border-radius: 7px;"
        )
        self.label_Disp4.setText("")
        self.label_Disp4.setObjectName("label_Disp4")
        self.gridLayout.addWidget(self.label_Disp4, 0, 2, 1, 1)

        self.label_Disp2 = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_Disp2.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "background-image: url(:/Image/Display2.jpg);\n"
            "border-radius: 7px;"
        )
        self.label_Disp2.setText("")
        self.label_Disp2.setObjectName("label_Disp2")
        self.gridLayout.addWidget(self.label_Disp2, 1, 0, 1, 1)

        self.label_Disp5 = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_Disp5.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "background-image: url(:/Image/Display4.jpg);\n"
            "border-radius: 7px;"
        )
        self.label_Disp5.setText("")
        self.label_Disp5.setObjectName("label_Disp5")
        self.gridLayout.addWidget(self.label_Disp5, 1, 1, 1, 1)

        self.label_Disp6 = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_Disp6.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "background-image: url(:/Image/Display6.jpg);\n"
            "border-radius: 7px;"
        )
        self.label_Disp6.setText("")
        self.label_Disp6.setObjectName("label_Disp6")
        self.gridLayout.addWidget(self.label_Disp6, 1, 2, 1, 1)

        self.pushButton_Signup = QtWidgets.QPushButton(parent=self.widget_Login)
        self.pushButton_Signup.setGeometry(QtCore.QRect(240, 420, 100, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Signup.setFont(font)
        self.pushButton_Signup.setStyleSheet("border-radius: 10px;\n" "")
        self.pushButton_Signup.setObjectName("pushButton_Signup")

        self.frame_Signup = QtWidgets.QFrame(parent=self.widget_Login)
        self.frame_Signup.setGeometry(QtCore.QRect(45, 187, 384, 541))
        self.frame_Signup.setStyleSheet(
            "QFrame {\n"
            "border-radius: 20px;\n"
            "background-color: rgb(250, 250, 250);\n"
            "border: 1px solid #D4AF37;\n"
            "}\n"
            "QLineEdit {\n"
            "border-radius: 3px;\n"
            "background-color: rgb(225, 225, 225);\n"
            "}\n"
            "QComboBox {\n"
            "border: 1px solid  rgb(225, 225, 225);\n"
            "border-radius: 3px;\n"
            "background-color: rgb(255, 255, 255);\n"
            "}\n"
            "QRadioButton {\n"
            "border: 1px solid  rgb(225, 225, 225);\n"
            "border-radius: 3px;\n"
            "background-color: rgb(255, 255, 255);\n"
            "}\n"
            "QLabel {\n"
            "border: none;\n"
            "}\n"
            "QPushButton {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, \n"
            "        stop:0 rgba(58, 32, 85, 219), \n"
            "        stop:1 rgba(207, 159, 36, 226));\n"
            "    color:rgba(255, 223, 186, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, \n"
            "        stop:0 rgba(80, 50, 130, 255), \n"
            "        stop:1 rgba(255, 200, 50, 255));\n"
            "    color: rgba(255, 255, 255, 255);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(150, 130, 20, 200);\n"
            "}\n"
            ""
        )
        self.frame_Signup.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Signup.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Signup.setObjectName("frame_Signup")
        
        self.frame_Signup.setVisible(False)

        self.label_Line = QtWidgets.QLabel(parent=self.frame_Signup)
        self.label_Line.setGeometry(QtCore.QRect(10, 80, 371, 20))
        self.label_Line.setObjectName("label_Line")

        self.lineEdit_First = QtWidgets.QLineEdit(parent=self.frame_Signup)
        self.lineEdit_First.setGeometry(QtCore.QRect(10, 140, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_First.setFont(font)
        self.lineEdit_First.setObjectName("lineEdit_First")

        self.lineEdit_Last = QtWidgets.QLineEdit(parent=self.frame_Signup)
        self.lineEdit_Last.setGeometry(QtCore.QRect(195, 140, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Last.setFont(font)
        self.lineEdit_Last.setObjectName("lineEdit_Last")

        self.lineEdit_SU_Email = QtWidgets.QLineEdit(parent=self.frame_Signup)
        self.lineEdit_SU_Email.setGeometry(QtCore.QRect(10, 180, 365, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SU_Email.setFont(font)
        self.lineEdit_SU_Email.setObjectName("lineEdit_SU_Email")

        self.lineEdit_SU_Pass = QtWidgets.QLineEdit(parent=self.frame_Signup)
        self.lineEdit_SU_Pass.setGeometry(QtCore.QRect(10, 220, 365, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SU_Pass.setFont(font)
        self.lineEdit_SU_Pass.setObjectName("lineEdit_SU_Pass")
        self.lineEdit_SU_Pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.label_Warning = QtWidgets.QLabel(parent=self.frame_Signup)
        self.label_Warning.setGeometry(QtCore.QRect(10, 100, 365, 31))
        self.label_Warning.setStyleSheet(
            "border: 2px solid rgb(220, 53, 69);\n"
            "border-radius: 3px;\n"
            "color: rgb(220, 53, 69);"
        )
        self.label_Warning.setText("")
        self.label_Warning.setObjectName("label_Warning")
        self.label_Warning.setVisible(False)

        self.lineEdit_SU_Pass_Conf = QtWidgets.QLineEdit(parent=self.frame_Signup)
        self.lineEdit_SU_Pass_Conf.setGeometry(QtCore.QRect(10, 260, 365, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SU_Pass_Conf.setFont(font)
        self.lineEdit_SU_Pass_Conf.setObjectName("lineEdit_SU_Pass_Conf")
        self.lineEdit_SU_Pass_Conf.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.comboBox_Month = QtWidgets.QComboBox(parent=self.frame_Signup)
        self.comboBox_Month.setGeometry(QtCore.QRect(10, 330, 118, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Month.setFont(font)
        self.comboBox_Month.setObjectName("comboBox_Month")

        self.pushButton_SU_Exit = QtWidgets.QPushButton(parent=self.frame_Signup)
        self.pushButton_SU_Exit.setGeometry(QtCore.QRect(340, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_SU_Exit.setFont(font)
        self.pushButton_SU_Exit.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    border-radius: 10px;\n"
            "    background-color: transparent;\n"
            "    color: rgb(0, 0, 0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(212, 175, 55, 0.2);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(212, 175, 55, 0.4);\n"
            "    padding-left: 3px;\n"
            "    padding-top: 3px;\n"
            "}"
        )
        self.pushButton_SU_Exit.setObjectName("pushButton_SU_Exit")

        self.label_Birthday = QtWidgets.QLabel(parent=self.frame_Signup)
        self.label_Birthday.setGeometry(QtCore.QRect(10, 310, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Birthday.setFont(font)
        self.label_Birthday.setObjectName("label_Birthday")

        self.comboBox_Day = QtWidgets.QComboBox(parent=self.frame_Signup)
        self.comboBox_Day.setGeometry(QtCore.QRect(133, 330, 118, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Day.setFont(font)
        self.comboBox_Day.setObjectName("comboBox_Day")

        self.comboBox_Year = QtWidgets.QComboBox(parent=self.frame_Signup)
        self.comboBox_Year.setGeometry(QtCore.QRect(256, 330, 118, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Year.setFont(font)
        self.comboBox_Year.setObjectName("comboBox_Year")

        self.label_Birthday_2 = QtWidgets.QLabel(parent=self.frame_Signup)
        self.label_Birthday_2.setGeometry(QtCore.QRect(10, 380, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Birthday_2.setFont(font)
        self.label_Birthday_2.setObjectName("label_Birthday_2")

        self.radioButton_Female = QtWidgets.QRadioButton(parent=self.frame_Signup)
        self.radioButton_Female.setGeometry(QtCore.QRect(10, 400, 118, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_Female.setFont(font)
        self.radioButton_Female.setLayoutDirection(
            QtCore.Qt.LayoutDirection.RightToLeft
        )
        self.radioButton_Female.setStyleSheet(
            "QRadioButton {\n" "text-align: left;\n" "}"
        )
        self.radioButton_Female.setObjectName("radioButton_Female")
        self.buttonGroup = QtWidgets.QButtonGroup(Form_Login)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_Female)

        self.radioButton_Male = QtWidgets.QRadioButton(parent=self.frame_Signup)
        self.radioButton_Male.setGeometry(QtCore.QRect(133, 400, 118, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_Male.setFont(font)
        self.radioButton_Male.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_Male.setStyleSheet(
            "QRadioButton {\n" "text-align: left;\n" "}"
        )
        self.radioButton_Male.setObjectName("radioButton_Male")
        self.buttonGroup.addButton(self.radioButton_Male)

        self.radioButton_Custom = QtWidgets.QRadioButton(parent=self.frame_Signup)
        self.radioButton_Custom.setGeometry(QtCore.QRect(256, 400, 118, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_Custom.setFont(font)
        self.radioButton_Custom.setLayoutDirection(
            QtCore.Qt.LayoutDirection.RightToLeft
        )
        self.radioButton_Custom.setStyleSheet(
            "QRadioButton {\n" "text-align: left;\n" "}"
        )
        self.radioButton_Custom.setObjectName("radioButton_Custom")
        self.buttonGroup.addButton(self.radioButton_Custom)

        self.label_Disclaimer = QtWidgets.QLabel(parent=self.frame_Signup)
        self.label_Disclaimer.setGeometry(QtCore.QRect(10, 450, 365, 21))
        self.label_Disclaimer.setObjectName("label_Disclaimer")

        self.pushButton_SU_Signup = QtWidgets.QPushButton(parent=self.frame_Signup)
        self.pushButton_SU_Signup.setGeometry(QtCore.QRect(103, 490, 177, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_SU_Signup.setFont(font)
        self.pushButton_SU_Signup.setObjectName("pushButton_SU_Signup")

        self.widget = QtWidgets.QWidget(parent=self.frame_Signup)
        self.widget.setGeometry(QtCore.QRect(20, 10, 134, 72))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header1 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_Header1.setFont(font)
        self.label_Header1.setStyleSheet("border: none;")
        self.label_Header1.setObjectName("label_Header1")
        self.verticalLayout.addWidget(self.label_Header1)
        self.label_Header2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Header2.setFont(font)
        self.label_Header2.setStyleSheet("border: none;")
        self.label_Header2.setObjectName("label_Header2")
        self.verticalLayout.addWidget(self.label_Header2)
        self.label_MainWarning = QtWidgets.QLabel(parent=self.widget_Login)
        self.label_MainWarning.setGeometry(QtCore.QRect(130, 250, 220, 41))
        self.label_MainWarning.setStyleSheet(
            "    border: 2px solid rgb(220, 53, 69); \n"
            "    border-radius: 10px;\n"
            "    padding: 5px;\n"
            "    background: rgba(255, 255, 255, 230); /* Slight transparency */\n"
            "    color: rgb(220, 53, 69);"
        )
        self.label_MainWarning.setText("")
        self.label_MainWarning.setObjectName("label_MainWarning")
        self.label_MainWarning.setVisible(False)

        self.label_Spacebg.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(255, 223, 186)
            )
        )
        self.pushButton_Login.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(255, 223, 186)
            )
        )
        self.pushButton_Signup.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(255, 223, 186)
            )
        )
        self.comboBox_Month.addItems(
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]
        )
        self.comboBox_Day.addItems(str(i) for i in range(1, 32))
        self.comboBox_Year.addItems(str(i) for i in range(1908, 2012))
        
        self.frame_Signup.raise_()
        
        self.retranslateUi(Form_Login)
        QtCore.QMetaObject.connectSlotsByName(Form_Login)

        

    def retranslateUi(self, Form_Login: QtWidgets.QWidget) -> None:
        """Sets the text and placeholder content for all widgets in the login form.

        This function is responsible for updating the UI with translated text for
        all widgets (labels, buttons, placeholders) within the login form.
        It uses the Qt translation system to ensure that text is localized as needed.

        Args:
            Form_Login (QtWidgets.QWidget): The widget that contains the UI elements to be translated.
        """
        _translate = QtCore.QCoreApplication.translate
        Form_Login.setWindowTitle(_translate("Form_Login", "Form"))
        self.lineEdit_Email.setPlaceholderText(
            _translate("Form_Login", "Email Address")
        )
        self.lineEdit_Pass.setPlaceholderText(_translate("Form_Login", " Password"))
        self.pushButton_Login.setText(_translate("Form_Login", "LOGIN"))
        self.label_Forgot.setText(
            _translate("Form_Login", "Forgot your User Name or Password?")
        )
        self.pushButton_SM1.setText(_translate("Form_Login", "E"))
        self.pushButton_SM2.setText(_translate("Form_Login", "D"))
        self.pushButton_SM3.setText(_translate("Form_Login", "C"))
        self.pushButton_SM4.setText(_translate("Form_Login", "M"))
        self.pushButton_Signup.setText(_translate("Form_Login", "SIGN UP"))
        self.label_Line.setText(
            _translate(
                "Form_Login",
                "-------------------------------------------------------------------------------------------",
            )
        )
        self.lineEdit_First.setPlaceholderText(_translate("Form_Login", "First name"))
        self.lineEdit_Last.setPlaceholderText(_translate("Form_Login", "Last name"))
        self.lineEdit_SU_Email.setPlaceholderText(
            _translate("Form_Login", "Email Address")
        )
        self.lineEdit_SU_Pass.setPlaceholderText(_translate("Form_Login", "Password"))
        self.lineEdit_SU_Pass_Conf.setPlaceholderText(
            _translate("Form_Login", "Confirm Password")
        )
        self.pushButton_SU_Exit.setText(_translate("Form_Login", ""))
        self.label_Birthday.setText(_translate("Form_Login", "Birthday"))
        self.label_Birthday_2.setText(_translate("Form_Login", "Gender"))
        self.radioButton_Female.setText(_translate("Form_Login", "Female            "))
        self.radioButton_Male.setText(_translate("Form_Login", "Male                "))
        self.radioButton_Custom.setText(_translate("Form_Login", "Custom            "))
        self.label_Disclaimer.setText(
            _translate("Form_Login", "By clicking Sign Up, you agree to our Terms.")
        )
        self.pushButton_SU_Signup.setText(_translate("Form_Login", "Sign Up"))
        self.label_Header1.setText(_translate("Form_Login", "Sign Up"))
        self.label_Header2.setText(_translate("Form_Login", "It's quick and easy."))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Sets up the main window layout and UI elements for the application.

        This function configures the layout of the main window, including
        the header, left menu, body, footer, and various UI components such as
        buttons and labels. It also sets up the appearance and behavior of
        each element (e.g., stylesheets, geometry, and fonts).

        Args:
            MainWindow (QtWidgets.QMainWindow): The main window widget where UI elements will be placed.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1335, 799)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setMouseTracking(True)
        self.is_dragging = False
        self.drag_start_position = QtCore.QPoint(0, 0)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.main_body = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_body.setGeometry(QtCore.QRect(0, 0, 1235, 724))
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_body.setObjectName("main_body")
        self.frame_Header = QtWidgets.QFrame(parent=self.main_body)
        self.frame_Header.setGeometry(QtCore.QRect(0, 0, 1235, 51))
        self.frame_Header.setStyleSheet(
            "QFrame {\n"
            "    background-color: rgb(45, 45, 45);\n"
            "    border-bottom: 1px solid #D4AF37;\n"
            "\n"
            "}\n"
            "QPushButton {\n"
            "    border: none;\n"
            "    border-radius: 10px;\n"
            "    background-color: transparent;\n"
            "    color: rgb(200, 200, 200);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(212, 175, 55, 0.2);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(212, 175, 55, 0.4);\n"
            "    padding-left: 3px;\n"
            "    padding-top: 3px;\n"
            "}"
        )
        self.frame_Header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Header.setObjectName("frame_Header")

        self.pushButton_Minimize = QtWidgets.QPushButton(parent=self.frame_Header)
        self.pushButton_Minimize.setGeometry(QtCore.QRect(1120, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_Minimize.setFont(font)
        self.pushButton_Minimize.setStyleSheet("")
        self.pushButton_Minimize.setObjectName("pushButton_Minimize")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=self.frame_Header)
        self.pushButton_Exit.setGeometry(QtCore.QRect(1200, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setStyleSheet("")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Maximize = QtWidgets.QPushButton(parent=self.frame_Header)
        self.pushButton_Maximize.setGeometry(QtCore.QRect(1160, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_Maximize.setFont(font)
        self.pushButton_Maximize.setStyleSheet("")
        self.pushButton_Maximize.setObjectName("pushButton_Maximize")
        self.pushButton_Maximize.setVisible(False)

        self.pushButton_Menu = QtWidgets.QPushButton(parent=self.frame_Header)
        self.pushButton_Menu.setGeometry(QtCore.QRect(0, 0, 41, 51))
        self.pushButton_Menu.setMinimumSize(QtCore.QSize(41, 0))
        self.pushButton_Menu.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_Menu.setFont(font)
        self.pushButton_Menu.setStyleSheet("")
        self.pushButton_Menu.setObjectName("pushButton_Menu")
        self.frame_Top_ToolBar = QtWidgets.QFrame(parent=self.frame_Header)
        self.frame_Top_ToolBar.setGeometry(QtCore.QRect(370, 0, 451, 51))
        self.frame_Top_ToolBar.setStyleSheet(
            "QFrame {\n"
            "    \n"
            "    background-image: url(:/Image/GALACTIC READS (450 x 100 px).png);\n"
            "    background-color: transparent;\n"
            "    background-repeat: none;\n"
            "background-position: center;\n"
            "}"
        )
        self.frame_Top_ToolBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Top_ToolBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Top_ToolBar.setObjectName("frame_Top_ToolBar")

        self.frame_Menu_Left = QtWidgets.QFrame(parent=self.main_body)
        self.frame_Menu_Left.setGeometry(QtCore.QRect(0, 50, 41, 641))
        self.frame_Menu_Left.setMinimumSize(QtCore.QSize(41, 0))
        self.frame_Menu_Left.setMaximumSize(QtCore.QSize(125, 16777215))
        self.frame_Menu_Left.setStyleSheet(
            "QFrame {\n"
            "    background-color: rgba(45, 45, 45, 150);\n"
            "    border-right: 1px solid #D4AF37;\n"
            "}"
        )
        self.frame_Menu_Left.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Menu_Left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Menu_Left.setObjectName("frame_Menu_Left")
        self.frame_Menu_Left.setMinimumWidth(41)
        self.frame_Menu_Left.setMaximumWidth(131)

        self.frame_Left_Menu_Top_Buttons = QtWidgets.QFrame(parent=self.frame_Menu_Left)
        self.frame_Left_Menu_Top_Buttons.setGeometry(QtCore.QRect(0, 0, 131, 641))
        self.frame_Left_Menu_Top_Buttons.setStyleSheet(
            "\n"
            "QPushButton {\n"
            "    padding: 20px 10px;\n"
            "    border: none;\n"
            "    border-radius: 10px;\n"
            "    background-color: transparent;\n"
            "    color: rgb(200, 200, 200);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(212, 175, 55, 0.2);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(212, 175, 55, 0.4);\n"
            "    padding-left: 3px;\n"
            "    padding-top: 3px;\n"
            "}"
        )
        self.frame_Left_Menu_Top_Buttons.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.frame_Left_Menu_Top_Buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Left_Menu_Top_Buttons.setObjectName("frame_Left_Menu_Top_Buttons")
        self.widget = QtWidgets.QWidget(parent=self.frame_Left_Menu_Top_Buttons)
        self.widget.setGeometry(QtCore.QRect(0, 0, 137, 651))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(7, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_Home = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_Home.setMinimumSize(QtCore.QSize(129, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Home.setFont(font)
        self.pushButton_Home.setStyleSheet(
            "background-image: url(:/Image/Home.png);\n"
            "background-repeat: none;\n"
            "padding-left: 30px;\n"
            "background-position: center left;"
        )
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButton_Home
        )
        self.pushButton_Account = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_Account.setMinimumSize(QtCore.QSize(129, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Account.setFont(font)
        self.pushButton_Account.setStyleSheet(
            "background-image: url(:/Image/Avatar.png);\n"
            "background-repeat: none;\n"
            "padding-left: 40px;\n"
            "background-position: center left;"
        )
        self.pushButton_Account.setObjectName("pushButton_Account")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButton_Account
        )
        self.pushButton_Settings = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_Settings.setMinimumSize(QtCore.QSize(129, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Settings.setFont(font)
        self.pushButton_Settings.setStyleSheet(
            "background-image: url(:/Image/Setting.png);\n"
            "background-repeat: none;\n"
            "padding-left: 40px;\n"
            "\n"
            "background-position: center left;"
        )
        self.pushButton_Settings.setObjectName("pushButton_Settings")
        self.pushButton_Settings.setVisible(False)
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pushButton_Settings
        )
        spacerItem = QtWidgets.QSpacerItem(
            10,
            480,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        self.frame_Footer = QtWidgets.QFrame(parent=self.main_body)
        self.frame_Footer.setGeometry(QtCore.QRect(0, 689, 1235, 32))
        self.frame_Footer.setStyleSheet(
            "QFrame {\n"
            "    background-color: rgba(0, 0, 0, 0.7);\n"
            "    border-top: 1px solid #D4AF37;\n"
            "    color: rgba(255, 255, 255, 0.7);\n"
            "    padding: 10px 20px;\n"
            "}\n"
            "QPushButton {\n"
            "    color: rgba(255, 255, 255, 0.7);\n"
            "    text-decoration: none;\n"
            "    background-color: rgba(0, 0, 0, 0.7);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    color: rgba(255, 255, 255, 1);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    color: rgba(212, 175, 55, 0.4);\n"
            "}\n"
            ""
        )
        self.frame_Footer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Footer.setObjectName("frame_Footer")
        self.label_Footer_Text_Left = QtWidgets.QLabel(parent=self.frame_Footer)
        self.label_Footer_Text_Left.setGeometry(QtCore.QRect(0, 1, 411, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_Footer_Text_Left.setFont(font)
        self.label_Footer_Text_Left.setStyleSheet("border: none;")
        self.label_Footer_Text_Left.setObjectName("label_Footer_Text_Left")
        self.label_Footer_Text_Center = QtWidgets.QLabel(parent=self.frame_Footer)
        self.label_Footer_Text_Center.setGeometry(QtCore.QRect(410, 1, 411, 32))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.label_Footer_Text_Center.setFont(font)
        self.label_Footer_Text_Center.setStyleSheet("border: none;")
        self.label_Footer_Text_Center.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Footer_Text_Center.setObjectName("label_Footer_Text_Center")
        self.widget1 = QtWidgets.QWidget(parent=self.frame_Footer)
        self.widget1.setGeometry(QtCore.QRect(820, 0, 411, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Help = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_Help.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Help.setObjectName("pushButton_Help")
        self.horizontalLayout.addWidget(self.pushButton_Help)
        self.pushButton_Terms = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_Terms.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Terms.setObjectName("pushButton_Terms")
        self.horizontalLayout.addWidget(self.pushButton_Terms)
        self.pushButton_Privacy = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_Privacy.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Privacy.setObjectName("pushButton_Privacy")
        self.horizontalLayout.addWidget(self.pushButton_Privacy)

        self.frame_Center_Main = QtWidgets.QFrame(parent=self.main_body)
        self.frame_Center_Main.setGeometry(QtCore.QRect(40, 50, 1194, 641))
        self.frame_Center_Main.setStyleSheet(
            "QFrame {\n" "background-color: rgba(0, 0, 0, 0);\n" "}\n"
        )
        self.frame_Center_Main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Center_Main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Center_Main.setObjectName("frame_Center_Main")

        self.frame_Logo = QtWidgets.QFrame(parent=self.frame_Center_Main)
        self.frame_Logo.setGeometry(QtCore.QRect(1, 1, 1194, 0))
        self.frame_Logo.setStyleSheet(
            "QFrame {\n"
            "   background-color: rgb(45, 45, 45);\n"
            "   border-bottom: 1px solid #D4AF37;\n"
            "}\n"
            "QPushButton {\n"
            "   background-color: Transparent;\n"
            "   background-repeat: no-repeat;\n"
            "   background-position: center;\n"
            "   border-right: 1px solid #D4AF37;\n"
            "   padding: 0px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgba(255, 255, 255, 30%);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "   background-color: rgba(255, 255, 255, 50%);\n"
            "}\n"
            "QPushButton:focus {\n"
            "   outline: none;\n"
            "}"
        )
        self.frame_Logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Logo.setObjectName("frame_Logo")

        self.pushButton_Logo1 = QtWidgets.QPushButton(parent=self.frame_Logo)
        self.pushButton_Logo1.setGeometry(QtCore.QRect(0, 0, 298, 61))
        self.pushButton_Logo1.setStyleSheet(
            "background-image: url(:/Image/SWLogo.png);\n"
        )
        self.pushButton_Logo1.setText("")
        self.pushButton_Logo1.setObjectName("pushButton_Logo1")

        self.pushButton_Logo2 = QtWidgets.QPushButton(parent=self.frame_Logo)
        self.pushButton_Logo2.setGeometry(QtCore.QRect(300, 0, 298, 61))
        self.pushButton_Logo2.setStyleSheet(
            "QPushButton {\n"
            "   background-image: url(:/Image/DWLogo.png);\n"
            "   background-color: rgba(200, 200, 200, 50%);\n"
            "   color: rgba(100, 100, 100, 100%);\n"
            "}\n"
            "QPushButton:disabled {\n"
            "    background-color: rgba(150, 150, 150, 50%);\n"
            "    color: rgba(150, 150, 150, 100%);\n"
            "    border: 1px solid rgba(100, 100, 100, 100%);\n"
            "}\n"
        )
        self.pushButton_Logo2.setText("")
        self.pushButton_Logo2.setObjectName("pushButton_Logo2")
        self.pushButton_Logo2.setEnabled(True)
        self.pushButton_Logo2.setToolTip("This feature is not available yet.")

        self.pushButton_Logo3 = QtWidgets.QPushButton(parent=self.frame_Logo)
        self.pushButton_Logo3.setGeometry(QtCore.QRect(600, 0, 298, 61))
        self.pushButton_Logo3.setStyleSheet(
            "QPushButton {\n"
            "   background-image: url(:/Image/STLogo.png);\n"
            "   background-color: rgba(200, 200, 200, 50%);\n"
            "   color: rgba(100, 100, 100, 100%);\n"
            "}\n"
            "QPushButton:disabled {\n"
            "    background-color: rgba(150, 150, 150, 50%);\n"
            "    color: rgba(150, 150, 150, 100%);\n"
            "    border: 1px solid rgba(100, 100, 100, 100%);\n"
            "}\n"
        )
        self.pushButton_Logo3.setText("")
        self.pushButton_Logo3.setObjectName("pushButton_Logo3")
        self.pushButton_Logo3.setEnabled(True)
        self.pushButton_Logo3.setToolTip("This feature is not available yet.")

        self.pushButton_Logo4 = QtWidgets.QPushButton(parent=self.frame_Logo)
        self.pushButton_Logo4.setGeometry(QtCore.QRect(900, 0, 298, 61))
        self.pushButton_Logo4.setStyleSheet(
            "QPushButton {\n"
            "   background-image: url(:/Image/WHLogo.png);\n"
            "   background-color: rgba(200, 200, 200, 50%);\n"
            "   color: rgba(100, 100, 100, 100%);\n"
            "}\n"
            "QPushButton:disabled {\n"
            "    background-color: rgba(150, 150, 150, 50%);\n"
            "    color: rgba(150, 150, 150, 100%);\n"
            "    border: 1px solid rgba(100, 100, 100, 100%);\n"
            "}\n"
        )
        self.pushButton_Logo4.setText("")
        self.pushButton_Logo4.setObjectName("pushButton_Logo4")
        self.pushButton_Logo4.setEnabled(True)
        self.pushButton_Logo4.setToolTip("This feature is not available yet.")

        self.frame_SW_Filter_Menu = QtWidgets.QFrame(parent=self.frame_Center_Main)
        self.frame_SW_Filter_Menu.setGeometry(QtCore.QRect(961, 2, 0, 639))
        self.frame_SW_Filter_Menu.setStyleSheet(
            "QFrame {\n"
            "    background-color: rgb(45, 45, 45);\n"
            "    border-left: 1px solid #D4AF37;\n"
            "}\n"
            "QLabel {\n"
            "    color: rgba(255, 255, 255, 0.7);\n"
            "    border: none;\n"
            "}\n"
            "QCheckBox {\n"
            "    color: rgba(255, 255, 255, 0.7);\n"
            "    border: none;\n"
            "}"
        )
        self.frame_SW_Filter_Menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_SW_Filter_Menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_SW_Filter_Menu.setObjectName("frame_SW_Filter_Menu")

        self.label_Filter = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Filter.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Filter.setFont(font)
        self.label_Filter.setObjectName("label_Filter")
        self.label_Line1 = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Line1.setGeometry(QtCore.QRect(7, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Line1.setFont(font)
        self.label_Line1.setObjectName("label_Line1")
        self.label_Universe = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Universe.setGeometry(QtCore.QRect(80, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_Universe.setFont(font)
        self.label_Universe.setObjectName("label_Universe")
        self.label_Line2 = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Line2.setGeometry(QtCore.QRect(7, 130, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Line2.setFont(font)
        self.label_Line2.setObjectName("label_Line2")
        self.label_Universe_2 = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Universe_2.setGeometry(QtCore.QRect(70, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_Universe_2.setFont(font)
        self.label_Universe_2.setObjectName("label_Universe_2")
        self.label_Line3 = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Line3.setGeometry(QtCore.QRect(7, 330, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Line3.setFont(font)
        self.label_Line3.setObjectName("label_Line3")
        self.label_Universe_3 = QtWidgets.QLabel(parent=self.frame_SW_Filter_Menu)
        self.label_Universe_3.setGeometry(QtCore.QRect(100, 350, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_Universe_3.setFont(font)
        self.label_Universe_3.setObjectName("label_Universe_3")

        self.pushButton_clear = QtWidgets.QPushButton(parent=self.frame_SW_Filter_Menu)
        self.pushButton_clear.setGeometry(QtCore.QRect(80, 590, 75, 23))
        self.pushButton_clear.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #D4AF37;\n"
            "    background-color: rgb(45, 45, 45);\n"
            "    color: rgb(200, 200, 200);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(212, 175, 55, 0.2);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(212, 175, 55, 0.4);\n"
            "    padding-left: 3px;\n"
            "    padding-top: 3px;\n"
            "}"
        )
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.widget2 = QtWidgets.QWidget(parent=self.frame_SW_Filter_Menu)
        self.widget2.setGeometry(QtCore.QRect(10, 70, 65, 53))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_Legends = QtWidgets.QCheckBox(parent=self.widget2)
        self.checkBox_Legends.setObjectName("checkBox_Legends")
        self.buttonGroup_Universe = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_Universe.setObjectName("buttonGroup_Universe")
        self.buttonGroup_Universe.addButton(self.checkBox_Legends)
        self.verticalLayout.addWidget(self.checkBox_Legends)
        self.checkBox_Canon = QtWidgets.QCheckBox(parent=self.widget2)
        self.checkBox_Canon.setObjectName("checkBox_Canon")
        self.buttonGroup_Universe.addButton(self.checkBox_Canon)
        self.verticalLayout.addWidget(self.checkBox_Canon)
        self.checkBox_Both = QtWidgets.QCheckBox(parent=self.widget2)
        self.checkBox_Both.setObjectName("checkBox_Both")
        self.buttonGroup_Universe.addButton(self.checkBox_Both)
        self.verticalLayout.addWidget(self.checkBox_Both)
        self.checkBox_Both.setVisible(False)

        self.widget3 = QtWidgets.QWidget(parent=self.frame_SW_Filter_Menu)
        self.widget3.setGeometry(QtCore.QRect(0, 180, 171, 148))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_ON = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_ON.setObjectName("checkBox_ON")
        self.buttonGroup_Novel = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_Novel.setObjectName("buttonGroup_Novel")
        self.buttonGroup_Novel.setExclusive(False)
        self.buttonGroup_Novel.addButton(self.checkBox_ON)
        self.verticalLayout_2.addWidget(self.checkBox_ON)
        self.checkBox_NA = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_NA.setObjectName("checkBox_NA")
        self.buttonGroup_Novel.addButton(self.checkBox_NA)
        self.verticalLayout_2.addWidget(self.checkBox_NA)
        self.checkBox_OJR = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_OJR.setObjectName("checkBox_OJR")
        self.buttonGroup_Novel.addButton(self.checkBox_OJR)
        self.verticalLayout_2.addWidget(self.checkBox_OJR)
        self.checkBox_JRA = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_JRA.setObjectName("checkBox_JRA")
        self.buttonGroup_Novel.addButton(self.checkBox_JRA)
        self.verticalLayout_2.addWidget(self.checkBox_JRA)
        self.checkBox_YR = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_YR.setObjectName("checkBox_YR")
        self.buttonGroup_Novel.addButton(self.checkBox_YR)
        self.verticalLayout_2.addWidget(self.checkBox_YR)
        self.checkBox_YA = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_YA.setObjectName("checkBox_YA")
        self.buttonGroup_Novel.addButton(self.checkBox_YA)
        self.verticalLayout_2.addWidget(self.checkBox_YA)
        self.checkBox_S = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_S.setObjectName("checkBox_S")
        self.buttonGroup_Novel.addButton(self.checkBox_S)
        self.verticalLayout_2.addWidget(self.checkBox_S)
        self.checkBox_GB = QtWidgets.QCheckBox(parent=self.widget3)
        self.checkBox_GB.setObjectName("checkBox_GB")
        self.buttonGroup_Novel.addButton(self.checkBox_GB)
        self.verticalLayout_2.addWidget(self.checkBox_GB)
        self.widget4 = QtWidgets.QWidget(parent=self.frame_SW_Filter_Menu)
        self.widget4.setGeometry(QtCore.QRect(0, 376, 228, 186))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_DOTJ = QtWidgets.QCheckBox(parent=self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_DOTJ.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_DOTJ.setSizePolicy(sizePolicy)
        self.checkBox_DOTJ.setMinimumSize(QtCore.QSize(181, 0))
        self.checkBox_DOTJ.setMaximumSize(QtCore.QSize(181, 16777215))
        self.checkBox_DOTJ.setObjectName("checkBox_DOTJ")
        self.buttonGroup_Era = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_Era.setObjectName("buttonGroup_Era")
        self.buttonGroup_Era.setExclusive(False)
        self.buttonGroup_Era.addButton(self.checkBox_DOTJ)
        self.verticalLayout_3.addWidget(self.checkBox_DOTJ)
        self.checkBox_TOR = QtWidgets.QCheckBox(parent=self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TOR.sizePolicy().hasHeightForWidth())
        self.checkBox_TOR.setSizePolicy(sizePolicy)
        self.checkBox_TOR.setMinimumSize(QtCore.QSize(221, 0))
        self.checkBox_TOR.setMaximumSize(QtCore.QSize(221, 16777215))
        self.checkBox_TOR.setObjectName("checkBox_TOR")
        self.buttonGroup_Era.addButton(self.checkBox_TOR)
        self.verticalLayout_3.addWidget(self.checkBox_TOR)
        self.checkBox_THR = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_THR.setObjectName("checkBox_THR")
        self.buttonGroup_Era.addButton(self.checkBox_THR)
        self.verticalLayout_3.addWidget(self.checkBox_THR)
        self.checkBox_FOTJ = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_FOTJ.setObjectName("checkBox_FOTJ")
        self.buttonGroup_Era.addButton(self.checkBox_FOTJ)
        self.verticalLayout_3.addWidget(self.checkBox_FOTJ)
        self.checkBox_NJO = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_NJO.setObjectName("checkBox_NJO")
        self.buttonGroup_Era.addButton(self.checkBox_NJO)
        self.verticalLayout_3.addWidget(self.checkBox_NJO)
        self.checkBox_ROTE = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_ROTE.setObjectName("checkBox_ROTE")
        self.buttonGroup_Era.addButton(self.checkBox_ROTE)
        self.verticalLayout_3.addWidget(self.checkBox_ROTE)
        self.checkBox_ROTFO = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_ROTFO.setObjectName("checkBox_ROTFO")
        self.buttonGroup_Era.addButton(self.checkBox_ROTFO)
        self.verticalLayout_3.addWidget(self.checkBox_ROTFO)
        self.checkBox_AOR = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_AOR.setObjectName("checkBox_AOR")
        self.buttonGroup_Era.addButton(self.checkBox_AOR)
        self.verticalLayout_3.addWidget(self.checkBox_AOR)
        self.checkBox_TNR = QtWidgets.QCheckBox(parent=self.widget4)
        self.checkBox_TNR.setObjectName("checkBox_TNR")
        self.buttonGroup_Era.addButton(self.checkBox_TNR)
        self.verticalLayout_3.addWidget(self.checkBox_TNR)

        self.pushButton_Top_Menu_Carrot = QtWidgets.QPushButton(
            parent=self.frame_Center_Main
        )
        self.pushButton_Top_Menu_Carrot.setGeometry(QtCore.QRect(582, 0, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_Top_Menu_Carrot.setFont(font)
        self.pushButton_Top_Menu_Carrot.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #D4AF37;\n"
            "    background-color: rgb(45, 45, 45);\n"
            "    color: rgb(200, 200, 200);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(212, 175, 55, 0.2);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(212, 175, 55, 0.4);\n"
            "    padding-left: 3px;\n"
            "    padding-top: 3px;\n"
            "}"
        )
        self.pushButton_Top_Menu_Carrot.setText("")
        self.pushButton_Top_Menu_Carrot.setObjectName("pushButton_Top_Menu_Carrot")

        self.tableView = QtWidgets.QTableView(parent=self.frame_Center_Main)
        self.tableView.setGeometry(QtCore.QRect(30, 30, 1051, 581))
        self.tableView.setStyleSheet(
            "QTableView {"
            "background-color: #1A1A1A;"
            "color: #F0F0F0;"
            "border: 1px solid black;"
            "}"
            "QTableView::item {"
            "padding: 5px;"
            "border-right: 1px solid rgba(212, 175, 55, 0.3);"
            "border-bottom: 1px solid rgba(212, 175, 55, 0.3);"
            "}"
            "QHeaderView::section {"
            "background-color: #D4AF37;"
            "color: white;"
            "border: 1px solid #D4AF37;"
            "font-weight: bold;"
            "}"
            "QTableView::item:selected {"
            "background-color: #D4AF37;"
            "}"
        )
        self.tableView.setObjectName("tableView")
        self.tableView.setVisible(False)

        self.pushButton_Side_Menu_Carrot = QtWidgets.QPushButton(
            parent=self.frame_Center_Main
        )
        self.pushButton_Side_Menu_Carrot.setGeometry(QtCore.QRect(1163, 300, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        self.pushButton_Side_Menu_Carrot.setFont(font)
        self.pushButton_Side_Menu_Carrot.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #D4AF37;\n"
            "    background-color: rgb(45, 45, 45);\n"
            "    color: rgb(200, 200, 200);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(212, 175, 55, 0.2);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(212, 175, 55, 0.4);\n"
            "    padding-left: 3px;\n"
            "    padding-top: 3px;\n"
            "}"
        )
        self.pushButton_Side_Menu_Carrot.setObjectName("pushButton_Side_Menu_Carrot")
        self.pushButton_Side_Menu_Carrot.setVisible(False)

        self.label_SpaceBg1 = QtWidgets.QLabel(parent=self.main_body)
        self.label_SpaceBg1.setGeometry(QtCore.QRect(-40, -50, 1335, 799))
        self.label_SpaceBg1.setStyleSheet(
            "QLabel#label_SpaceBg1 {\n"
            "background-image: url(:/Image/space2.png);\n"
            "border-radius: 20px;"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "QTextBrowser {\n"
            "background-color: rgba(216, 216, 216, 0);"
            "}\n"
        )
        self.label_SpaceBg1.setText("")
        self.label_SpaceBg1.setObjectName("label_SpaceBg1")
        self.label_SpaceBg2 = QtWidgets.QLabel(parent=self.main_body)
        self.label_SpaceBg2.setGeometry(QtCore.QRect(-40, -50, 1335, 799))
        self.label_SpaceBg2.setStyleSheet(
            "QLabel#label_SpaceBg2 {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
            "border-radius: 20px;"
            "}\n"
        )
        self.label_SpaceBg2.setText("")
        self.label_SpaceBg2.setObjectName("label_SpaceBg2")

        self.textBrowser = QtWidgets.QTextBrowser(parent=self.label_SpaceBg1)
        self.textBrowser.setGeometry(QtCore.QRect(90, 110, 1175, 621))
        self.textBrowser.setStyleSheet(
            "QTextBrowser {\n" "background-color: rgba(216, 216, 216, 0);" "}\n"
        )

        self.textBrowser.setObjectName("textBrowser")
        
        self.frame_profile = QtWidgets.QFrame(parent=self.frame_Center_Main)
        self.frame_profile.setGeometry(QtCore.QRect(0, 0, 0, 641))
        self.frame_profile.setStyleSheet("QFrame#frame_profile {\n"
"border: 1px solid #D4AF37;\n"
"background-color: rgb(45, 45, 45);\n"
"}")
        self.frame_profile.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_profile.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_profile.setObjectName("frame_profile")
        
        self.widget = QtWidgets.QWidget(parent=self.frame_profile)
        self.widget.setGeometry(QtCore.QRect(260, 50, 191, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.label_prof_last_name_header = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_last_name_header.setFont(font)
        self.label_prof_last_name_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_last_name_header.setObjectName("label_prof_last_name_header")
        self.verticalLayout_5.addWidget(self.label_prof_last_name_header)
        self.label_prof_last_name = QtWidgets.QLabel(parent=self.widget)
        self.label_prof_last_name.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.label_prof_last_name.setText("")
        self.label_prof_last_name.setObjectName("label_prof_last_name")
        self.verticalLayout_5.addWidget(self.label_prof_last_name)
        self.label_prof_last_name.raise_()
        self.label_prof_last_name_header.raise_()
        self.widget1 = QtWidgets.QWidget(parent=self.frame_profile)
        self.widget1.setGeometry(QtCore.QRect(50, 50, 191, 71))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_prof_first_name_header = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_first_name_header.setFont(font)
        self.label_prof_first_name_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_first_name_header.setObjectName("label_prof_first_name_header")
        self.verticalLayout_4.addWidget(self.label_prof_first_name_header)
        self.label_prof_first_name = QtWidgets.QLabel(parent=self.widget1)
        self.label_prof_first_name.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.label_prof_first_name.setText("")
        self.label_prof_first_name.setObjectName("label_prof_first_name")
        self.verticalLayout_4.addWidget(self.label_prof_first_name)
        self.label_prof_first_name.raise_()
        self.label_prof_first_name_header.raise_()
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 130, 271, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_prof_pass_header = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_pass_header.setFont(font)
        self.label_prof_pass_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_pass_header.setObjectName("label_prof_pass_header")
        self.verticalLayout_6.addWidget(self.label_prof_pass_header)
        self.lineEdit_prof_pass = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.lineEdit_prof_pass.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_prof_pass.setText("")
        self.lineEdit_prof_pass.setObjectName("lineEdit_prof_pass")
        self.lineEdit_prof_pass.setMinimumHeight(31)
        self.lineEdit_prof_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout_6.addWidget(self.lineEdit_prof_pass)
        self.pushButton_chg_pass = QtWidgets.QPushButton(parent=self.frame_profile)
        self.pushButton_chg_pass.setGeometry(QtCore.QRect(330, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_chg_pass.setFont(font)
        self.pushButton_chg_pass.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(216, 216, 216);\n"
                                               "border: 1px solid #000000;\n"
                                               "border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color: rgb(192, 192, 192);\n"
                                               "padding-left: 3px;\n"
                                               "padding-right: 3px;\n"
                                               "}\n"
                                               )
        self.pushButton_chg_pass.setObjectName("pushButton_chg_pass")
        
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_3.setGeometry(QtCore.QRect(50, 210, 401, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_prof_email_header = QtWidgets.QLabel(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_email_header.setFont(font)
        self.label_prof_email_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_email_header.setObjectName("label_prof_email_header")
        self.verticalLayout_7.addWidget(self.label_prof_email_header)
        self.label_prof_email = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.label_prof_email.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.label_prof_email.setText("")
        self.label_prof_email.setObjectName("label_prof_email")
        self.verticalLayout_7.addWidget(self.label_prof_email)
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_4.setGeometry(QtCore.QRect(50, 290, 401, 71))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_prof_address_header = QtWidgets.QLabel(parent=self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_address_header.setFont(font)
        self.label_prof_address_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_address_header.setObjectName("label_prof_address_header")
        self.verticalLayout_8.addWidget(self.label_prof_address_header)
        self.lineEdit_prof_address = QtWidgets.QLineEdit(parent=self.layoutWidget_4)
        self.lineEdit_prof_address.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_prof_address.setText("")
        self.lineEdit_prof_address.setObjectName("lineEdit_prof_address")
        self.lineEdit_prof_address.setMinimumHeight(31)
        self.verticalLayout_8.addWidget(self.lineEdit_prof_address)
        self.layoutWidget_5 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_5.setGeometry(QtCore.QRect(50, 450, 401, 71))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_prof_country_header = QtWidgets.QLabel(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_country_header.setFont(font)
        self.label_prof_country_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_country_header.setObjectName("label_prof_country_header")
        self.verticalLayout_9.addWidget(self.label_prof_country_header)
        self.comboBox_country = QtWidgets.QComboBox(parent=self.layoutWidget_5)
        self.comboBox_country.setMinimumSize(QtCore.QSize(0, 31))
        self.comboBox_country.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px")
        self.comboBox_country.setObjectName("comboBox_country")
        self.verticalLayout_9.addWidget(self.comboBox_country)
        
        self.layoutWidget_6 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_6.setGeometry(QtCore.QRect(340, 370, 111, 71))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_prof_zip_header = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_zip_header.setFont(font)
        self.label_prof_zip_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_zip_header.setObjectName("label_prof_zip_header")
        self.verticalLayout_10.addWidget(self.label_prof_zip_header)
        self.lineEdit_prof_zip = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.lineEdit_prof_zip.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_prof_zip.setText("")
        self.lineEdit_prof_zip.setObjectName("lineEdit_prof_zip")
        self.verticalLayout_10.addWidget(self.lineEdit_prof_zip)
        self.lineEdit_prof_zip.setMinimumHeight(31)
        
        self.layoutWidget_7 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_7.setGeometry(QtCore.QRect(200, 370, 131, 71))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_prof_state_header = QtWidgets.QLabel(parent=self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_state_header.setFont(font)
        self.label_prof_state_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_state_header.setObjectName("label_prof_state_header")
        self.verticalLayout_11.addWidget(self.label_prof_state_header)
        self.comboBox_state = QtWidgets.QComboBox(parent=self.layoutWidget_7)
        self.comboBox_state.setMinimumSize(QtCore.QSize(0, 31))
        self.comboBox_state.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px")
        self.comboBox_state.setObjectName("comboBox_state")
        self.verticalLayout_11.addWidget(self.comboBox_state)
        
        self.layoutWidget_8 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_8.setGeometry(QtCore.QRect(50, 530, 131, 71))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_prof_gender_header = QtWidgets.QLabel(parent=self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_gender_header.setFont(font)
        self.label_prof_gender_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_gender_header.setObjectName("label_prof_gender_header")
        self.verticalLayout_12.addWidget(self.label_prof_gender_header)
        self.comboBox_gender = QtWidgets.QComboBox(parent=self.layoutWidget_8)
        self.comboBox_gender.setMinimumSize(QtCore.QSize(0, 31))
        self.comboBox_gender.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px")
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.verticalLayout_12.addWidget(self.comboBox_gender)
        
        self.layoutWidget_9 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_9.setGeometry(QtCore.QRect(280, 530, 171, 71))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_prof_dob_header = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_dob_header.setFont(font)
        self.label_prof_dob_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_dob_header.setObjectName("label_prof_dob_header")
        self.verticalLayout_13.addWidget(self.label_prof_dob_header)
        self.dateEdit_dob = QtWidgets.QDateEdit(parent=self.layoutWidget_9)
        self.dateEdit_dob.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_dob.setFont(font)
        self.dateEdit_dob.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px")
        self.dateEdit_dob.setObjectName("dateEdit_dob")
        self.dateEdit_dob.setDisplayFormat("MMMM dd yyyy")
        self.verticalLayout_13.addWidget(self.dateEdit_dob)
        self.dateEdit_dob.setReadOnly(True)
        
        self.label_prof_header = QtWidgets.QLabel(parent=self.frame_profile)
        self.label_prof_header.setGeometry(QtCore.QRect(170, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_prof_header.setFont(font)
        self.label_prof_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_prof_header.setObjectName("label_prof_header")
        
        self.pushButton_prof_update = QtWidgets.QPushButton(parent=self.frame_profile)
        self.pushButton_prof_update.setGeometry(QtCore.QRect(185, 606, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_prof_update.setFont(font)
        self.pushButton_prof_update.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(216, 216, 216);\n"
                                               "border: 1px solid #000000;\n"
                                               "border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color: rgb(192, 192, 192);\n"
                                               "padding-left: 3px;\n"
                                               "padding-right: 3px;\n"
                                               "}\n"
                                               )
        self.pushButton_prof_update.setObjectName("pushButton_prof_update")
        
        self.label_prof_warning_2 = QtWidgets.QLabel(parent=self.frame_profile)
        self.label_prof_warning_2.setGeometry(QtCore.QRect(166, 133, 231, 31))
        self.label_prof_warning_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_prof_warning_2.setObjectName("label_prof_warning_2")
        self.label_prof_warning_2.setVisible(False)
        
        self.label_success = QtWidgets.QLabel(parent=self.frame_profile)
        self.label_success.setGeometry(QtCore.QRect(50, 610, 111, 21))
        self.label_success.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_success.setObjectName("label_success")
        self.label_success.setVisible(False)
        
        self.layoutWidget_12 = QtWidgets.QWidget(parent=self.frame_profile)
        self.layoutWidget_12.setGeometry(QtCore.QRect(50, 370, 141, 71))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_prof_city_header = QtWidgets.QLabel(parent=self.layoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_city_header.setFont(font)
        self.label_prof_city_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_city_header.setObjectName("label_prof_city_header")
        self.verticalLayout_16.addWidget(self.label_prof_city_header)
        self.lineEdit_city = QtWidgets.QLineEdit(parent=self.layoutWidget_12)
        self.lineEdit_city.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px")
        self.lineEdit_city.setText("")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.verticalLayout_16.addWidget(self.lineEdit_city)
        self.lineEdit_city.setMinimumHeight(31)
        
        self.frame_chg_pass = QtWidgets.QFrame(parent=self.frame_Center_Main)
        self.frame_chg_pass.setStyleSheet("QFrame#frame_chg_pass {\n"
"border: 1px solid #D4AF37;\n"
"background-color: rgb(45, 45, 45);\n"
"}")
        
        self.frame_chg_pass = QtWidgets.QFrame(parent=self.frame_Center_Main)
        self.frame_chg_pass.setGeometry(QtCore.QRect(491, 201, 0, 261))
        self.frame_chg_pass.setStyleSheet("QFrame#frame_chg_pass {\n"
"border: 1px solid #D4AF37;\n"
"background-color: rgb(45, 45, 45);\n"
"}")
        self.frame_chg_pass.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_chg_pass.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_chg_pass.setObjectName("frame_chg_pass")
        self.layoutWidget_10 = QtWidgets.QWidget(parent=self.frame_chg_pass)
        self.layoutWidget_10.setGeometry(QtCore.QRect(10, 10, 271, 71))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_prof_new_pass_header = QtWidgets.QLabel(parent=self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_new_pass_header.setFont(font)
        self.label_prof_new_pass_header.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_new_pass_header.setObjectName("label_prof_new_pass_header")
        self.verticalLayout_14.addWidget(self.label_prof_new_pass_header)
        self.lineEdit_prof_new_pass = QtWidgets.QLineEdit(parent=self.layoutWidget_10)
        self.lineEdit_prof_new_pass.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_prof_new_pass.setText("")
        self.lineEdit_prof_new_pass.setObjectName("lineEdit_prof_new_pass")
        self.lineEdit_prof_new_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_prof_new_pass.setMinimumHeight(31)
        self.verticalLayout_14.addWidget(self.lineEdit_prof_new_pass)
        self.layoutWidget_11 = QtWidgets.QWidget(parent=self.frame_chg_pass)
        self.layoutWidget_11.setGeometry(QtCore.QRect(10, 90, 271, 71))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_prof_new_pass_header_2 = QtWidgets.QLabel(parent=self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prof_new_pass_header_2.setFont(font)
        self.label_prof_new_pass_header_2.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
        self.label_prof_new_pass_header_2.setObjectName("label_prof_new_pass_header_2")
        self.verticalLayout_15.addWidget(self.label_prof_new_pass_header_2)
        self.lineEdit_prof_new_pass_2 = QtWidgets.QLineEdit(parent=self.layoutWidget_11)
        self.lineEdit_prof_new_pass_2.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px\n"
"")
        self.lineEdit_prof_new_pass_2.setText("")
        self.lineEdit_prof_new_pass_2.setObjectName("lineEdit_prof_new_pass_2")
        self.lineEdit_prof_new_pass_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_prof_new_pass_2.setMinimumHeight(31)
        self.verticalLayout_15.addWidget(self.lineEdit_prof_new_pass_2)
        self.pushButton_chg_submit = QtWidgets.QPushButton(parent=self.frame_chg_pass)
        self.pushButton_chg_submit.setGeometry(QtCore.QRect(80, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_chg_submit.setFont(font)
        self.pushButton_chg_submit.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(216, 216, 216);\n"
                                               "border: 1px solid #000000;\n"
                                               "border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color: rgb(192, 192, 192);\n"
                                               "padding-left: 3px;\n"
                                               "padding-right: 3px;\n"
                                               "}\n"
                                               )
        self.pushButton_chg_submit.setObjectName("pushButton_chg_submit")
        
        self.label_prof_warning = QtWidgets.QLabel(parent=self.frame_chg_pass)
        self.label_prof_warning.setGeometry(QtCore.QRect(10, 220, 269, 31))
        self.label_prof_warning.setStyleSheet("")
        self.label_prof_warning.setText("")
        self.label_prof_warning.setObjectName("label_prof_warning")
        self.label_prof_warning.setVisible(False)
        
        self.comboBox_state.addItems([
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", 
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
    "West Virginia", "Wisconsin", "Wyoming", 
    "Armed Forces Americas (AA)", 
    "Armed Forces Europe (AE)", 
    "Armed Forces Pacific (AP)"
])
        
        self.comboBox_country.addItems([
    "United States", "Canada", "Mexico", "Cuba", "Puerto Rico", 
    "Guatemala", "Belize", "Costa Rica", "El Salvador", "Honduras", 
    "Nicaragua", "Panama", "Argentina", "Brazil", "Chile", "Colombia", 
    "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "Australia", 
    "New Zealand", "United Kingdom", "Ireland", "France", "Germany", 
    "Italy", "Spain", "Portugal", "Netherlands", "Belgium", "Switzerland", 
    "Austria", "Sweden", "Norway", "Denmark", "Finland", "Iceland", 
    "Russia", "China", "Japan", "South Korea", "India", "Pakistan", 
    "Bangladesh", "Sri Lanka", "Nepal", "Maldives", "Indonesia", 
    "Thailand", "Vietnam", "Philippines", "Malaysia", "Singapore", 
    "South Africa", "Egypt", "Nigeria", "Kenya", "Ethiopia", "Israel", 
    "Saudi Arabia", "United Arab Emirates", "Turkey", "Iran", "Iraq", 
    "Argentina", "Brazil", "Chile", "Cuba", "Dominican Republic", 
    "Jamaica", "Trinidad and Tobago", "Haiti"
])
        
        self.comboBox_gender.addItems(["Male", "Female", "Custom"])

        self.frame_Center_Main.raise_()
        self.textBrowser.raise_()
        self.tableView.raise_()
        self.frame_Header.raise_()
        self.frame_Footer.raise_()
        self.frame_Logo.raise_()
        self.pushButton_Help.raise_()
        self.pushButton_Terms.raise_()
        self.pushButton_Privacy.raise_()
        self.frame_profile.raise_()
        self.frame_chg_pass.raise_()
        self.frame_Menu_Left.raise_()
        self.frame_SW_Filter_Menu.raise_()
        self.pushButton_Top_Menu_Carrot.raise_()
        self.pushButton_Side_Menu_Carrot.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """
        Retranslate the user interface by setting the text of various widgets.

        This function sets the text of the UI components, such as labels, buttons,
        and checkboxes, to their respective translations. It is called when the
        application is initialized or when the language is changed.

        Args:
            MainWindow (QtWidgets.QMainWindow): The main window object that contains
            the user interface elements.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Minimize.setText(_translate("MainWindow", ""))
        self.pushButton_Exit.setText(_translate("MainWindow", ""))
        self.pushButton_Maximize.setText(_translate("MainWindow", ""))
        self.pushButton_Menu.setText(_translate("MainWindow", ""))
        self.pushButton_Home.setText(_translate("MainWindow", "HOME"))
        self.pushButton_Account.setText(_translate("MainWindow", "ACCOUNT"))
        self.pushButton_Settings.setText(_translate("MainWindow", "SETTINGS"))
        self.label_Footer_Text_Left.setText(
            _translate(
                "MainWindow", "© 2024 Galactic Reads | Explore the Stars of Literature"
            )
        )
        self.label_Footer_Text_Center.setText(
            _translate("MainWindow", "App Version: v1.0.3 | User:")
        )
        self.pushButton_Help.setText(_translate("MainWindow", "Help"))
        self.pushButton_Terms.setText(_translate("MainWindow", "Terms"))
        self.pushButton_Privacy.setText(_translate("MainWindow", "Privacy Policy"))
        self.label_Filter.setText(_translate("MainWindow", "Filter by:"))
        self.label_Line1.setText(
            _translate("MainWindow", "---------------------------")
        )
        self.label_Universe.setText(_translate("MainWindow", "Universe"))
        self.label_Line2.setText(
            _translate("MainWindow", "---------------------------")
        )
        self.label_Universe_2.setText(_translate("MainWindow", "Novel Type"))
        self.label_Line3.setText(
            _translate("MainWindow", "---------------------------")
        )
        self.label_Universe_3.setText(_translate("MainWindow", "Era"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear Filter"))
        self.checkBox_Legends.setText(_translate("MainWindow", "Legends"))
        self.checkBox_Canon.setText(_translate("MainWindow", "Canon"))
        self.checkBox_Both.setText(_translate("MainWindow", "Both"))
        self.checkBox_ON.setText(_translate("MainWindow", "Original Novels (ON)"))
        self.checkBox_NA.setText(_translate("MainWindow", "Novel Adaptations (NA)"))
        self.checkBox_OJR.setText(
            _translate("MainWindow", "Original Junior Novels (OJR)")
        )
        self.checkBox_JRA.setText(
            _translate("MainWindow", "Junior Novel Adaptations (JRA)")
        )
        self.checkBox_YR.setText(_translate("MainWindow", "Young Readers (YR)"))
        self.checkBox_YA.setText(_translate("MainWindow", "Young Adult Novels (YA)"))
        self.checkBox_S.setText(_translate("MainWindow", "Script Books (S)"))
        self.checkBox_GB.setText(_translate("MainWindow", "Gamebooks (GB)"))
        self.checkBox_DOTJ.setText(
            _translate("MainWindow", "Dawn of the Jedi ~ 25,000 BBY")
        )
        self.checkBox_TOR.setText(
            _translate("MainWindow", "The Old Republic 25,000 - 1,000 BBY")
        )
        self.checkBox_THR.setText(
            _translate("MainWindow", "The High Republic 500 BBY - 100 BBY")
        )
        self.checkBox_FOTJ.setText(
            _translate("MainWindow", "Fall of the Jedi 100 BBY - 19 BBY")
        )
        self.checkBox_NJO.setText(
            _translate("MainWindow", "Reign of the Empire 19 BBY - 5 BBY")
        )
        self.checkBox_ROTE.setText(
            _translate("MainWindow", "Age of Rebellion 5 BBY - 4 ABY")
        )
        self.checkBox_ROTFO.setText(
            _translate("MainWindow", "The New Republic 5 ABY - 34 ABY")
        )
        self.checkBox_AOR.setText(
            _translate("MainWindow", "Rise of the First Order 34 ABY - 35 ABY")
        )
        self.checkBox_TNR.setText(
            _translate("MainWindow", "New Jedi Order 36 ABY - Unknown")
        )

        self.pushButton_Top_Menu_Carrot.setText(_translate("MainWindow", ""))
        self.pushButton_Side_Menu_Carrot.setText(_translate("MainWindow", ""))
        self.label_prof_last_name_header.setText(_translate("MainWindow", "Last Name"))
        self.label_prof_first_name_header.setText(_translate("MainWindow", "First Name"))
        self.label_prof_pass_header.setText(_translate("MainWindow", "Password"))
        self.pushButton_chg_pass.setText(_translate("MainWindow", "Change Password"))
        self.label_prof_email_header.setText(_translate("MainWindow", "Email"))
        self.label_prof_address_header.setText(_translate("MainWindow", "Address"))
        self.label_prof_country_header.setText(_translate("MainWindow", "Country"))
        self.label_prof_zip_header.setText(_translate("MainWindow", "Zip Code"))
        self.label_prof_state_header.setText(_translate("MainWindow", "State"))
        self.label_prof_gender_header.setText(_translate("MainWindow", "Gender"))
        self.label_prof_dob_header.setText(_translate("MainWindow", "Date of Birth"))
        self.label_prof_header.setText(_translate("MainWindow", "My profile"))
        self.pushButton_prof_update.setText(_translate("MainWindow", "Update"))
        self.label_prof_warning_2.setText(_translate("MainWindow", "Incorrect password!"))
        self.label_success.setText(_translate("MainWindow", "Updated Successfully!"))
        self.label_prof_city_header.setText(_translate("MainWindow", "City"))
        self.pushButton_prof_update.setText(_translate("MainWindow", "Update"))
        self.label_prof_new_pass_header.setText(_translate("MainWindow", "New Password"))
        self.label_prof_new_pass_header_2.setText(_translate("MainWindow", "Confirm Password"))
        self.pushButton_chg_submit.setText(_translate("MainWindow", "Submit"))
