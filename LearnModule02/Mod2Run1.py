## Professor Reed demonstrates graphics for Math and Science, OETC 2014
## (just load and go--some errors maybe reported should be OK as-is)
## Graphics overview ONLY!!!
## fileid: mod3run1.py
####

##import initExample ## Add path to library (just for examples; you do not need this)

import numpy as np
import pyqtgraph as pg
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import time
import sys

"""
Display a plot and an image with minimal setup. 

pg.plot() and pg.image() are indended to be used from an interactive prompt
to allow easy data inspection (but note that PySide unfortunately does not
call the Qt event loop while the interactive prompt is running, in this case
it is necessary to call QApplication.exec_() to make the windows appear).
"""
def simplePlot():
    data = np.random.normal(size=1000)
    pg.plot(data, title="Simplest possible plotting example")

    data = np.random.normal(size=(500,500))
    pg.image(data, title="Simplest possible image example")

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if __name__ == '__main__':
        import sys
        if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
            pg.QtGui.QApplication.exec_()
            
# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""
##import initExample ## Add path to library (just for examples; you do not need this)

class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []
        rng = max(values)-min(values)
        #if rng < 120:
        #    return pg.AxisItem.tickStrings(self, values, scale, spacing)
        if rng < 3600*24:
            string = '%H:%M:%S'
            label1 = '%b %d -'
            label2 = ' %b %d, %Y'
        elif rng >= 3600*24 and rng < 3600*24*30:
            string = '%d'
            label1 = '%b - '
            label2 = '%b, %Y'
        elif rng >= 3600*24*30 and rng < 3600*24*30*24:
            string = '%b'
            label1 = '%Y -'
            label2 = ' %Y'
        elif rng >=3600*24*30*24:
            string = '%Y'
            label1 = ''
            label2 = ''
        for x in values:
            try:
                strns.append(time.strftime(string, time.localtime(x)))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')
        try:
            label = time.strftime(label1, time.localtime(min(values)))+time.strftime(label2, time.localtime(max(values)))
        except ValueError:
            label = ''
        #self.setLabel(text=label)
        return strns

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)

def makeFancyPlots():
    app = pg.mkQApp()

    axis = DateAxis(orientation='bottom')
    vb = CustomViewBox()

    pw = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False, title="PlotItem with custom axis and ViewBox<br>Menu disabled, mouse behavior changed: left-drag to zoom, right-click to reset zoom")
    dates = np.arange(8) * (3600*24*356)
    pw.plot(x=dates, y=[1,6,2,4,3,5,6,8], symbol='o')
    pw.show()
    pw.setWindowTitle('pyqtgraph example: customPlot')

    r = pg.PolyLineROI([(0,0), (10, 10)])
    pw.addItem(r)

# -*- coding: utf-8 -*-
"""
Example demonstrating a variety of scatter plot features.
"""

## Add path to library (just for examples; you do not need this)
##import initExample

##from pyqtgraph.Qt import QtGui, QtCore
##import pyqtgraph as pg
##import numpy as np

def makeMultiplePlots():
##    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
##        QtGui.QApplication.instance().exec_()
    app = QtGui.QApplication([])
    mw = QtGui.QMainWindow()
    mw.resize(800,800)
    view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
    mw.setCentralWidget(view)
    mw.show()
    mw.setWindowTitle('pyqtgraph example: ScatterPlot')

## create four areas to add plots
    w1 = view.addPlot()
    w2 = view.addViewBox()
    w2.setAspectLocked(True)
    view.nextRow()
    w3 = view.addPlot()
    w4 = view.addPlot()
    print("Generating data, this takes a few seconds...")

## There are a few different ways we can draw scatter plots; each is optimized for different types of data:


## 1) All spots identical and transform-invariant (top-left plot). 
## In this case we can get a huge performance boost by pre-rendering the spot 
## image and just drawing that image repeatedly.

    n = 300
    s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
    pos = np.random.normal(size=(2,n), scale=1e-5)
    spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
    s1.addPoints(spots)
    w1.addItem(s1)

## Make all plots clickable
    lastClicked = []
    def clicked(plot, points):
        global lastClicked
        for p in lastClicked:
            p.resetPen()
        print("clicked points", points)
        for p in points:
            p.setPen('b', width=2)
        lastClicked = points
    s1.sigClicked.connect(clicked)



