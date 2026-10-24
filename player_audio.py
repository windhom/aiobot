import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtGui import QPixmap

def installSong():
    file, _ = QFileDialog.getOpenFileName(
        window, # Родительский виджет
        "Загрузить трек", # Заголовок диалогового окна
        "", # начальная папка открытия
        "Audio Files (*.mp3)" # фильтр типов файлов
    )
    print(_)
    if file:
        track_name = file.split('/')[-1]
        track_list.addItem(track_name)
        track_paths.append(file)

def stopSong():
    media_player.stop()

def pauseSong():
    media_player.pause()

def nazad():
    media_player.setPosition(media_player.position() - 5000)

def vpered():
    media_player.setPosition(media_player.position() + 5000)

def playSong():
    selected_index = track_list.currentRow()

    if selected_index >= 0:
        file_path = track_paths[selected_index]
        media_player.setSource(QUrl.fromLocalFile(file_path))
        media_player.play()

app = QApplication(sys.argv)
window = QWidget()
window.resize(700, 400)
QV = QVBoxLayout()
QH = QHBoxLayout()
audio_output = QAudioOutput()
media_player = QMediaPlayer()
media_player.setAudioOutput(audio_output)
track_list = QListWidget()
track_paths = []

InstSong = QPushButton("Загрузить трек")
InstSong.clicked.connect(installSong)
Nazad = QPushButton("\u23EA")
Nazad.clicked.connect(nazad)
PauseSong = QPushButton("\u23F8")
PauseSong.clicked.connect(pauseSong)
Vpered = QPushButton("\u23E9")
Vpered.clicked.connect(vpered)
StopSong = QPushButton("Остановить")
StopSong.clicked.connect(stopSong)
PlaySong = QPushButton("Воспроизвести")
PlaySong.clicked.connect(playSong)

QV.addWidget(InstSong)
QV.addWidget(track_list)
QH.addWidget(Nazad)
QH.addWidget(PauseSong)
QH.addWidget(Vpered)
QV.addLayout(QH)
QV.addWidget(StopSong)
QV.addWidget(PlaySong)
window.setLayout(QV)

window.show()
app.exec()