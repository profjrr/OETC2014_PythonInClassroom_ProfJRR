# -*- coding: utf-8 -*-
## Professor Reed sez: just load and go--no instructions needed!!
##
"""
Display an animated arrowhead following a curve.
This example uses the CurveArrow class, which is a combination
of ArrowItem and CurvePoint. 
"""

##import initExample ## Add path to library (just for examples; you do not need this)

import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([])

w = QtGui.QMainWindow()
cw = pg.GraphicsLayoutWidget()
w.show()
w.resize(400,600)
w.setCentralWidget(cw)
w.setWindowTitle('pyqtgraph example: Arrow')

p2 = cw.addPlot(row=1, col=0)

c = p2.plot(x=np.sin(np.linspace(0, 2*np.pi, 1000)), y=np.cos(np.linspace(0, 6*np.pi, 1000)))
a = pg.CurveArrow(c)
p2.addItem(a)

anim = a.makeAnimation(loop=-1)
anim.start()


