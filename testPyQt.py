from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        self.loc_x = 100
        self.loc_y = 100
        self.width = 1280
        self.height = 720
        self.title = 'Title'
        self.setGeometry(self.loc_x, self.loc_y, self.width, self.height)
        self.setWindowTitle(self.title)
        self.app = QApplication(sys.argv)
        self.center = [int(self.width / 2), int(self.height / 2)]

        self.createWindow()

    def createWindow(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText('This is my first! Hope it goes well.')
        self.label.setGeometry(0, 0, 150, 20)
        self.label.move(self.center[0],self.center[1])

        #Add button
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Click!')
        self.button1.setGeometry(50, 50, 150, 50)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('You pressed the button! You pressed the button!')
        self.update()

    def update(self):
        self.label.adjustSize()


def main():
    app = QApplication(sys.argv)
    firstWindow = mainWindow()
    firstWindow.show()
    sys.exit(app.exec_())

#This essientially says that this file is the main file and cannot be imported!!
if __name__ == '__main__':
    main()