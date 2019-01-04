
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Button And Status Bar'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 440
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Stataus Bar Code
        self.statusBar().showMessage('Status bar')

        #Button Code
        button = QPushButton('Push ME', self)
        button.setToolTip('Speed Up')
        button.move(300,200)
        @pyqtSlot()
        def on_click(self):
            print('You Clicked ME')
        button.clicked.connect(on_click)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
