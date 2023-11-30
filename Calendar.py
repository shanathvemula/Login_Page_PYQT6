from PyQt5 import QtWidgets, QtCore


class CalendarPicker(QtWidgets.QDialog):
    pick_date = QtCore.pyqtSignal(QtCore.QDate)

    def __init__(self, parent=None):
        super(CalendarPicker, self).__init__(parent)

        self.setWindowTitle("Pick a date")

        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.clicked.connect(self.get_date)

        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.calendar)

    def get_date(self, date):
        self.pick_date.emit(date)
        self.close()


class Calendar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)

        self.date_edit = QtWidgets.QLineEdit(self)
        self.date_edit.setPlaceholderText("Select the date")
        self.date_edit.setReadOnly(True)

        self.date_picker = QtWidgets.QPushButton("...", self)
        self.date_picker.clicked.connect(self.open_calendar)

        # self.test_edit = QtWidgets.QLineEdit(self)

        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.date_edit)
        layout.addWidget(self.date_picker)
        # layout.addWidget(self.test_edit)

    def open_calendar(self):
        calendar_dialog = CalendarPicker(self)
        calendar_dialog.pick_date.connect(self.update_date)
        calendar_dialog.exec()

    def update_date(self, date):
        # print(dir(date))
        self.date_edit.setText(date.toString())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    gui = Calendar()
    gui.show()
    app.exec()
