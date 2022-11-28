import sys
import smartphone_rekomender as cbr
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                            QPushButton, QWidget,QMainWindow, QLabel, 
                            QLineEdit, QDoubleSpinBox, QSpinBox,
                            QHBoxLayout, QComboBox)

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        custom_font = QFont()
        custom_font.setPointSize(12)
        QApplication.setFont(custom_font, "QLabel")
        QApplication.setFont(custom_font, "QGroupBox")
        QApplication.setFont(custom_font, "QPushButton")

        self.hlayout = QHBoxLayout()
        gridInput = QGridLayout()
        self.memory = self.createSpinBox('Memory', 2, 18, 2)
        self.internal_storage = self.createSpinBox('Internal Storage', 32, 1024, 32)
        self.os_price = self.createTextbox('Price')
        self.body_length = self.createSpinBox('Body Length', 138.4, 173.0, 0.1, checked = False, double = True)
        self.body_width = self.createSpinBox('Body Width', 67.3, 130.1, 0.1, checked = False, double = True)
        self.body_thickness = self.createSpinBox('Body Thickness', 6.3, 10.3, 0.1, checked = False, double = True)
        self.weight = self.createSpinBox('Weight', 144, 263, 1, checked = False)
        self.battery = self.createSpinBox('Battery', 2000, 7000, 100, checked = False)
        self.display_size = self.createSpinBox('Display Size', 4.7, 7.6, 0.1, checked = False, double = True)
        self.display_res = self.createSpinBox('Display Resolution', 720, 1800, 360, checked = False)
        self.refesh_rate = self.createSpinBox('Display Refesh Rate', 60, 180, 30, checked = False)
        self.display_type = self.createComboBox('Display Type', checked = False)
        self.feature = self.featureBox()
        gridInput.addWidget(self.memory, 0, 0)
        gridInput.addWidget(self.internal_storage, 1, 0)
        gridInput.addWidget(self.battery, 2, 0)
        gridInput.addWidget(self.body_length, 0, 1)
        gridInput.addWidget(self.body_width, 1, 1)
        gridInput.addWidget(self.body_thickness, 2, 1)
        gridInput.addWidget(self.weight, 3, 1)
        gridInput.addWidget(self.display_size, 0, 2)
        gridInput.addWidget(self.display_res, 1, 2)
        gridInput.addWidget(self.refesh_rate, 2, 2)
        gridInput.addWidget(self.display_type, 3, 2)
        gridInput.addWidget(self.os_price, 4, 0, 4, 3)
        gridInput.addWidget(self.feature, 8, 0, 8, 3)

        self.labelResult = QLabel()
        self.labelResult.setText('Top 5 Smartphone yang Direkomendasikan')
        self.pic1 = QLabel()
        self.label1 = QLabel()
        self.pic2 = QLabel()
        self.label2 = QLabel()
        self.pic3 = QLabel()
        self.label3 = QLabel()
        self.pic4 = QLabel()
        self.label4 = QLabel()
        self.pic5 = QLabel()
        self.label5 = QLabel()

        self.btnSearch = QPushButton('Cari')
        self.btnSearch.clicked.connect(self.onClickSearch)
        gridInput.addWidget(self.btnSearch, 16, 0, 16, 3)

        self.hlayout.addLayout(gridInput)
        self.setLayout(self.hlayout)

        self.setWindowTitle("Smartphone Rekomender 2022")

    def createSpinBox(self, label, min, max, interval, checked = True, double = False):
        groupBox = QGroupBox(label)
        checkbox = QCheckBox()

        if double:
            inputbox = QDoubleSpinBox()
        else:
            inputbox = QSpinBox()
        inputbox.setMinimum(min)
        inputbox.setMaximum(max)
        inputbox.setSingleStep(interval)

        checkbox.setChecked(checked)

        vbox = QGridLayout()
        vbox.addWidget(checkbox, 0, 0)
        vbox.addWidget(inputbox, 0, 1)
        vbox.columnStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def createTextbox(self, label, checked = True):
        groupBox = QGroupBox(label)
        checkbox = QCheckBox()

        inputbox = QLineEdit()
        inputbox.setText("1000")

        checkbox.setChecked(checked)

        vbox = QGridLayout()
        vbox.addWidget(checkbox, 0, 0)
        vbox.addWidget(inputbox, 0, 1)
        vbox.columnStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def createComboBox(self, label, checked = True):
        groupBox = QGroupBox(label)
        checkbox = QCheckBox()

        inputbox = QComboBox()
        inputbox.addItems(['IPS', 'OLED'])

        checkbox.setChecked(checked)

        vbox = QGridLayout()
        vbox.addWidget(checkbox, 0, 0)
        vbox.addWidget(inputbox, 0, 1)
        vbox.columnStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def featureBox(self):
        groupBox = QGroupBox('Feature')

        dual_sim = QCheckBox('Dual Sim')
        dual_sim.setChecked(True)
        esim = QCheckBox('eSim')
        memory_slot = QCheckBox('Memory Slot')
        fiveG = QCheckBox('5G')
        nfc = QCheckBox('NFC')
        nfc.setChecked(True)
        hdr = QCheckBox('HDR')

        vbox = QGridLayout()
        vbox.addWidget(dual_sim, 0, 0)
        vbox.addWidget(esim, 1, 0)
        vbox.addWidget(nfc, 0, 1)
        vbox.addWidget(fiveG, 1, 1)
        vbox.addWidget(memory_slot, 0, 2)
        vbox.addWidget(hdr, 1, 2)
        vbox.columnStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def onClickSearch(self):
        if self.memory.findChildren(QCheckBox)[0].isChecked():
            memory = self.memory.findChildren(QSpinBox)[0].value()
        else:
            memory = 0

        if self.internal_storage.findChildren(QCheckBox)[0].isChecked():
            internal_storage = self.internal_storage.findChildren(QSpinBox)[0].value()
        else:
            internal_storage = 0

        if self.os_price.findChildren(QCheckBox)[0].isChecked():
            os_price = int(self.os_price.findChildren(QLineEdit)[0].text())
        else:
            os_price = 0

        if self.feature.findChildren(QCheckBox)[0].isChecked():
            dual_sim = True
        else:
            dual_sim = 0

        if self.feature.findChildren(QCheckBox)[1].isChecked():
            esim = True
        else:
            esim = 0

        if self.feature.findChildren(QCheckBox)[2].isChecked():
            memory_slot = True
        else:
            memory_slot = 0

        if self.feature.findChildren(QCheckBox)[3].isChecked():
            fiveG = True
        else:
            fiveG = 0

        if self.feature.findChildren(QCheckBox)[4].isChecked():
            nfc = True
        else:
            nfc = 0

        if self.body_length.findChildren(QCheckBox)[0].isChecked():
            body_length = self.body_length.findChildren(QDoubleSpinBox)[0].value()
        else:
            body_length = 0

        if self.body_width.findChildren(QCheckBox)[0].isChecked():
            body_width = self.body_width.findChildren(QDoubleSpinBox)[0].value()
        else:
            body_width = 0

        if self.body_thickness.findChildren(QCheckBox)[0].isChecked():
            body_thickness = self.body_thickness.findChildren(QDoubleSpinBox)[0].value()
        else:
            body_thickness = 0

        if self.weight.findChildren(QCheckBox)[0].isChecked():
            weight = self.weight.findChildren(QSpinBox)[0].value()
        else:
            weight = 0

        if self.battery.findChildren(QCheckBox)[0].isChecked():
            battery = self.battery.findChildren(QSpinBox)[0].value()
        else:
            battery = 0

        if self.display_type.findChildren(QCheckBox)[0].isChecked():
            display_type = self.display_type.findChildren(QComboBox)[0].currentText()
        else:
            display_type = 0

        if self.display_size.findChildren(QCheckBox)[0].isChecked():
            display_size = self.display_size.findChildren(QDoubleSpinBox)[0].value()
        else:
            display_size = 0

        if self.display_res.findChildren(QCheckBox)[0].isChecked():
            display_res = self.display_res.findChildren(QSpinBox)[0].value()
        else:
            display_res = 0

        if self.refesh_rate.findChildren(QCheckBox)[0].isChecked():
            refesh_rate = self.refesh_rate.findChildren(QSpinBox)[0].value()
        else:
            refesh_rate = 0

        if self.feature.findChildren(QCheckBox)[5].isChecked():
            display_hdr = True
        else:
            display_hdr = 0

        top = cbr.run(memory, internal_storage, os_price, dual_sim, esim,
                        memory_slot, fiveG, nfc, body_length, body_width,
                        body_thickness, weight, battery, display_type, display_size,
                        display_res, refesh_rate, display_hdr)

        gridResult = QGridLayout()
        gridResult.setSpacing(20)

        gridResult.addWidget(self.labelResult, 0, 0, 1, 4, Qt.AlignCenter)
        gridResult.addWidget(self.pic1, 1, 0, 1, 2, Qt.AlignCenter)
        gridResult.addWidget(self.label1, 1, 1, 1, 4, Qt.AlignCenter)
        gridResult.addWidget(self.pic2, 3, 0, Qt.AlignCenter)
        gridResult.addWidget(self.label2, 4, 0, Qt.AlignCenter)
        gridResult.addWidget(self.pic3, 3, 1, Qt.AlignCenter)
        gridResult.addWidget(self.label3, 4, 1, Qt.AlignCenter)
        gridResult.addWidget(self.pic4, 3, 2, Qt.AlignCenter)
        gridResult.addWidget(self.label4, 4, 2, Qt.AlignCenter)
        gridResult.addWidget(self.pic5, 3, 3, Qt.AlignCenter)
        gridResult.addWidget(self.label5, 4, 3, Qt.AlignCenter)
        self.hlayout.addLayout(gridResult)

        self.pic1.setPixmap(QPixmap("photos/" + top['device'].iloc[0] + ".jpg"))
        self.label1.setText(top['device'].iloc[0])
        self.pic2.setPixmap(QPixmap("photos/" + top['device'].iloc[1] + ".jpg").scaledToWidth(80))
        self.label2.setText(top['device'].iloc[1])
        self.pic3.setPixmap(QPixmap("photos/" + top['device'].iloc[2] + ".jpg").scaledToWidth(80))
        self.label3.setText(top['device'].iloc[2])
        self.pic4.setPixmap(QPixmap("photos/" + top['device'].iloc[3] + ".jpg").scaledToWidth(80))
        self.label4.setText(top['device'].iloc[3])
        self.pic5.setPixmap(QPixmap("photos/" + top['device'].iloc[4] + ".jpg").scaledToWidth(80))
        self.label5.setText(top['device'].iloc[4])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())