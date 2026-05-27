"""
A.R.C Move (Automated Realtime Cursor Movement)
----------------------------------------------
A futuristic utility that simulates physical mouse movement to maintain 
system activity, wrapped in an immersive JARVIS/ctOS-themed HUD.

Main Logic:
1. Multi-threaded Execution: Separates cursor movement from GUI rendering.
2. Cloud-Asset Streaming: Loads high-definition HUD video via GitHub Releases.
3. Interactive HUD: Fullscreen toggle and automated failsafes.
"""

import sys
import time
import pyautogui
from PyQt6.QtCore import Qt, QThread, QUrl
from PyQt6.QtGui import QIcon 
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class MovementThread(QThread):
    """
    Handles the cursor automation logic in a separate background thread.
    
    This ensures that the 'while True' loop and 'time.sleep' do not 
    block the main GUI thread, keeping the video playback smooth.
    """
    def run(self):
        """Executes the automated cursor movement cycle."""
        # PyAutoGUI Failsafe: Move mouse to any corner of the screen to abort.
        pyautogui.FAILSAFE = True
        
        while True:
            # Capture current mouse coordinates
            x, y = pyautogui.position()
            
            # Perform a micro-drag (2 pixels) to simulate physical interaction.
            # This is often more effective than a simple 'moveTo' for keeping 
            # specific applications or systems awake.
            pyautogui.dragTo(x + 2, y, duration=0.2)
            pyautogui.dragTo(x, y, duration=0.2)
            
            # Wait for 30 seconds before the next movement cycle.
            time.sleep(30)

class ARC(QMainWindow):
    """
    The main Application Window.
    
    Responsible for initializing the HUD interface, streaming the background 
    video, and managing window state (Normal vs. Fullscreen).
    """
    def __init__(self):
        super().__init__()

        # --- 1. Window Branding & Identity ---
        self.setWindowTitle("A.R.C Move")
        
        # Load the static icon. Windows uses the 1st frame if a GIF is provided.
        self.setWindowIcon(QIcon("HUD.png"))
        
        # --- 2. Dynamic Sizing ---
        # Get primary monitor geometry to calculate initial window size.
        screen = QApplication.primaryScreen().geometry()
        width = int(screen.width() * 0.8)   # 80% of screen width
        height = int(screen.height() * 0.8) # 80% of screen height
        
        self.resize(width, height)
        
        # Center the window on the display
        self.move(int((screen.width() - width) / 2), 
                  int((screen.height() - height) / 2))

        # --- 3. Multimedia Setup (The HUD) ---
        # The VideoWidget is the canvas where the video is drawn.
        self.video_widget = QVideoWidget()
        
        # QMediaPlayer handles the backend decoding and playback.
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        
        # Direct URL to the hosted MP4 asset.
        video_path = QUrl("https://github.com/ChaitanyaKumarS2403/assets/releases/download/ctOS_Boot/ctOS_Booting.mp4")
        self.media_player.setSource(video_path)

        # Infinite loop: -1 tells the player to restart the video once it ends.
        self.media_player.setLoops(-1) 

        # --- 4. UI Layout ---
        # Using a vertical layout with 0 margins to ensure the video is edge-to-edge.
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.video_widget)

        # Set the central widget container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- 5. Start Background Thread ---
        # Initializing the worker thread to start cursor movement immediately.
        self.worker = MovementThread()
        self.worker.start()

        # Begin video playback.
        self.media_player.play()

    def keyPressEvent(self, event):
        """
        Handles keyboard inputs for the application.
        
        Args:
            event (QKeyEvent): The key event triggered by the user.
        """
        # Toggle Fullscreen mode using the 'F' key.
        if event.key() == Qt.Key.Key_F:
            if self.isFullScreen():
                # Reverts to windowed mode with title bar and controls.
                self.showNormal()
            else:
                # Enters "Cinema/HUD" mode: No title bar, no taskbar.
                self.showFullScreen()

if __name__ == "__main__":
    # Initialize the high-level Application object.
    app = QApplication(sys.argv)
    
    # Create and display the ARC HUD.
    window = ARC()
    window.show()
    
    # Execute the application loop.
    sys.exit(app.exec())