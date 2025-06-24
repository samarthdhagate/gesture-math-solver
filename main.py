import cv2
import mediapipe as mp
import time

from recognizer import recognize_combined_gesture, get_finger_state
from evaluator import calculate_output
from overlay import render_overlay_text
from speaker import speak

mp_hands = mp.solutions.hands
hand_processor = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

detected_hands = []
input_equation = ""
computed_answer = ""
prev_gesture_time = 0
update_interval = 1.25

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand_processor.process(frame_rgb)
    current_time = time.time()
    detected_hands = []

    if results.multi_hand_landmarks and results.multi_handedness:
        for landmarks, hand_type in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_type.classification[0].label
            detected_hands.append((landmarks, label))
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        if len(detected_hands) == 1:
            hand, label = detected_hands[0]
            finger_count = get_finger_state(hand, label)
            if 0 <= finger_count <= 5 and current_time - prev_gesture_time > update_interval:
                input_equation += str(finger_count)
                prev_gesture_time = current_time

        elif len(detected_hands) == 2:
            gesture = recognize_combined_gesture(detected_hands[0], detected_hands[1])
            if gesture and current_time - prev_gesture_time > update_interval:
                if gesture == "clear":
                    input_equation = ""
                    computed_answer = ""
                elif gesture == "del":
                    input_equation = input_equation[:-1]
                elif gesture == "=":
                    computed_answer = calculate_output(input_equation)
                    speak(f"The answer is {computed_answer}")
                elif gesture == "exit":
                    break
                else:
                    input_equation += gesture
                prev_gesture_time = current_time

    render_overlay_text(frame, input_equation, computed_answer)
    cv2.imshow("Gesture Calculator", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
    elif key == ord('c'):
        input_equation = ""
        computed_answer = ""

cap.release()
cv2.destroyAllWindows()
