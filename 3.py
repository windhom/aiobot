# Импорты
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


# Инициализация приложения
app = QApplication(sys.argv)


# Создание окна
window = QWidget()
window.setWindowTitle("Обработка отпускания клавиш")


# Функция для обработки отпускания клавиш
def handle_key_release(event):
    # Проверяем, какая именно клавиша была отпущена
    if event.key() == Qt.Key.Key_W:
        print("Отпущена клавиша W")
    elif event.key() == Qt.Key.Key_A:
        print("Отпущена клавиша A")
    elif event.key() == Qt.Key.Key_S:
        print("Отпущена клавиша S")
    elif event.key() == Qt.Key.Key_D:
        print("Отпущена клавиша D")
    elif event.key() == Qt.Key.Key_1:
        print("Отпущена кнопка 1")


# Присваиваем обработчик событий отпускания клавиш
window.keyPressEvent = handle_key_release


# Показываем окно
window.show()


# Цикл обработки событий
app.exec()