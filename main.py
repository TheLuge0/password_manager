import sys
from PyQt6 import QtWidgets, QtCore, QtGui
import os
from api import *


class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        """Init the window"""
        super().__init__()
        self.setup_ui()
        self.setup_connection()


    def setup_ui(self):
        """Create the ui"""
        popup.setObjectName("Form")
        popup.resize(400, 295)
        self.fr_all = QtWidgets.QFrame(parent=popup)
        self.fr_all.setGeometry(QtCore.QRect(-20, -10, 421, 321))
        self.fr_all.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.fr_all.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_all.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_all.setObjectName("fr_all")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.fr_all)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 374, 47))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.Hlayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Hlayout_2.setContentsMargins(15, 0, 20, 0)
        self.Hlayout_2.setSpacing(0)
        self.Hlayout_2.setObjectName("Hlayout_2")
        self.fr_logo = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.fr_logo.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fr_logo.setFont(font)
        self.fr_logo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fr_logo.setLineWidth(1)
        self.fr_logo.setMidLineWidth(0)
        self.fr_logo.setPixmap(QtGui.QPixmap("image/807241.png"))
        self.fr_logo.setScaledContents(True)
        self.fr_logo.setIndent(-1)
        self.fr_logo.setObjectName("label")
        self.Hlayout_2.addWidget(self.fr_logo)
        self.Hlayout_2.addWidget(self.fr_logo)
        self.lb_title = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_title.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lb_title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lb_title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.lb_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_title.setObjectName("lb_title")
        self.Hlayout_2.addWidget(self.lb_title)
        self.lb_info = QtWidgets.QLabel(parent=self.fr_all)
        self.lb_info.setGeometry(QtCore.QRect(40, 95, 359, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_info.setFont(font)
        self.lb_info.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_info.setObjectName("lb_info")

        if first_time():
            self.lb_firsttime = QtWidgets.QLabel(parent=self.fr_all)
            self.lb_firsttime.setGeometry(QtCore.QRect(30, 175, 371, 21))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.lb_firsttime.setFont(font)
            self.lb_firsttime.setStyleSheet("color: rgb(255, 255, 255);")
            self.lb_firsttime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.lb_firsttime.setObjectName("lb_firsttime")
        else: 
            self.lb_error = QtWidgets.QLabel(parent=self.fr_all)
            self.lb_error.setGeometry(QtCore.QRect(30, 175, 371, 21))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.lb_error.setFont(font)
            self.lb_error.setStyleSheet("color: rgb(255, 50, 50);")
            self.lb_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.lb_error.setObjectName("lb_error")
            self.lb_error.hide()
                

        self.le_input = QtWidgets.QLineEdit(parent=self.fr_all)
        self.le_input.setGeometry(QtCore.QRect(20, 135, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_input.setFont(font)
        self.le_input.setStyleSheet("color: rgb(255, 255, 255);\n""\n""")
        self.le_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.le_input.setFrame(False)
        self.le_input.setDragEnabled(False)
        self.le_input.setReadOnly(False)
        self.le_input.setPlaceholderText("")
        self.le_input.setClearButtonEnabled(True)
        self.le_input.setObjectName("le_input")
        self.line_up = QtWidgets.QFrame(parent=self.fr_all)
        self.line_up.setGeometry(QtCore.QRect(-20, 165, 461, 5))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.line_up.setFont(font)
        self.line_up.setAutoFillBackground(False)
        self.line_up.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.line_up.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.line_up.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_up.setLineWidth(1)
        self.line_up.setObjectName("line_up")
        self.line_down = QtWidgets.QFrame(parent=self.fr_all)
        self.line_down.setGeometry(QtCore.QRect(-30, 135, 461, 5))
        self.line_down.setAutoFillBackground(False)
        self.line_down.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.line_down.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.line_down.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_down.setLineWidth(1)
        self.line_down.setObjectName("line_down")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.fr_all)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 220, 361, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Hlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Hlayout.setContentsMargins(0, 0, 0, 0)
        self.Hlayout.setObjectName("Hlayout")
        self.btn_validate = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_validate.setFont(font)
        self.btn_validate.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.btn_validate.setCheckable(False)
        self.btn_validate.setDefault(False)
        self.btn_validate.setFlat(False)
        self.btn_validate.setObjectName("btn_validate")
        self.Hlayout.addWidget(self.btn_validate)
        self.btn_cancel = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.btn_cancel.setCheckable(False)
        self.btn_cancel.setDefault(False)
        self.btn_cancel.setFlat(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.Hlayout.addWidget(self.btn_cancel)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(popup)


    def retranslateUi(self):
        """Create the ui"""
        _translate = QtCore.QCoreApplication.translate
        popup.setWindowTitle(_translate("Form", "Gestionnaire de mot de passe"))
        self.lb_title.setText(_translate("Form", "Gestionnaire de mot de passe"))
        if first_time():
            self.lb_firsttime.setText(_translate("From", "Attention vous ne pourrez plus le modifier ni le voir !"))
            self.lb_info.setText(_translate("Form", "Définisez votre mot de passe:"))
        else:
            self.lb_info.setText(_translate("Form", "Entrez votre mot de passe:"))
            self.lb_error.setText(_translate("Form", "Mot de passe invalide, veuillez réessayer")) 
        self.btn_validate.setText(_translate("Form", "Valider"))
        self.btn_cancel.setText(_translate("Form", "Quitter"))


    def setup_connection(self):
        """Setup the user's inputs"""
        self.btn_validate.clicked.connect(self.open_window)
        self.btn_cancel.clicked.connect(self.close_window)
        self.le_input.returnPressed.connect(self.open_window)


    def open_window(self):
        """Generate the key

        Returns:
            bool : False if line edit is empty
        """
        global key
        input_user = self.le_input.text()
        if first_time():
            if input_user == "":
                return False
            salt = init_salt()
            password = define_password(input_user, salt)
            init_password(password)
        else:
            salt = load_salt()
            password = define_password(input_user, salt)
        key = password
        if check_password(password):
            main_window.show()
            ui.reload_tablewidget()
            popup.hide()
        else:
            self.lb_error.show()


    def close_window(self):
        """Close the window"""
        popup.hide()
        sys.exit()


class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        """Init the window"""
        super().__init__()
        self.setup_ui()
        self.setup_coonections()


    def setup_ui(self):
        """Create the ui"""
        main_window.setObjectName("MainWindow")
        main_window.resize(795, 606)
        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.fr_all = QtWidgets.QFrame(parent=self.centralwidget)
        self.fr_all.setGeometry(QtCore.QRect(-30, -20, 841, 641))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fr_all.setFont(font)
        self.fr_all.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.fr_all.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_all.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_all.setObjectName("fr_all")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.fr_all)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, 40, 870, 82))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Hlayout1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Hlayout1.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.Hlayout1.setContentsMargins(150, 0, 0, 0)
        self.Hlayout1.setSpacing(30)
        self.Hlayout1.setObjectName("Hlayout1")
        self.lb_logo = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lb_logo.setMaximumSize(QtCore.QSize(75, 75))
        self.lb_logo.setText("")
        self.lb_logo.setPixmap(QtGui.QPixmap("image/807241.png"))
        self.lb_logo.setScaledContents(True)
        self.lb_logo.setObjectName("lb_logo")
        self.Hlayout1.addWidget(self.lb_logo)
        self.lb_title = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lb_title.setFont(font)
        self.lb_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lb_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_title.setObjectName("lb_title")
        self.Hlayout1.addWidget(self.lb_title)
        self.Hlayout1.setStretch(1, 6)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.fr_all)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 519, 711, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.Hlayout2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Hlayout2.setContentsMargins(0, 0, 0, 0)
        self.Hlayout2.setObjectName("Hlayout2")
        self.btn_add = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_add.setCheckable(False)
        self.btn_add.setAutoRepeat(False)
        self.btn_add.setAutoDefault(False)
        self.btn_add.setFlat(False)
        self.btn_add.setObjectName("btn_add")
        self.Hlayout2.addWidget(self.btn_add)
        self.btn_delete = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_delete.setObjectName("btn_delete")
        self.Hlayout2.addWidget(self.btn_delete)
        self.tw_main = QtWidgets.QTableWidget(parent=self.fr_all)
        self.tw_main.setGeometry(QtCore.QRect(90, 190, 671, 311))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.tw_main.setFont(font)
        self.tw_main.setAutoFillBackground(False)
        self.tw_main.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.tw_main.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tw_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tw_main.setLineWidth(0)
        self.tw_main.setMidLineWidth(0)
        self.tw_main.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tw_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tw_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tw_main.setAutoScroll(True)
        self.tw_main.setAutoScrollMargin(16)
        self.tw_main.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tw_main.setTabKeyNavigation(True)
        self.tw_main.setDragEnabled(False)
        self.tw_main.setAlternatingRowColors(False)
        self.tw_main.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tw_main.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_main.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tw_main.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tw_main.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tw_main.setShowGrid(True)
        self.tw_main.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tw_main.setWordWrap(True)
        self.tw_main.setCornerButtonEnabled(True)
        self.tw_main.setRowCount(0)
        self.tw_main.setObjectName("tw_main")
        self.tw_main.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        item.setFont(font)
        item.setBackground(QtGui.QColor(40, 40, 40))
        self.tw_main.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        item.setFont(font)
        item.setBackground(QtGui.QColor(40, 40, 40))
        self.tw_main.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_main.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_main.setItem(0, 1, item)
        self.tw_main.horizontalHeader().setVisible(False) #type: ignore
        self.tw_main.horizontalHeader().setCascadingSectionResizes(False) #type: ignore
        self.tw_main.horizontalHeader().setDefaultSectionSize(250) #type: ignore
        self.tw_main.horizontalHeader().setHighlightSections(True) #type: ignore
        self.tw_main.horizontalHeader().setMinimumSectionSize(0) #type: ignore
        self.tw_main.horizontalHeader().setSortIndicatorShown(False) #type: ignore
        self.tw_main.horizontalHeader().setStretchLastSection(True) #type: ignore
        self.tw_main.verticalHeader().setVisible(False) #type: ignore
        self.tw_main.verticalHeader().setCascadingSectionResizes(False) #type: ignore
        self.tw_main.verticalHeader().setDefaultSectionSize(55) #type: ignore
        self.tw_main.verticalHeader().setHighlightSections(True) #type: ignore
        self.tw_main.verticalHeader().setMinimumSectionSize(0) #type: ignore
        self.tw_main.verticalHeader().setSortIndicatorShown(False) #type: ignore
        self.tw_main.verticalHeader().setStretchLastSection(False) #type: ignore
        self.line_left = QtWidgets.QFrame(parent=self.fr_all)
        self.line_left.setGeometry(QtCore.QRect(40, 10, 31, 641))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_left.setFont(font)
        self.line_left.setMouseTracking(False)
        self.line_left.setTabletTracking(False)
        self.line_left.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.line_left.setAcceptDrops(False)
        self.line_left.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line_left.setAutoFillBackground(False)
        self.line_left.setStyleSheet("\n"
"color: rgb(255, 170, 0);\n"
"")
        self.line_left.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_left.setLineWidth(5)
        self.line_left.setMidLineWidth(0)
        self.line_left.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_left.setObjectName("line_left")
        self.line_right = QtWidgets.QFrame(parent=self.fr_all)
        self.line_right.setGeometry(QtCore.QRect(780, 0, 31, 641))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_right.setFont(font)
        self.line_right.setMouseTracking(False)
        self.line_right.setTabletTracking(False)
        self.line_right.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.line_right.setAcceptDrops(False)
        self.line_right.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line_right.setAutoFillBackground(False)
        self.line_right.setStyleSheet("color: rgb(255, 170, 0);")
        self.line_right.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_right.setLineWidth(5)
        self.line_right.setMidLineWidth(0)
        self.line_right.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_right.setObjectName("line_right")
        self.lb_account = QtWidgets.QLabel(parent=self.fr_all)
        self.lb_account.setGeometry(QtCore.QRect(90, 140, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_account.setFont(font)
        self.lb_account.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_account.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lb_account.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_account.setObjectName("lb_account")
        self.lb_password = QtWidgets.QLabel(parent=self.fr_all)
        self.lb_password.setGeometry(QtCore.QRect(340, 140, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_password.setFont(font)
        self.lb_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_password.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lb_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_password.setObjectName("lb_password")
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.tw_main.raise_()
        self.line_right.raise_()
        self.line_left.raise_()
        self.lb_account.raise_()
        self.lb_password.raise_()
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)


    def retranslateUi(self, MainWindow):
        """Create the ui"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestionnaire de mot de passe"))
        self.lb_title.setText(_translate("MainWindow", "Gestionnaire de mot de passe"))
        self.btn_add.setText(_translate("MainWindow", "Ajouter"))
        self.btn_delete.setText(_translate("MainWindow", "Supprimer"))
        self.tw_main.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tw_main.setSortingEnabled(False)
        item = self.tw_main.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Account")) #type: ignore
        item = self.tw_main.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mot de passe")) #type: ignore
        __sortingEnabled = self.tw_main.isSortingEnabled()
        self.tw_main.setSortingEnabled(False)
        self.tw_main.setSortingEnabled(__sortingEnabled)
        self.lb_account.setText(_translate("MainWindow", "Compte"))
        self.lb_password.setText(_translate("MainWindow", "Mot de passe"))


    def setup_coonections(self):
        """Setup the user's inputs"""
        self.btn_add.clicked.connect(self.add_item)
        self.btn_delete.clicked.connect(self.delete_item)
        self.tw_main.itemChanged.connect(self.edit_item)

    
    def add_item(self):
        """Open the window for add item"""
        dialogue.show()
        self.reload_tablewidget()


    def reload_tablewidget(self):
        """Reload all the table widget"""
        for _ in range (0, (self.tw_main.rowCount())):
            self.tw_main.removeRow(0)

        all_data = load_data(path_data, key)
        n = 0
        for accounts, password in all_data.items():
            self.tw_main.insertRow(n)
            self.tw_main.setItem(n, 0, items(accounts))
            self.tw_main.setItem(n, 1, items(password))
            n += 1


    def delete_item(self):
        """Delete the selected rows"""
        for items in self.tw_main.selectedIndexes():
            account = self.tw_main.item(items.row(), 0).text() #type: ignore
            delete_data(account)
        self.reload_tablewidget()
        

    def edit_item(self):
        """Edit the data into the table widget"""
        all_data = load_data(path_data, key)
        if self.tw_main.selectedItems(): 
            row_number = self.tw_main.selectedIndexes()[0].row()
            new_account_name = self.tw_main.selectedItems()[0].text()
            new_password = self.tw_main.selectedItems()[1].text()
            if new_account_name and new_password:
                n = 0
                for old_account_name, _ in all_data.items():
                    if n == row_number:
                        if new_account_name != old_account_name:
                            os.rename(path_data / old_account_name, path_data / new_account_name)
                        else:
                            edit_data(path_data, old_account_name, new_password)
                            encrypt_data(path_data, old_account_name, key)
                    n += 1
            else:
                self.reload_tablewidget()
            

class Ui_Form2(object):

    def __init__(self):
        """Init the window"""
        super().__init__()
        self.setup_ui()
        self.setup_connections()


    def setup_ui(self):
        """Create the ui"""
        dialogue.setObjectName("Form")
        dialogue.resize(400, 300)
        self.fr_all = QtWidgets.QFrame(parent=dialogue)
        self.fr_all.setGeometry(QtCore.QRect(-11, -11, 421, 321))
        self.fr_all.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.fr_all.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_all.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_all.setObjectName("fr_all")
        self.le_count = QtWidgets.QLineEdit(parent=self.fr_all)
        self.le_count.setGeometry(QtCore.QRect(30, 60, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.le_count.setFont(font)
        self.le_count.setAutoFillBackground(False)
        self.le_count.setStyleSheet("color: rgb(255, 255, 255);")
        self.le_count.setText("")
        self.le_count.setFrame(False)
        self.le_count.setDragEnabled(True)
        self.le_count.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.le_count.setClearButtonEnabled(True)
        self.le_count.setObjectName("le_count")
        self.le_password = QtWidgets.QLineEdit(parent=self.fr_all)
        self.le_password.setEnabled(True)
        self.le_password.setGeometry(QtCore.QRect(30, 170, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.le_password.setFont(font)
        self.le_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.le_password.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.le_password.setText("")
        self.le_password.setFrame(False)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.le_password.setClearButtonEnabled(True)
        self.le_password.setObjectName("le_password")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.fr_all)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Hlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Hlayout.setContentsMargins(0, 0, 0, 0)
        self.Hlayout.setObjectName("Hlayout")
        self.btn_validate = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_validate.setFont(font)
        self.btn_validate.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.btn_validate.setCheckable(False)
        self.btn_validate.setDefault(False)
        self.btn_validate.setFlat(False)
        self.btn_validate.setObjectName("btn_validate")
        self.Hlayout.addWidget(self.btn_validate)
        self.btn_cancel = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.btn_cancel.setCheckable(False)
        self.btn_cancel.setDefault(False)
        self.btn_cancel.setFlat(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.Hlayout.addWidget(self.btn_cancel)
        self.line1 = QtWidgets.QFrame(parent=self.fr_all)
        self.line1.setGeometry(QtCore.QRect(-30, 57, 461, 5))
        self.line1.setAutoFillBackground(False)
        self.line1.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.line1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.line1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line1.setLineWidth(1)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QFrame(parent=self.fr_all)
        self.line2.setGeometry(QtCore.QRect(-10, 108, 461, 5))
        self.line2.setAutoFillBackground(False)
        self.line2.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.line2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.line2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line2.setLineWidth(1)
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QFrame(parent=self.fr_all)
        self.line3.setGeometry(QtCore.QRect(-20, 168, 461, 5))
        self.line3.setAutoFillBackground(False)
        self.line3.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.line3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.line3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line3.setLineWidth(1)
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QFrame(parent=self.fr_all)
        self.line4.setGeometry(QtCore.QRect(-20, 218, 461, 5))
        self.line4.setAutoFillBackground(False)
        self.line4.setStyleSheet("color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.line4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.line4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line4.setLineWidth(1)
        self.line4.setObjectName("line4")
        self.lb_1 = QtWidgets.QLabel(parent=self.fr_all)
        self.lb_1.setGeometry(QtCore.QRect(50, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_1.setFont(font)
        self.lb_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_1.setObjectName("lb_1")
        self.lb_2 = QtWidgets.QLabel(parent=self.fr_all)
        self.lb_2.setGeometry(QtCore.QRect(20, 130, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lb_2.setFont(font)
        self.lb_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_2.setObjectName("lb_2")

        self.retranslateUi(dialogue)
        QtCore.QMetaObject.connectSlotsByName(dialogue)


    def retranslateUi(self, Form):
        """Create the ui"""
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestionnaire de mot de passe"))
        self.btn_validate.setText(_translate("Form", "Valider"))
        self.btn_cancel.setText(_translate("Form", "Annuler"))
        self.lb_1.setText(_translate("Form", "Entrez le nom du compte :"))
        self.lb_2.setText(_translate("Form", "Entrez le mot de passe du compte :"))


    def setup_connections(self):
        """Setup the user's inputs"""
        self.btn_validate.clicked.connect(self.add_data)
        self.btn_cancel.clicked.connect(self.quit)


    def add_data(self):
        """Create a encrypt file with the password"""
        count = self.le_count.text()
        password = self.le_password.text()
        
        if count and password:
            edit_data(path_data, count.capitalize(), password)
            encrypt_data(path_data, count, key)

            ui.reload_tablewidget()
            self.le_count.clear()
            self.le_password.clear()
            dialogue.hide()


    def quit(self):
        """Close the window"""
        dialogue.hide()


class items(QtWidgets.QTableWidgetItem):

    def __init__(self, text):
        """Create a item for table widget

        Args:
            text : the 'name' of this item
        """
        super().__init__()
        self.setText(text)
        self.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.setFont(font)


app = QtWidgets.QApplication([])

main_window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()

popup = QtWidgets.QWidget()
ui2 = Ui_Form()

dialogue = QtWidgets.QWidget()
ui3 = Ui_Form2()

popup.show()

sys.exit(app.exec())
