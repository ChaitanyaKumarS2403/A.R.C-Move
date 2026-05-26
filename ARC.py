import sys
import time
import pyautogui
from PyQt6.QtCore import Qt, QThread, QUrl
from PyQt6.QtGui import QIcon  # Added for icon support
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

# --- Worker Thread (Core Logic - Unaltered) ---
class MovementThread(QThread):
    def run(self):
        pyautogui.FAILSAFE = True
        while True:
            x, y = pyautogui.position()
            # Original movement logic
            pyautogui.dragTo(x + 2, y, duration=0.2)
            pyautogui.dragTo(x, y, duration=0.2)
            
            time.sleep(30)

# --- GUI Window ---
class ARC(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A.R.C Move")
        
        # 1. Set the Window Icon (Grabs 1st frame of Icon.gif)
        self.setWindowIcon(QIcon("HUD.png"))
        
        # 2. Set window size to roughly fill the screen (80%)
        screen = QApplication.primaryScreen().geometry()
        width = int(screen.width() * 0.8)
        height = int(screen.height() * 0.8)
        self.resize(width, height)
        
        # Center the window
        self.move(int((screen.width() - width) / 2), int((screen.height() - height) / 2))

        # 3. Setup Video Player
        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        
        # Video path as requested
        video_path = QUrl("https://github.com/ChaitanyaKumarS2403/assets/releases/download/ctOS/ctOS_Loading.mp4")
        self.media_player.setSource(video_path)

        # Loop configuration
        self.media_player.setLoops(-1) 

        # 4. Layout (No margins, no text)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.video_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 5. Initialize Background Process
        self.worker = MovementThread()
        self.worker.start()

        # Start Playback
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ARC()
    window.show()
    sys.exit(app.exec())
