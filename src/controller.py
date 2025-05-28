from pynput.keyboard import Controller, Key
import time

keyboard = Controller()
last_action = None
cooldown = 1  # seconds
last_time = time.time()

def handle_gesture(gesture):
    global last_action, last_time

    key_map = {
        "Jump": Key.up,
        "Slide": Key.down,
        "Left": Key.left,
        "Right": Key.right
    }

    current_time = time.time()

    if gesture != last_action or current_time - last_time > cooldown:
        if gesture in key_map:
            print(f"[ACTION] {gesture} → {key_map[gesture]}")
            keyboard.press(key_map[gesture])
            keyboard.release(key_map[gesture])
            last_action = gesture
            last_time = current_time
        elif gesture != "Unknown":
            print(f"[INFO] Gesture detected: {gesture} (no key mapped)")


def handle_tilt(tilt_direction):
    if tilt_direction == "Tilt Left":
        print("[TILT] Move lane left (A)")
        keyboard.press('a')
        keyboard.release('a')
    elif tilt_direction == "Tilt Right":
        print("[TILT] Move lane right (D)")
        keyboard.press('d')
        keyboard.release('d')
