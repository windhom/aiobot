import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTabWidget, QPushButton

app = QApplication(sys.argv)
window = QWidget()
Layout = QVBoxLayout()
window.setLayout(Layout)

tab_bar = QTabWidget()
Layout.addWidget(tab_bar)

hometab = QWidget()
homelab = QLabel("страница 1")
homeVB = QVBoxLayout()
homestr = QLabel("Жираф - высокий и пятнистый")
homeVB.addWidget(homelab)
homeVB.addWidget(homestr)
hometab.setLayout(homeVB)

tab_bar.addTab(hometab, "жираф")

hometab1 = QWidget()
homelab1 = QLabel("страница 2")
homeVB1 = QVBoxLayout()
homestr1 = QLabel("черепаха - зеленая, медленная и с панцирем")
homeVB1.addWidget(homelab1)
homeVB1.addWidget(homestr1)
hometab1.setLayout(homeVB1)

tab_bar.addTab(hometab1, "черепаха")

hometab2 = QWidget()
homelab2 = QLabel("страница 3")
homeVB2 = QVBoxLayout()
homestr2 = QLabel("кошка красивая")
homeVB2.addWidget(homelab2)
homeVB2.addWidget(homestr2)
hometab2.setLayout(homeVB2)

tab_bar.addTab(hometab2, "кошка")

window.show()
app.exec()