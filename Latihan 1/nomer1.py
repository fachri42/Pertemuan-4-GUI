import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
class nomer1(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500,200)
        self.move(400,400)
        self.setWindowTitle('Praktikum Pemrograman GUI')

        self.label1 = QLabel('Dosen Pengampu')
        self.label1.move(100,40)
        self.label1.setParent(self)

        self.label2 = QLabel('Afandi Nur Aziz Thohari, S.T.,M.Cs')
        self.label2.move(100,60)
        self.label2.setParent(self)

        self.label3 = QLabel('Copyright @2019')
        self.label3.move(200,180)
        self.label3.setParent(self)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    minform = nomer1()
    minform.show()
    a.exec_()