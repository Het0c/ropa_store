import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)

class RopaStore(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venta de Ropa - RopaStore")
        self.setGeometry(100, 100, 700, 400)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Formulario de producto
        form_layout = QHBoxLayout()
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre de la prenda")
        self.talla_input = QLineEdit()
        self.talla_input.setPlaceholderText("Talla")
        self.precio_input = QLineEdit()
        self.precio_input.setPlaceholderText("Precio")
        self.cantidad_input = QLineEdit()
        self.cantidad_input.setPlaceholderText("Cantidad")
        form_layout.addWidget(QLabel("Nombre:"))
        form_layout.addWidget(self.nombre_input)
        form_layout.addWidget(QLabel("Talla:"))
        form_layout.addWidget(self.talla_input)
        form_layout.addWidget(QLabel("Precio:"))
        form_layout.addWidget(self.precio_input)
        form_layout.addWidget(QLabel("Cantidad:"))
        form_layout.addWidget(self.cantidad_input)
        layout.addLayout(form_layout)

        # Botón para agregar producto
        self.agregar_btn = QPushButton("Agregar Producto")
        self.agregar_btn.clicked.connect(self.agregar_producto)
        layout.addWidget(self.agregar_btn)

        # Tabla de productos
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Talla", "Precio", "Cantidad"])
        layout.addWidget(self.tabla)

        # Botón para vender producto
        self.vender_btn = QPushButton("Vender Producto Seleccionado")
        self.vender_btn.clicked.connect(self.vender_producto)
        layout.addWidget(self.vender_btn)

        central_widget.setLayout(layout)

    def agregar_producto(self):
        nombre = self.nombre_input.text()
        talla = self.talla_input.text()
        precio = self.precio_input.text()
        cantidad = self.cantidad_input.text()

        if not nombre or not talla or not precio or not cantidad:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio debe ser número y cantidad debe ser entero.")
            return

        row = self.tabla.rowCount()
        self.tabla.insertRow(row)
        self.tabla.setItem(row, 0, QTableWidgetItem(nombre))
        self.tabla.setItem(row, 1, QTableWidgetItem(talla))
        self.tabla.setItem(row, 2, QTableWidgetItem(f"{precio:.2f}"))
        self.tabla.setItem(row, 3, QTableWidgetItem(str(cantidad)))

        self.nombre_input.clear()
        self.talla_input.clear()
        self.precio_input.clear()
        self.cantidad_input.clear()

    def vender_producto(self):
        selected = self.tabla.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione un producto para vender.")
            return

        cantidad_item = self.tabla.item(selected, 3)
        cantidad = int(cantidad_item.text())
        if cantidad > 0:
            cantidad -= 1
            self.tabla.setItem(selected, 3, QTableWidgetItem(str(cantidad)))
            QMessageBox.information(self, "Venta", "Producto vendido exitosamente.")
        else:
            QMessageBox.warning(self, "Sin stock", "No hay stock disponible para este producto.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RopaStore()
    window.show()
    sys.exit(app.exec_())