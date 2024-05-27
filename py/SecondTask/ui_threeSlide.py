import math

from PySide2.QtWidgets import QMainWindow, QMessageBox

from py.PropertyFile.PropertySelection import PropertySelection
from py.SecondTask.ui_fourSlide import FourSlide
from ui.SecondTask.ui_threeSlide import Ui_MainWindow
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

class threeSlide(QMainWindow):
    def __init__(self):
        super(threeSlide, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QPixmap(u"image/secondTask/fourFormyla.png"))
        self.ui.pushButton.clicked.connect(self.continueTask)

    def continueTask(self):
        self.text = str(self.ui.lineEdit.text())
        P = PropertySelection()
        if not self.text:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText("Поле 'Ответ' должно быть заполнено!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
            return
        self.variant_number = int(P.get_Variant()) - 1

        R = float(self.ui.lineEdit_3.text().replace(",", "."))
        S0 = float(self.ui.lineEdit_2.text().replace(",", "."))

        R0 = 10 * math.log10(S0 / P.get_Sorg() * math.pow(10, 0.1 * float(R)))

        P.set_R(R)
        P.set_R0(R0)

        if round(R0, 2) == round(float(self.text.replace(",", ".")), 2):
            self.newWindow = FourSlide()
            self.newWindow.show()
            self.destroy()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText("Неверный ответ!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox