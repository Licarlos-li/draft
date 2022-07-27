# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
import numpy as np
 
 
class BallCartoon(QMainWindow):
    n = 0
    flag = 0
    ani_w = None
 
    def __init__(self):
        super(BallCartoon, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(1000, 600)
        self.setWindowTitle('弹 弹 弹')
        self.setFixedSize(self.width(), self.height())
        self.btn_start = QPushButton(self)
        self.btn_start.setText('Start')
        self.btn_start.setGeometry(500, 500, 100, 50)
 
        self.btn_start.clicked.connect(self.slot_btn_start)
 
    def resizeEvent(self, event):
        palette = QPalette()
        pix = QPixmap('yu.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)
 
    def slot_btn_start(self):
        self.mbt = MyBeautifulThread()
        self.mbt.trigger.connect(self.mimi)
        self.mbt.start()
 
    def mimi(self, msg):
        self.btn_1 = QPushButton(self)
        self.btn_1.setStyleSheet('''
                            QPushButton
                             {text-align : center;
                             background-color : cyan;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             QPushButton:pressed
                             {text-align : center;
                             background-color : red;
                             font: bold;
                             border-color: cyan;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             ''')
        self.btn_1.setGeometry(200, 300, 20, 20)
        self.btn_1.show()
        self.down(self.btn_1, QEasingCurve.OutBounce)
        self.n = np.random.randint(0, 950)
 
    def down(self, kj, css):
        animation = QPropertyAnimation(kj, b'pos', self)
        animation.setStartValue(QPoint(self.n, 0))
        animation.setEndValue(QPoint(self.n, 500))
        animation.setDuration(2500)
        animation.setEasingCurve(css)
        animation.start()
        animation.finished.connect(kj.deleteLater)
 
    def closeEvent(self, event):
        if self.ani_w is None:
            self.ani_w = QPropertyAnimation(self, b'windowOpacity', self)
            self.ani_w.setStartValue(1)
            self.ani_w.setEndValue(0)
            self.ani_w.setDuration(3000)
            self.ani_w.finished.connect(self.close)
            self.ani_w.start()
            event.ignore()
 
 
class MyBeautifulThread(QThread):
    trigger = pyqtSignal(str)
 
    def __init__(self):
        super(MyBeautifulThread, self).__init__()
 
    def run(self):
        w = BallCartoon()
        while 1:
            self.trigger.emit('6')
            time.sleep(0.2)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    bc = BallCartoon()
    bc.show()
    sys.exit(app.exec_())