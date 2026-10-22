import math

TIPS = (8, 12, 16, 20)  # Index, Middle, Ring, Pinky fingertips (thumb ignored for reliability)
EXTEND_RATIO = 1.1       # tip must be this much farther from the wrist than its PIP joint


def _dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def fingers_extended(hand_landmarks):
    """Rotation-invariant: a finger is extended when its tip is farther from the wrist
    than its middle (PIP) joint, so it works with a tilted or sideways hand."""
    lm = hand_landmarks.landmark
    return tuple(_dist(lm[t], lm[0]) > _dist(lm[t - 2], lm[0]) * EXTEND_RATIO for t in TIPS)


_GESTURES = {
    (False, False, False, False): "Slide",  # Fist
    (True, False, False, False): "Left",    # Index only
    (True, True, False, False): "Right",    # Index + middle
    (True, True, True, False): "Jump",      # Index + middle + ring
}


def detect_gesture(hand_landmarks):
    # Requires the exact finger set, so index+pinky no longer counts as "two fingers"
    return _GESTURES.get(fingers_extended(hand_landmarks), "Unknown")


def detect_gesture_legacy(hand_landmarks):
    """Original rule (assumes an upright hand), kept for benchmarking."""
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
