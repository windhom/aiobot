import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

app = QApplication(sys.argv)
Label = QLabel()

photo = QPixmap("IMG.PNG")
photo = photo.scaled(200, 200)
Label.setPixmap(photo)

Label.show()
app.exec()