import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile("Pizzeria.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Access UI elements using self.ui.<element_name>
        self.ui.pbExit.clicked.connect(self.bye)
        self.ui.rbSmall.toggled.connect(self.CalculatePrice)
        self.ui.rbMedium.toggled.connect(self.CalculatePrice)
        self.ui.rbLarge.toggled.connect(self.CalculatePrice)
        self.ui.cbBeef.stateChanged.connect(self.CalculatePrice)
        self.ui.cbBellPepper.stateChanged.connect(self.CalculatePrice)
        self.ui.cbChicken.stateChanged.connect(self.CalculatePrice)
        self.ui.cbMushroom.stateChanged.connect(self.CalculatePrice)
        self.ui.cbOnion.stateChanged.connect(self.CalculatePrice)
        self.ui.cbPepperoni.stateChanged.connect(self.CalculatePrice)
        self.ui.cbPork.stateChanged.connect(self.CalculatePrice)
        self.ui.cbTomato.stateChanged.connect(self.CalculatePrice)
        self.ui.pbOrder.clicked.connect(self.Message)

    def bye(self):
        self.close()

    def CalculatePrice(self):
        price = 0
        if self.ui.rbSmall.isChecked():
            price += 5
        elif self.ui.rbMedium.isChecked():
            price += 10
        elif self.ui.rbLarge.isChecked():
            price += 15

        if self.ui.cbBeef.isChecked():
            price += 4
        if self.ui.cbBellPepper.isChecked():
            price += 1
        if self.ui.cbChicken.isChecked():
            price += 2
        if self.ui.cbMushroom.isChecked():
            price += 1
        if self.ui.cbOnion.isChecked():
            price += 1
        if self.ui.cbPepperoni.isChecked():
            price += 4
        if self.ui.cbPork.isChecked():
            price += 3
        if self.ui.cbTomato.isChecked():
            price += 1

        self.ui.lePrice.setText(f"{price:.2f}")
        salesTax = float(price) * 0.09
        self.ui.leSalesTax.setText(f"{salesTax:.2f}")
        Total = f"{(salesTax + float(price)):.2f}"
        self.ui.leTotal.setText(Total)
        return Total

    def Message(self):
        Total = self.CalculatePrice()
        Note = (
            "Dear Customer,\n\nPlease pay $"
            + Total
            + " at cashier and wait for your delicious pizza.\n\n"
            + "Thanks for your business and have a nice day!\n\n"
            + "Pizzaria Management"
        )
        QMessageBox.about(self, "Pizzaria", Note)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
