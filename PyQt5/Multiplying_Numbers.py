import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Multiplication'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Making the Text Boxes
        self.n1 = QLineEdit(self)
        self.n1.move(20, 30)
        self.n1.resize(240, 40)

        self.n1l = QLabel("Enter number 1",self)
        self.n1l.move(20,5)


        self.n2 = QLineEdit(self)
        self.n2.move(20, 100)
        self.n2.resize(240, 40)

        self.n2l = QLabel("Enter number 2",self)
        self.n2l.move(20,75)


        # Making The Button
        self.button = QPushButton("Press To Multiply", self)
        self.button.move(20, 150)

        # Linking to the funtion
        self.button.clicked.connect(self.onclick)
        self.button.adjustSize()

        self.show()

    @pyqtSlot()
    def onclick(self):
        #Making Variable
        n1value = int(self.n1.text())
        n2value = int(self.n2.text())
        multiplied = str(n1value * n2value)

        #Puting it in a messagebox
        QMessageBox.question(self, "Multiplying", str(n1value) + " X " + str(n2value) + " = " + multiplied, QMessageBox.Ok,
                             QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
