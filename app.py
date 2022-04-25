from PyQt5.QtCore import QEvent
import sys
from random import randint
from PyQt5.QtWidgets import (QWidget, QApplication,
QLabel,QPushButton,QMessageBox)
from Style.style import style

class mouseoverEvent(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.width = 500
        self.height = 400

        self.title = QLabel('Do you want to be my girlfriend?', self)
        self.title.setGeometry(110, 20, 300, 40)
        
        self.btnNo = QPushButton('No',self)
        self.btnNo.setObjectName('btnNo')
        self.btnNo.setGeometry(120, 100, 100, 35)
        self.btnNo.installEventFilter(self)

        self.btnYes = QPushButton('Yes',self)
        self.btnYes.setObjectName('btnYes')
        self.btnYes.setGeometry(290, 100, 100, 35)
        self.btnYes.clicked.connect(lambda: self.getMessage())
        
        self.setStyleSheet(style)
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.show()
    def getMessage(self):
            message = QMessageBox(self)
            message.setWindowTitle('Girlfriend')
            message.setIcon(QMessageBox.Information)
            message.setText('You are my girlfriend!')  
            message.exec_()



    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter :
            self.btnNo.setGeometry(randint(event.y(),self.width-event.x()),
            randint(event.x(),self.height-event.y()), 100, 35)
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mouseoverEvent()
    sys.exit(app.exec_())