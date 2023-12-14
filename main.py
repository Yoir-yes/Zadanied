
import sys
import re

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ZapiszButton.clicked.connect(self.addtolist)
        self.ui.ZapiszdoplikuButton.clicked.connect(self.addtofile)
        self.show()



    def getUserdata(self):

        imie = self.ui.ImieLine.text()
        naziwsko = self.ui.NazwiskoLine.text()
        pesel = self.ui.PeselLine.text()
        numbertl = self.ui.NumerLine.text()

        dane = imie+" "+naziwsko

        def check_pesel(pesel):
            if (re.match('[0-9]{11}$', pesel)):
                pass
            else:
                return 0
            l = int(pesel[10])
            suma = ((l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (
                (l * int(pesel[4]))) + (3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (
                            l * int(pesel[8])) + (3 * int(pesel[9])))
            kontrolka = 10 - (suma % 10)
            if kontrolka == 10:
                kontrolka = 0
            else:
                kontrolka = kontrolka

            if ((kontrolka == 10) or (kontrolka == 0)):
                return False
            else:
                return True

        if check_pesel(pesel):
            return {'imie': imie, 'nazwisko': naziwsko, 'pesel':pesel, 'numertf' : numbertl}
        else:
            blad = QMessageBox()
            blad.setText("Pesel nie jest poprawny")
            blad.exec()

    def addtolist(self):
        dane = self.getUserdata()
        fullname = dane['imie'] + " " + dane['nazwisko']
        self.ui.listWidget.addItem(fullname)

    def addtofile(self):
        dane = self.getUserdata()
        fullname = dane['imie'] + " " + dane['nazwisko']
        filename = dane['imie'] + "_" + dane['nazwisko']+'.txt'
        with open(filename, 'a') as file:
            file.write(fullname + '\n')

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())