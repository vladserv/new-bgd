import math

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QMessageBox

from data.data import tab_в, tab_г, tab_1
from py.PropertyFile.PropertySelection import PropertySelection
from py.SecondTask.ui_secondSlide import secondSlide
from ui.SecondTask.ui_firstSlide import Ui_MainWindow
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

class FirstSlide(QMainWindow):
    variant_number: str
    text: str

    def __init__(self):
        super(FirstSlide, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QPixmap(u"../../image/secondTask/firstFormyla.png"))
        self.ui.pushButton.clicked.connect(self.continueTask)
        self.ui.comboBox_2.currentIndexChanged.connect(self.on_combobox_changed)

    @Slot(int)
    def on_combobox_changed(self, index):
        P = PropertySelection()
        selected_value = self.ui.comboBox_2.currentIndex()
        if selected_value == 0: return
        self.ui.label_7.setText(str(tab_1[int(P.get_Gerts())][selected_value - 1]))

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

        # Используйте .iloc[] для доступа к данным с использованием числовых индексов столбцов
        value = tab_в[int(P.get_Gerts())][self.variant_number + 1]  # Длина соответствующая частоте variant_number]

        # Используйте .iloc[] для доступа к данным с использованием числовых индексов столбцов
        length = tab_г.iloc[0, self.variant_number]  # Длина соответствующая частоте variant_numberant_number
        height = tab_г.iloc[1, self.variant_number]  # Высота соответствующая частоте variant_number
        Rtr = value - int(self.ui.label_7.text()) - 10 * math.log10(round(P.get_B(), 2)) + 10 * math.log10(length * height)

        if round(Rtr, 2) == round(float(self.text.replace(",", ".")), 2):
            self.newWindow = secondSlide()
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