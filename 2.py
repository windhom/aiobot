from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

# Инициализация приложения
app = QApplication(sys.argv)


# Создание окна
window = QWidget()
window.setWindowTitle('Обработка событий мыши')


# Функция для обработки прокрутки колесика мыши
def handle_wheel_event(event):
    delta_y = event.angleDelta().y()  # получаем вертикальное смещение
    if delta_y > 0:
        print("Колесико прокручено вверх")
    elif delta_y < 0:
        print("Колесико прокручено вниз")


# Устанавливаем обработчик событий прокрутки колесика мыши
window.wheelEvent = handle_wheel_event

def handle_mouse_press(event):
    if event.button() == Qt.MouseButton.LeftButton:
        print("Левая кнопка")

# window.mousePressEvent = handle_mouse_press


window.mouseDoubleClickEvent = handle_mouse_press



# Показываем окно
window.show()


# Цикл обработки событий
app.exec()