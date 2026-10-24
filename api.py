import sys
import requests
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class PokeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Покемончики")
        self.resize(320, 240)

        
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(1.0)

        self.cry_url = None
        self.init_ui()
   
    def init_ui(self): 
        layout = QVBoxLayout()

        
        input_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя (например, pikachu)")
        self.search_btn = QPushButton("Найти")
        self.search_btn.clicked.connect(self.fetch_pokemon)
        
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.search_btn)
        layout.addLayout(input_layout)

       
        self.info_label = QLabel("Введите имя покемона на АНГЛИЙСКОМ")
        layout.addWidget(self.info_label)

        
        self.play_btn = QPushButton("Воспроизвести звук")
        self.play_btn.setEnabled(False)
        self.play_btn.clicked.connect(self.play_sound)
        layout.addWidget(self.play_btn)

        self.setLayout(layout)
       
    def fetch_pokemon(self):
        name = self.name_input.text().strip().lower()
        if not name:
            return

        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                poke_name = data["name"].capitalize()
                poke_weight = data["weight"]
                poke_height = data["height"]
                poke_ability = data["abilities"][0]["ability"]["name"]

                self.info_label.setText(
                    f"<b>{poke_name}</b><br>Рост: {poke_height}<br>Вес: {poke_weight} <br>Способность: {poke_ability}</br>"
                )

                
                self.cry_url = data.get("cries", {}).get("latest")
                if self.cry_url:
                    self.play_btn.setEnabled(True)
                    self.play_sound()  
                else:
                    self.play_btn.setEnabled(False)
            else:
                self.info_label.setText("Покемон не найден.")
                self.play_btn.setEnabled(False)
        except requests.exceptions.RequestException:
                self.info_label.setText("Ошибка сети.")
    def play_sound(self):
        if self.cry_url:
            self.player.setSource(QUrl(self.cry_url))
            self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokeApp()
    window.show()
    sys.exit(app.exec())