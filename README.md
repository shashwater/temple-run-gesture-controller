# Temple Run Gesture Controller

Play Temple Run using hand gestures captured by your webcam.

The controller uses MediaPipe hand landmarks, classifies finger positions and hand tilt, then sends keyboard input to the focused game window.

## Controls

| Gesture | Action | Key |
| --- | --- | --- |
| Fist | Slide | Down arrow |
| One finger | Turn left | Left arrow |
| Two fingers | Turn right | Right arrow |
| Three fingers | Jump | Up arrow |
| Hand tilt | Change lane | A / D |

## How it works

`Webcam → OpenCV frames → MediaPipe landmarks → gesture rules → keyboard events`

- `src/main.py` captures frames, runs hand tracking and displays the detected gesture.
- `src/gestures.py` classifies raised fingers and hand tilt.
- `src/controller.py` maps gestures to keyboard events. Turn, slide and jump actions use a one-second repeat cooldown.

## Run locally

```bash
git clone https://github.com/shashwater/temple-run-gesture-controller.git
cd temple-run-gesture-controller
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
```

Launch Temple Run in an Android emulator and focus its window before using the controller. On Windows, activate the environment with `.venv\Scripts\activate`.

Press `q` in the camera window to stop. Your OS may ask for camera and keyboard-control permissions.

## Limitations

This is a rule-based prototype for one hand. Lighting, camera angle and hand position affect recognition. Tilt events repeat while the hand stays tilted. Dependencies are not yet version-pinned.

## Stack

Python · OpenCV · MediaPipe · NumPy · pynput
