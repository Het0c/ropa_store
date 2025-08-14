# main.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QLineEdit, QMessageBox
)
from db.database import init_db, registrar_venta, get_prenda
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

init_db()


class RopaStore(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧵 RopaStore - Inventario")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #1e1e1e; color: #f0f0f0;")
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        # Menú lateral
        menu = QVBoxLayout()
        menu.setAlignment(Qt.AlignTop)

        btn_inventario = QPushButton("Inventario")
        btn_ventas = QPushButton("Registrar Venta")
        btn_reportes = QPushButton("Reportes")

        for btn in [btn_inventario, btn_ventas, btn_reportes]:
            btn.setStyleSheet("background-color: #333; padding: 10px; font-size: 14px;")
            menu.addWidget(btn)

        # Tabla de inventario
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Código", "Nombre", "Talla", "Stock", "Precio"])
        self.table.setStyleSheet("background-color: #2e2e2e; font-size: 13px;")
        self.load_sample_data()

        # Panel derecho
        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("Inventario de Prendas"))
        right_panel.addWidget(self.table)

        # Campo de escaneo simulado
        self.scan_input = QLineEdit()
        self.scan_input.setPlaceholderText("Escanea o ingresa código de prenda...")
        self.scan_input.returnPressed.connect(self.registrar_venta)
        right_panel.addWidget(self.scan_input)

        layout.addLayout(menu, 1)
        layout.addLayout(right_panel, 4)
        self.setLayout(layout)

    def load_sample_data(self):
        sample = [
            ["1234567890123", "Polera Negra", "M", "25", "$9.990"],
            ["9876543210987", "Jeans Azul", "L", "12", "$14.990"],
            ["4567891234567", "Chaqueta Cuero", "XL", "5", "$29.990"]
        ]
        self.table.setRowCount(len(sample))
        for row, item in enumerate(sample):
            for col, value in enumerate(item):
                self.table.setItem(row, col, QTableWidgetItem(value))

    registrar_venta = registrar_venta
    # def registrodeventa(self):
    #     code = self.scan_input.text()
    #     found = False
    #     for row in range(self.table.rowCount()):
    #         if self.table.item(row, 0).text() == code:
    #             stock = int(self.table.item(row, 3).text())
    #             if stock > 0:
    #                 self.table.setItem(row, 3, QTableWidgetItem(str(stock - 1)))
    #                 QMessageBox.information(self, "Venta registrada", f"Venta de {self.table.item(row,1).text()} registrada.")
    #             else:
    #                 QMessageBox.warning(self, "Sin stock", "Esta prenda está agotada.")
    #             found = True
    #             break
    #     if not found:
    #         QMessageBox.warning(self, "No encontrado", "Código no corresponde a ninguna prenda.")
    #     self.scan_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RopaStore()
    window.show()
    sys.exit(app.exec_())
