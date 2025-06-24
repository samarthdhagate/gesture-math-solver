import cv2

def render_overlay_text(frame, equation, result):
    """
    Displays expression and result as text overlay on the webcam feed.
    """
    cv2.putText(frame, f'Input: {equation}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Result: {result}', (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.putText(frame, "Show 'Q' gesture or press 'q' to quit", (10, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (128, 128, 128), 1)
