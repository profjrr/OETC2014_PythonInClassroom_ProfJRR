## Professor Reed demonstrates "simpleplot2" -- January OETC 2014
## Python Programming in Your Classroom
## for Python 3.3 or better
## Modifed (Dec.14th, 2013) by ProfJRR into separate functions.
##
## runSimplePlot() -- for testing and evaluation
##
"""
Display a plot and an image with minimal setup. 

pg.plot() and pg.image() are indended to be used from an interactive prompt
to allow easy data inspection (but note that PySide unfortunately does not
call the Qt event loop while the interactive prompt is running, in this case
it is necessary to call QApplication.exec_() to make the windows appear).
"""
##import initExample ## Add path to library (just for examples; you do not need this)

import sys
import numpy as np
import pyqtgraph as pg

## Start Qt event loop unless running in interactive mode or using pyside.
def simplePlot():
    data = np.random.normal(size=1000)
    pg.plot(data, title="Simplest possible plotting example")

    data = np.random.normal(size=(500,500))
    pg.image(data, title="Simplest possible image example")
    pg.QtGui.QApplication.exec_()
##
#### Run or Test your SimplePlot routine ###
def testSimplePlot():
    simplePlot()
#### end of main function for Simpleplot2 ###
    
