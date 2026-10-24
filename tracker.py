import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QProgressBar

goal = 2000
totalWater = 0
newGoal = 0

def create_celb():
    global goal
    new_goal = celb.text()
    if new_goal.isdigit() and int(new_goal) >= 0:
        goal = int(new_goal)
        celb.clear()
        update_display()

def addwater():
    global totalWater
    newValue = Line_water.text()
    if newValue.isdigit():
        totalWater += int(newValue)
        update_display()

def restart():
    global totalWater
    totalWater = 0
    update_display()

def update_display():
    global totalWater
    perscent = min(int((totalWater / goal)* 100), 100)
    Progress.setValue(perscent)
    stat.setText(f"выпито {totalWater}/{goal}")

app = QApplication(sys.argv)
window = QWidget()
QV = QVBoxLayout()
QH = QHBoxLayout()

celb = QLineEdit()
zadatbCelb = QPushButton("Задать цель")
zadatbCelb.clicked.connect(create_celb)
QH.addWidget(celb)
QH.addWidget(zadatbCelb)

QH2 = QHBoxLayout()
Line_water = QLineEdit()
Line_water.setPlaceholderText("например: 200")
add_water_button = QPushButton("Добавить")
add_water_button.clicked.connect(addwater)
QH2.addWidget(Line_water)
QH2.addWidget(add_water_button)
QV.addLayout(QH)
QV.addLayout(QH2)

Label = QLabel("Введите обьем воды(мл): ")
QV.addWidget(Label)

Progress = QProgressBar()
QV.addWidget(Progress)

stat = QLabel(f"выпито {0}/{0}")
QV.addWidget(stat)

sbros_stat = QPushButton("Сбросить статистику")
sbros_stat.clicked.connect(restart)
sbros_stat.clicked.connect(update_display)
QV.addWidget(sbros_stat)

window.setLayout(QV)

window.show()
app.exec()