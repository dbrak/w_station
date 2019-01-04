import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QSlider
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'F To C'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        c = 1
        data = 100
        p = "ºC"

        self.lable = QLabel()
        self.lable.move(30, 30)
        self.lable.setText(str(data) + str(p))

        self.convert = QPushButton("Change to ºF", self)
        self.convert.adjustSize()
        self.convert.move(2.5, 450)

        if c % 2 == 0:
            self.convert.clicked.connect(self.onclick(False, data, c))
            p = "ºF"
        else:
            self.convert.clicked.connect(self.onclick(True, data, c))
            p = "ºF"

        self.show()

    @pyqtSlot()
    def onclick(self,u, data, c):
        if u == True:
            data = (data - 32) * 5 / 9
            self.convert.setText("Change to ºC")
            self.convert.adjustSize()
        else:
            data = (data * 9 / 5) + 32
            self.convert.setText("Change to ºF")
            self.convert.adjustSize()
        c = c + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
