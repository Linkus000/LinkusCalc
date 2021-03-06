import sys
from mathfunctions import toBinary, toTernary
from PyQt4 import QtGui
from math import sqrt

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.wie=4
    def initUI(self):

        inw=QtGui.QLineEdit(self)
        inw.move(130,80)
        self.lbl=QtGui.QLabel(self)
        self.lbl.move(130,120)
        inw.textChanged[str].connect(self.onInput)
        combo = QtGui.QComboBox(self)
        combo.move(10, 80)
        combo.addItem("toBinary")
        combo.addItem("toTernary")
        combo.addItem("fromBinary")
        combo.addItem("fromTernary")
        combo.activated[str].connect(self.onTypeSwitch)
        self.setWindowTitle("Very simple GUI 2,3 <--> 10 integer base converter")
        self.resize(400, 230)
        self.center()
        self.show()
    def onTypeSwitch(self, item):
        if item=='fromBinary': self.wie=2
        elif item=='fromTernary': self.wie=3
        elif item=='toBinary': self.wie=4
        else: self.wie=5
    def onInput(self, text):
        try:
            if text=='': self.lbl.setText('')
            elif self.wie==4: self.lbl.setText(toBinary(text))
            elif self.wie==5: self.lbl.setText(toTernary(text))
            else: self.lbl.setText(str(int(text, self.wie)))
        except ValueError:
            self.lbl.setText("Value Error!")
        self.lbl.adjustSize()
    def center(self):
        qr=self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app=QtGui.QApplication(sys.argv)
    GUI=Example()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
