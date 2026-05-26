# 🛰️ A.R.C Move
A.R.C Move, named after the backcronym "Automated Realtime Cursor Movement" – is a high-tech utility designed to simulate physical mouse activity using an immersive JARVIS-inspired HUD (Heads-Up Display). It ensures system activity remains "online" while providing a futuristic visual experience.

Developed by **Chaitanya Kumar Sathivada**

<a href="https://github.com/ChaitanyaKumarS2403">
  <img src="https://github.com/ChaitanyaKumarS2403/assets/raw/main/projects_repo/Misc/github_profile.png" alt="GitHub" height=50>
</a>
<a href="https://www.linkedin.com/in/chaitanya-kumar-sathivada/">
  <img src="https://github.com/ChaitanyaKumarS2403/assets/raw/main/projects_repo/Misc/linkedin_profile.png" alt="LinkedIn" height=50>
</a>

Download the resource now! Click on the `Download` button below and extract the files to your desired location.

<a href="https://github.com/ChaitanyaKumarS2403/ffmpeg-wrapper/releases/download/v1.0.0.0/FFmpeg.Wrapper.exe">
        <img src="https://github.com/ChaitanyaKumarS2403/assets/raw/main/projects_repo/Misc/DownloadNow.png" alt="Download Now" height=50>
</a>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
</p>

## ✨ Features
* **Immersive GUI:** A full-screen looping JARVIS HUD video background.
* **Physical Simulation:** Uses `pyautogui` to perform micro-movements (2 pixels) to mimic actual human interaction.
* **Smart Threading:** The GUI remains responsive while the movement logic runs silently in the background.
* **One-Click Launch:** Includes a `.bat` file that automatically checks for and installs missing dependencies.
* **Branded Interface:** Integrated window icon support for a professional look.

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
</p>

## 🚀 Getting Started

### Prerequisites
* **Python 3.10+** (Tested on 3.13)
* **Pip** (Latest version recommended)

### Installation
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ChaitanyaKumarS2403/A.R.C-Move.git
    cd A.R.C-Move
    ```
2.  **Add your Assets:**
    * Place your HUD video URL in the `video_path` variable. @[line 47]

### Running the App
Simply double-click the `execute.bat` file. 
This script will:
1.  Verify Python is installed.
2.  Install required libraries (`pyautogui`, `PyQt6`).
3.  Launch the **A.R.C** interface.

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
</p>

## 🛠️ Technical Breakdown
The project is built using a dual-layer architecture:
* **The Worker (QThread):** Manages the `while True` loop for cursor movement every 30 seconds to prevent GUI freezing.
* **The Frontend (PyQt6):** Handles the Multimedia player and edge-to-edge video rendering using `QVideoWidget`.

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
</p>

## ⌨️ Controls
* **Minimize:** Hides the HUD to the taskbar while A.R.C stays active.
* **Maximize/Restore:** Scales the HUD to fill your display.
* **Close:** Stops the script and the movement logic immediately.
* **Safety Failsafe:** Slam your mouse into any corner of the screen to trigger the `pyautogui` failsafe.
