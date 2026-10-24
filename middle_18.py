import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

num = 0

def click():
    global num
    num += 1
    btn.setText(str(num))

app = QApplication(sys.argv)
window = QWidget()
QV = QVBoxLayout()

btn = QPushButton(str(num))
btn.clicked.connect(click)

QV.addWidget(btn)
window.setLayout(QV)
window.show()
app.exec()