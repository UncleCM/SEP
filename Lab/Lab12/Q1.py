import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel
from datetime import date as Date

class BookingSystem:
    def __init__(self):
        self.bookings = []
        self.observers = []
        self.counter = 1

    def addBooking(self, date):
        self.bookings.append((date, f"Booking {self.counter}"))
        self.counter += 1
        self.notifyObservers()

    def searchBooking(self, date):
        return [booking for booking in self.bookings if booking[0] == date]

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.bookings)

class BookingObserver:
    def update(self, bookings):
        pass

class StaffUi(BookingObserver):
    def __init__(self, s, name):
        self.name = name
        self.system = s

    def update(self, bookings):
        print(self.name + ":StaffUi.update():")
        print("-- Booking Data --")
        for date, description in bookings:
            print(f"{date} : {description}")

    def submit(self, date):
        self.system.display(date)

class MainWindow(QMainWindow):
    def __init__(self, booking_system):
        super().__init__()
        self.booking_system = booking_system
        self.initUI()
        self.addDefaultBookings()

    def initUI(self):
        self.setWindowTitle('Booking System')
        self.setGeometry(100, 100, 400, 300)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.page1 = QWidget()
        self.page2 = QWidget()

        self.initPage1()
        self.initPage2()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

    def initPage1(self):
        layout = QVBoxLayout()

        self.booking_list = QListWidget()
        self.updateBookingList()

        select_button = QPushButton('Search Booking')
        select_button.clicked.connect(self.showPage2)

        layout.addWidget(self.booking_list)
        layout.addWidget(select_button)

        self.page1.setLayout(layout)

    def initPage2(self):
        layout = QVBoxLayout()

        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText('Date (DD)')
        self.month_input = QLineEdit()
        self.month_input.setPlaceholderText('Month (MM)')
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText('Year (YYYY)')

        search_button = QPushButton('Search Booking')
        search_button.clicked.connect(self.searchBooking)

        layout.addWidget(QLabel('Search Booking'))
        layout.addWidget(self.date_input)
        layout.addWidget(self.month_input)
        layout.addWidget(self.year_input)
        layout.addWidget(search_button)

        self.page2.setLayout(layout)

    def showPage2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def searchBooking(self):
        day = int(self.date_input.text())
        month = int(self.month_input.text())
        year = int(self.year_input.text())

        search_date = Date(year, month, day)
        bookings = self.booking_system.searchBooking(search_date)
        self.booking_list.clear()
        if bookings:
            for booking in bookings:
                self.booking_list.addItem(f"{booking[0]} : {booking[1]}")
        else:
            self.booking_list.addItem(f"No bookings found on {search_date}")
        self.stacked_widget.setCurrentWidget(self.page1)

    def updateBookingList(self):
        self.booking_list.clear()
        for booking in self.booking_system.bookings:
            self.booking_list.addItem(f"{booking[0]} : {booking[1]}")

    def addDefaultBookings(self):
        self.booking_system.addBooking(Date(2011, 9, 1))
        self.booking_system.addBooking(Date(2011, 10, 1))
        self.booking_system.addBooking(Date(2011, 10, 1))
        self.booking_system.addBooking(Date(2011, 11, 1))
        self.booking_system.addBooking(Date(2011, 12, 1))
        self.updateBookingList()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    booking_system = BookingSystem()
    main_window = MainWindow(booking_system)

    ui1 = StaffUi(booking_system, "Ui#1")
    booking_system.addObserver(ui1)

    main_window.show()
    sys.exit(app.exec_())