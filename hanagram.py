#main controller of the program.
import os
import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollBar

from permutation import Permutation

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
hanagram_ui = uic.loadUiType(BASE_DIR + r'\hanagram.ui')[0]

class WorkThread(QThread):
  send_status_signal = pyqtSignal(bool)
  before_thread = pyqtSignal()
  after_thread = pyqtSignal()

  def __init__(self, func, name = 'Default_Thread'):
    super().__init__(self)
    self.func = func
    self.name = name

  def run(self):
    self.send_status_signal.emit(True)
    self.before_thread.emit()
    self.func()
    self.send_status_signal.emit(False)
    self.after_thread.emit()

class HanagramWindow(QMainWindow, hanagram_ui):
  def __init__(self, QApplication):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('hanagram ver 0.0.5')

    self.permut = Permutation()
    self.string = ''
    self.res = []

    self.pushButton.clicked.connect(self._clicked_button)
    self.pushButton_Shuffle.clicked.connect(self._clicked_shuffle_button)
    self.lineEdit.textEdited.connect(lambda: self._edited_line_text(self.lineEdit.text()))
  
  def _clicked_button(self):
    self.res = self.permut.get_permutation_result(self.string)
    self._update_textedit()

  def _clicked_shuffle_button(self):
    if self.res == []: return
    random.shuffle(self.res)
    self._update_textedit()
  
  def _edited_line_text(self, text):
    self.string = text

  def _update_textedit(self):
    self.textBrowser.clear()
    for res_string in self.res:
      self.textBrowser.append(res_string)
    self.textBrowser.verticalScrollBar().triggerAction(QScrollBar.SliderToMinimum)
    

if __name__=='__main__':
  app = QApplication(sys.argv)
  win = HanagramWindow(app)
  win.show()
  sys.exit(app.exec_())