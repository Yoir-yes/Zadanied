
import sys
import re

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ZapiszButton.clicked.connect(self.getUserdata)
        self.ui.ZapiszdoplikuButton.clicked.connect(self.addtofile)
        self.show()



    def getUserdata(self):

        imie = self.ui.ImieLine.text()
        naziwsko = self.ui.NazwiskoLine.text()
        pesel = self.ui.PeselLine.text()
        numbertl = self.ui.NumerLine.text()

        dane = imie+" "+naziwsko
        namefile = imie + '_' + naziwsko + ".txt"

        if re.match('[0-9]{11}$',pesel):
            self.ui.listWidget.addItem(dane)
        else:
            blad = QMessageBox()
            blad.setText("Pesel nie jest poprawny")
            blad.exec()

    def addtofile(self):
        imie = self.ui.ImieLine.text()
        naziwsko = self.ui.NazwiskoLine.text()
        pesel = self.ui.PeselLine.text()
        numbertl = self.ui.NumerLine.text()

        dane = imie + " " + naziwsko
        namefile = imie + '_' + naziwsko + ".txt"

        if re.match('[0-9]{11}$', pesel):
            with open(namefile, 'a') as file:
                file.write(dane + '\n')
        else:
            blad = QMessageBox()
            blad.setText("Pesel nie jest poprawny")
            blad.exec()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())