#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *

### Configuration parameters ###

height  = 18
opacity = 0.5
color   = "yellow"

################################

class MainWindow(QMainWindow):

  yoff=height/2
  toggle=False
  label=None

  def __init__(_, parent=None):
    super(MainWindow, _).__init__(parent)
    _.setFixedSize( QApplication.desktop().screenGeometry().width(), height )
    _.move( 0, 0 )
    _.setWindowOpacity( opacity )
    _.setWindowFlags( Qt.Window | Qt.FramelessWindowHint )
    _.setStyleSheet("background:" + color)

    _.label=QLabel("<b>Click</b> or press <b>CTRL</b> to hold.&nbsp; Press <b>Esc</b> to close")
    _.label.setAlignment(Qt.AlignCenter)
    _.label.setAttribute(Qt.WA_TransparentForMouseEvents)
    _.setCentralWidget(_.label)

  def updatePosition(_, evt):
    if _.toggle:
      p = evt.globalPos()
      if p:
        ny = p.y()-_.yoff
        if ny >= 0:
          _.move(0, ny)

  def toggleHold(_):
    _.toggle = not _.toggle
    _.centralWidget().setVisible( not _.centralWidget().isVisible() )

  def eventFilter(_, src, evt):
    if evt.type() == QEvent.MouseMove:
      _.updatePosition(evt)
    elif evt.type() == QEvent.MouseButtonPress:
      if evt.buttons() == Qt.LeftButton: _.toggleHold()
    elif evt.type() == QEvent.KeyRelease:
      if evt.key() == Qt.Key_Control: _.toggleHold()
      elif evt.key() == Qt.Key_Escape: QApplication.quit()
    return QWidget.eventFilter(_, src, evt)

if __name__ == "__main__":
  app = QApplication([])
  mw = MainWindow()
  mw.show()
  app.installEventFilter(mw)
  app.exec_()