## 2) Spots are transform-invariant, but not identical (top-right plot). 
## In this case, drawing is as fast as 1), but there is more startup overhead
## and memory usage since each spot generates its own pre-rendered image.

    s2 = pg.ScatterPlotItem(size=10, pen=pg.mkPen('w'), pxMode=True)
    pos = np.random.normal(size=(2,n), scale=1e-5)
    spots = [{'pos': pos[:,i], 'data': 1, 'brush':pg.intColor(i, n), 'symbol': i%5, 'size': 5+i/10.} for i in range(n)]
    s2.addPoints(spots)
    w2.addItem(s2)
    s2.sigClicked.connect(clicked)


## 3) Spots are not transform-invariant, not identical (bottom-left). 
## This is the slowest case, since all spots must be completely re-drawn 
## every time because their apparent transformation may have changed.

    s3 = pg.ScatterPlotItem(pxMode=False)   ## Set pxMode=False to allow spots to transform with the view
    spots3 = []
    for i in range(10):
        for j in range(10):
            spots3.append({'pos': (1e-6*i, 1e-6*j), 'size': 1e-6, 'pen': {'color': 'w', 'width': 2}, 'brush':pg.intColor(i*10+j, 100)})
    s3.addPoints(spots3)
    w3.addItem(s3)
    s3.sigClicked.connect(clicked)


## Test performance of large scatterplots

    s4 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 20))
    pos = np.random.normal(size=(2,10000), scale=1e-9)
    s4.addPoints(x=pos[0], y=pos[1])
    w4.addItem(s4)
    s4.sigClicked.connect(clicked)


## Start Qt event loop unless running in interactive mode or using pyside.
##if __name__ == '__main__':
##    import sys
##    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
##        QtGui.QApplication.instance().exec_()
####
# -*- coding: utf-8 -*-
"""
This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with 
the left/right mouse buttons. Right click on any plot to show a context menu.
"""

##import initExample ## Add path to library (just for examples; you do not need this)


##from pyqtgraph.Qt import QtGui, QtCore
##import numpy as np
##import pyqtgraph as pg

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))

p2 = win.addPlot(title="Multiple curves")
p2.plot(np.random.normal(size=100), pen=(255,0,0))
p2.plot(np.random.normal(size=100)+5, pen=(0,255,0))
p2.plot(np.random.normal(size=100)+10, pen=(0,0,255))

p3 = win.addPlot(title="Drawing with points")
p3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')


win.nextRow()

p4 = win.addPlot(title="Parametric, grid enabled")
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p4.plot(x, y)
p4.showGrid(x=True, y=True)

p5 = win.addPlot(title="Scatter plot, axis labels, log scale")
x = np.random.normal(size=1000) * 1e-5
y = x*1000 + 0.005 * np.random.normal(size=1000)
y -= y.min()-1.0
mask = x > 1e-15
x = x[mask]
y = y[mask]
p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
p5.setLabel('left', "Y Axis", units='A')
p5.setLabel('bottom', "Y Axis", units='s')
p5.setLogMode(x=True, y=False)

p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')
data = np.random.normal(size=(10,1000))
ptr = 0
def update():
    global curve, data, ptr, p6
    curve.setData(data[ptr%10])
    if ptr == 0:
        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


win.nextRow()

p7 = win.addPlot(title="Filled plot, axis disabled")
y = np.sin(np.linspace(0, 10, 1000)) + np.random.normal(size=1000, scale=0.1)
p7.plot(y, fillLevel=-0.3, brush=(50,50,200,100))
p7.showAxis('bottom', False)


x2 = np.linspace(-100, 100, 1000)
data2 = np.sin(x2) / x2
p8 = win.addPlot(title="Region Selection")
p8.plot(data2, pen=(255,255,255,200))
lr = pg.LinearRegionItem([400,700])
lr.setZValue(-10)
p8.addItem(lr)

p9 = win.addPlot(title="Zoom on selected region")
p9.plot(data2)
def updatePlot():
    p9.setXRange(*lr.getRegion(), padding=0)
def updateRegion():
    lr.setRegion(p9.getViewBox().viewRange()[0])
lr.sigRegionChanged.connect(updatePlot)
p9.sigXRangeChanged.connect(updateRegion)
updatePlot()

#### Start Qt event loop unless running in interactive mode or using pyside.
##if __name__ == '__main__':
##    import sys
##    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
##        QtGui.QApplication.instance().exec_()
    
####
def testOurGraphics():
##    simplePlot()
##    makeFancyPlots()
    makeMultiplePlots()
    
    
    
