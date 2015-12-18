import os
import sys

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication
from PyQt5.uic import loadUiType


os.chdir(os.path.join(os.path.dirname(__file__), 'ves'))
UI_MainWindow, QMainWindow = loadUiType('mainwindow.ui')

class Main(QMainWindow, UI_MainWindow):

    def __init__(self):

        super(Main, self).__init__()

        self.initUi()


    def initUi(self):
        saveAction = QAction(QIcon('save.png'), '&Save As', self)
        saveAction.setShortcut('Ctrl+S')

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Alt+F4')

        saveAction.triggered.connect(QApplication.saveStateRequest)
        exitAction.triggered.connect(QApplication.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Main()
    print(sorted(dir(main)))
    main.show()

    sys.exit(app.exec_())
