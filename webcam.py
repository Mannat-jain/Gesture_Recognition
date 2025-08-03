import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# hand tracking
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

# finger states (True=open, False=closed)
def get_finger_states(landmarks):
    fingers = []

    # Thumb (x axis because it's sideways)
    fingers.append(landmarks[4][0] > landmarks[3][0])

    # Other fingers (y axis)
    fingers.append(landmarks[8][1] < landmarks[6][1])   # Index
    fingers.append(landmarks[12][1] < landmarks[10][1]) # Middle
    fingers.append(landmarks[16][1] < landmarks[14][1]) # Ring
    fingers.append(landmarks[20][1] < landmarks[19][1]) # Pinky

    return fingers

# Function to classify gesture based on finger states
def classify_gesture(fingers):
    if fingers == [False, True, False, False, False]:
        return "1"
    elif fingers == [False, True, True, False, False]:
        return "2 (Peace??)"
    elif fingers == [False, True, True, True, False]:
        return "3"
    elif fingers == [False, True, True, True, True]:
        return "4"
    elif fingers == [True, True, True, True, True]:
        return "5 (Palm??)"
    elif fingers == [True, False, False, False, False]:
        return "Thumbs Up!! "
    elif fingers == [False, False, False, False, False]:
        return "Fist!!"
    elif fingers == [False, True, False, False, True]:
        return "Rock!!"
    elif fingers == [False, False, True, True, True]:
        return "Okay!!"
    elif fingers == [True,True,False,False,False]:
        return "Heart!!"
    else:
        return "Unknown?????"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert to RGB(mediapipe req RGB and cv take in BGR)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture_text = "No hand detected"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append((int(lm.x * w), int(lm.y * h)))

            finger_states = get_finger_states(landmarks)
            gesture_text = classify_gesture(finger_states)

    # Display gesture
    cv2.putText(frame, gesture_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)
    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
