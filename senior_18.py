import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QPushButton

buttons = ['1', '2', '3', '/',
           '4', '5', '6', '*',
           '7', '8', '9', '-',
           '0', 'C', '=', '+']

app = QApplication(sys.argv)
window = QWidget()
Vvod = QLineEdit()
layout = QVBoxLayout()
window.setLayout(layout)

layout.addWidget(Vvod)

grid = QGridLayout()

row = 0
col = 0

for btnText in buttons:
    btn = QPushButton(btnText)
    grid.addWidget(btn, row, col)

    col += 1
    if col > 3:
        col = 0
        row += 1

layout.addLayout(grid)

window.show()
app.exec()