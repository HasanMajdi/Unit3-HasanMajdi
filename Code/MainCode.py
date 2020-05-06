import csv
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem, QColorDialog
from PyQt5.uic.properties import QtGui
from Equitable import Equi_Table
from Users import User
from MainPage import Ui_MainWindow
from loginFin import Ui_login
from myLib import verify_password, hash_password


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.data = self.load_data()
        self.Users_btn.clicked.connect(self.UesApp)
        self.Equipments.clicked.connect(self.EqApp)
        self.Confirm_Main.clicked.connect(self.save)
        self.Revert_Main.clicked.connect(self.cancel)
        self.Tabl_Items.cellChanged.connect(self.changeDB)

        log = Loginpage(self)
        log.show()

    def load_data(self):
        data = []
        with open('db.csv') as mydatabase:
            file = csv.reader(mydatabase, delimiter=",")
            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    print(col)
                    data.append([i, j, col])
                    self.Tabl_Items.setItem(i, j, QTableWidgetItem(col))
        return data

    def changeDB(self):
        item = self.Tabl_Items.currentItem()  # clicking itme
        row = self.Tabl_Items.currentRow()  # Clicking row
        col = self.Tabl_Items.currentColumn()  # Clicking Col
        # show the item in the terminal for debugging proccess
        self.Revert_Main.setDisabled(False)
        self.Confirm_Main.setDisabled(False)

    def UesApp(self):
        UVar = usewind(self)
        UVar.show()

    def EqApp(self):
        Eq = EqTable(self)
        Eq.show()

    def save(self):
        print("Save to csv file")

    def cancel(self):
        print("Reload the Table")


class Loginpage(Ui_login):
    def __init__(self, parent=None):
        super(Loginpage, self).__init__(parent)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.try_login)

    def try_login(self):
        # Read the entred username
        user = self.Username.text()
        print('username entered=', user)
        # Read the entred password
        password = self.Password.text()
        print('Password', password)
        PassUSe = (user + password)
        # Open the file with the passwords
        with open('Output.csv') as Output_file:
            # Read in the file
            file = csv.reader(Output_file)
            for f in file:
                hsh = f
            print(hsh)
            # use the vertify_password function with the stored and given password
            Hash = verify_password(hash_password(hsh[0]), PassUSe)
            print(PassUSe)
            print(Hash)
            # if the password matches break the loop and close
            if Hash:
                self.close()
            # if not ; show an error , RED FRAME FOR BUTTONS
            else:
                self.Username.setStyleSheet("#Username{\n"
                                            "border: 3px solid;\n"
                                            "border-color: red;\n"
                                            "}")
                self.Password.setStyleSheet("#Password{\n"
                                            "border: 3px solid;\n"
                                            "border-color: red;\n"
                                            "}")
                print("Wrong password")


class usewind(User):
    def __init__(self, parent=None):
        super(usewind, self).__init__(parent)
        self.setupUi(self)
        self.Back_U.clicked.connect(self.exit_user)

    def exit_user(self):
        self.close()


class EqTable(Equi_Table):
    def __init__(self, parent=None):
        super(EqTable, self).__init__(parent)
        self.setupUi(self)
        print("Clicked", self.Back_Eq.clicked.connect(self.exit_Equi))

    def exit_Equi(self):
        self.close()


app = QApplication(sys.argv)
widget = Main()
widget.show()
sys.exit(app.exec_())
