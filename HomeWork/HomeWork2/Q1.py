import sys
from PySide6.QtWidgets import *

class BasicBankingSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basic Banking System')
        self.setGeometry(100, 100, 400, 200)

        self.balance = 0

        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Welcome to Basic Banking System")
        vbox.addWidget(self.label)

        self.check_balance = QPushButton('Check Balance', self)
        self.check_balance.clicked.connect(self.open_balance_window)

        self.transaction = QPushButton('Make Transaction', self)
        self.transaction.clicked.connect(self.open_transaction_window)


        vbox.addWidget(self.check_balance)
        vbox.addWidget(self.transaction)

        self.setLayout(vbox)
        self.show()    


    def open_balance_window(self):
        dilog = QDialog(self)
        dilog.setWindowTitle("Check Balance")
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(f"Current Balance: ${self.balance:.2f}")
        layout.addWidget(label)
        close_bth = QPushButton('Close', self)
        close_bth.clicked.connect(dilog.close)
        layout.addWidget(close_bth)
        dilog.setLayout(layout)
        dilog.show()

    def open_transaction_window(self):
        dilog = QDialog(self)
        dilog.setWindowTitle("Make Transaction")
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Enter amount to deposit or withdraw:")
        layout.addWidget(label)
        self.amount_entry = QLineEdit(self)
        layout.addWidget(self.amount_entry)
        deposit_btn = QPushButton('Deposit', self)
        deposit_btn.clicked.connect(self.deposit)
        layout.addWidget(deposit_btn)
        withdraw_btn = QPushButton('Withdraw', self)
        withdraw_btn.clicked.connect(self.withdraw)
        layout.addWidget(withdraw_btn)
        close_bth = QPushButton('Close', self)
        close_bth.clicked.connect(dilog.close)
        layout.addWidget(close_bth)
        self.status_label = QLabel(self)
        layout.addWidget(self.status_label)
        dilog.setLayout(layout)
        dilog.show()

    def deposit(self):
        try:
            amount = float(self.amount_entry.text())
            self.balance += amount
            self.amount_entry.clear()
            self.status_label.setText(f"Deposited ${amount:.2f}")
        except:
            self.status_label.setText("Invalid amount")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.text())
            if amount > self.balance:
                self.status_label.setText("Insufficient balance")
            else:
                self.balance -= amount
                self.amount_entry.clear()
                self.status_label.setText(f"Withdrew ${amount:.2f}")
        except:
            self.status_label.setText("Invalid amount")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BasicBankingSystem()
    sys.exit(app.exec())