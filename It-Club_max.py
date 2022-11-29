import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 141, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ГТА 6"))
        self.button.setText(_translate("MainWindow", "Нажми на меня"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.is_paint = False

        self.button.clicked.connect(self.paint)

    def paint(self):
        self.is_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for _ in range(10):
            # Задаем кисть
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            r = random.randint(5, 150)
            x_win, y_win = self.geometry().x(), self.geometry().y()
            x, y = random.randint(20, x_win - 20 - r - r), random.randint(20, y_win - 20 - r - r)
            qp.drawEllipse(x, y, r, r)

        self.is_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    ex.show()

    sys.exit(app.exec())
