def detect_gesture(hand_landmarks):
    tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers_up = []

    lm = hand_landmarks.landmark

    # Ignore thumb for reliability
    fingers_up.append(0)

    # Check index to pinky
    for tip in tips[1:]:
        if lm[tip].y < lm[tip - 2].y - 0.02:
            fingers_up.append(1)
        else:
            fingers_up.append(0)

    total = sum(fingers_up)

    if total == 0:
        return "Slide"      # ✊ Fist
    elif total == 1:
        return "Left"       # ☝️ 1 finger
    elif total == 2:
        return "Right"      # ✌️ 2 fingers
    elif total == 3:
        return "Jump"       # 🤟 3 fingers
    else:
        return "Unknown"


def get_hand_tilt_direction(hand_landmarks):
    lm = hand_landmarks.landmark
    wrist = lm[0]
    middle_tip = lm[12]

    x_diff = middle_tip.x - wrist.x

    if x_diff > 0.08:
        return "Tilt Right"
    elif x_diff < -0.08:
        return "Tilt Left"
    else:
        return None
