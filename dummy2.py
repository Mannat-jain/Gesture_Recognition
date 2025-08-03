import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from collections import Counter

# Initialize MediaPipe for hand tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define gesture labels (You can expand this later)
gesture_labels = {
    0: "Fist",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
}

def count_fingers(hand_landmarks):
    # Check if fingers are open using landmark positions
    tips = [8, 12, 16, 20]  # Index to pinky tips
    fingers = []

    # Thumb (special case)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

def main():
    st.set_page_config(page_title="Gesture Recognition", layout="wide")
    st.title("🖐️ Real-Time Hand Gesture Recognition")

    run = st.checkbox("Start Camera")
    FRAME_WINDOW = st.image([])
    result_text = st.empty()

    if run:
        cap = cv2.VideoCapture(0)

        with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.warning("Camera not working!")
                    break

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                prediction = ""

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                        finger_count = count_fingers(hand_landmarks)
                        prediction = gesture_labels.get(finger_count, "Unknown")

                FRAME_WINDOW.image(image, channels="BGR")
                result_text.markdown(f"### Predicted Gesture: **{prediction}**")

        cap.release()
    else:
        result_text.markdown("_Click the checkbox to start the webcam feed._")

if __name__ == "__main__":
    main()
