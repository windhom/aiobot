import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTabWidget, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
Layout = QVBoxLayout()
window.setLayout(Layout)

tab_bar = QTabWidget()
Layout.addWidget(tab_bar)

regtab = QWidget()
reglab_name = QLabel("name:")
reg_name = QLineEdit()
reglab_email = QLabel("email:")
reg_email = QLineEdit()
reglab_pass = QLabel("password:")
reg_pass = QLineEdit()
button = QPushButton("Зарегестрироваться")
regHB = QVBoxLayout()
regHB.addWidget(reglab_name)
regHB.addWidget(reg_name)
regHB.addWidget(reglab_email)
regHB.addWidget(reg_email)
regHB.addWidget(reglab_pass)
regHB.addWidget(reg_pass)
regHB.addWidget(button)
regtab.setLayout(regHB)

tab_bar.addTab(regtab, "Регистрация")

vhodtab = QWidget()
vhodlab_name = QLabel("name:")
vhod_name = QLineEdit()
vhodlab_pass = QLabel("password:")
vhod_pass = QLineEdit()
btn = QPushButton("Войти")
vhodHB = QVBoxLayout()
vhodHB.addWidget(vhodlab_name)
vhodHB.addWidget(vhod_name)
vhodHB.addWidget(vhodlab_pass)
vhodHB.addWidget(vhod_pass)
vhodHB.addWidget(btn)
vhodtab.setLayout(vhodHB)

tab_bar.addTab(vhodtab, "Вход")

window.show()
app.exec()