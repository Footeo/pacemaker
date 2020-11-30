from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import settings 

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        Time = [1,2,3,4,5,6,7,8,9,10]  #seconds
        Amplitude = [0,0,1,5,-1,-0.5,-.25,0,0,0]  #Ex Voltage

        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(Time, Amplitude, pen=pen)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()