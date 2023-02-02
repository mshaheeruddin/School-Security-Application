import sys
from LoginForm import Ui_SVA
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_SVA):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
