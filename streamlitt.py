# gesture_app.py

import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

st.title("🖐️ Hand Gesture Detection App")

# Set up MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# OpenCV Video Capture
cap = cv2.VideoCapture(0)
stframe = st.empty()

st.info("📸 Turn on your webcam to begin")

while True:
    ret, frame = cap.read()
    if not ret:
        st.warning("❌ Failed to capture from camera")
        break

    # Flip the frame to avoid mirror view
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    # Convert to RGB again for Streamlit display
    stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    # Optional: add a stop condition (for development use 'break' or 'ESC')
