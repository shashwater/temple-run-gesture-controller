# Temple Run Gesture Controller 🎮🖐️

Control Temple Run with your bare hands using Python, OpenCV, and MediaPipe!

This real-time computer vision project lets you use hand gestures to play Temple Run inside an Android emulator like Bluestacks — no keyboard or controller needed.

## 🔥 Demo
- ✊ **Fist** → Slide (↓)
- ☝️ **1 Finger** → Turn Left (←)
- ✌️ **2 Fingers** → Turn Right (→)
- 🤟 **3 Fingers** → Jump (↑)
- 🤚 **Tilt** left/right → Lane movement (A/D keys)

## 🧠 Tech Stack
- Python
- OpenCV
- MediaPipe
- pynput

## 🚀 How to Run
1. Clone this repo:
    ```bash
    git clone https://github.com/shashwater/temple-run-gesture-controller.git
    cd temple-run-gesture-controller
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch Temple Run in Bluestacks and focus the window

4. Run the controller:
    ```bash
    python3 src/main.py
    ```

## 📹 What It Does
Your webcam detects your hand gestures, translates them to keyboard inputs (`↑ ↓ ← → a d`), and sends them to the focused window — letting you control Temple Run like a Jedi.

---

Made with 👊 and caffeine by [@shashwater](https://github.com/shashwater)
