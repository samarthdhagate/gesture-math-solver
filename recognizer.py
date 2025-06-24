import numpy as np

def get_finger_state(hand_landmarks, handedness):
    """
    Returns number of extended fingers using MediaPipe hand landmarks.
    Adjusts logic for handedness (left vs right).
    """
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    if handedness == "Left":
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x else 0)

    for id in range(1, 5):
        fingers.append(1 if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y else 0)

    return fingers.count(1)

def calculate_distance(p1, p2):
    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def recognize_combined_gesture(hand1_data, hand2_data):
    """
    Identifies a combined gesture from two hands.
    Returns the corresponding symbol or command.
    """
    (hand1, label1), (hand2, label2) = hand1_data, hand2_data
    f1 = get_finger_state(hand1, label1)
    f2 = get_finger_state(hand2, label2)
    dist = calculate_distance(hand1.landmark[8], hand2.landmark[8])

    gesture_pair = tuple(sorted([f1, f2]))
    gesture_map = {
        (1, 1): "+" if dist > 0.06 else "exit",
        (1, 2): "-",
        (1, 3): "*",
        (1, 4): "/",
        (2, 2): "del",
        (1, 5): "6",
        (2, 5): "7",
        (3, 5): "8",
        (4, 5): "9",
        (0, 0): "=",
        (5, 5): "clear"
    }

    return gesture_map.get(gesture_pair, None)
