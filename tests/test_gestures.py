"""Synthetic-hand tests (no camera / MediaPipe needed): python3 tests/test_gestures.py"""
import math, os, sys
from types import SimpleNamespace as NS
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from gestures import detect_gesture, detect_gesture_legacy

BASES = {8: 5, 12: 9, 16: 13, 20: 17}  # tip -> MCP base


def hand(up, angle=0.0):
    """Upright hand with wrist at origin, rotated by `angle` degrees. up = fingers extended (idx, mid, ring, pinky)."""
    pts = [(0.0, 0.0)] * 21
    pts = list(pts)
    for i, (tip, on) in enumerate(zip((8, 12, 16, 20), up)):
        x = -0.06 + 0.04 * i
        pts[tip - 3] = (x, -0.20)                       # MCP
        pts[tip - 2] = (x, -0.30)                       # PIP
        pts[tip - 1] = (x, -0.38 if on else -0.26)      # DIP
        pts[tip] = (x, -0.46 if on else -0.22)          # tip
    a = math.radians(angle)
    c, s = math.cos(a), math.sin(a)
    return NS(landmark=[NS(x=x * c - y * s, y=x * s + y * c) for x, y in pts])


CASES = {"Slide": (0, 0, 0, 0), "Left": (1, 0, 0, 0), "Right": (1, 1, 0, 0), "Jump": (1, 1, 1, 0)}


def test_upright():
    for name, up in CASES.items():
        assert detect_gesture(hand(up)) == name, name


def test_rotation_invariant():
    for ang in (30, 60, 90, 180, 270):
        for name, up in CASES.items():
            assert detect_gesture(hand(up, ang)) == name, (name, ang)


def test_exact_finger_set():
    assert detect_gesture(hand((1, 0, 0, 1))) == "Unknown"  # index+pinky is not "Right"
    assert detect_gesture(hand((1, 1, 1, 1))) == "Unknown"  # open palm


def test_legacy_breaks_when_rotated():
    assert detect_gesture_legacy(hand((1, 1, 0, 0), 90)) != "Right"


if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v(); print("ok", k)
