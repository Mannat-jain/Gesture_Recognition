import streamlit as st
import cv2
import numpy as np
import time
import random

# Define your 7 dummy gestures
GESTURES = ["Thumbs Up 👍", "Peace ✌️", "Stop ✋", "Okay 👌", "Fist ✊", "Palm 🖐️", "Rock 🤘"]

# Dummy gesture predictor function
def predict_dummy_gesture():
    return random.choice(GESTURES)

# Streamlit UI
st.set_page_config(page_title="Gesture Recognition App", layout="centered")
st.title("🖐️ Real-Time Gesture Recognition (Dummy Version)")
st.markdown("### Using OpenCV + Streamlit | Simulated Logic")

start_cam = st.button("Start Webcam")

# Display area for webcam and prediction
frame_placeholder = st.empty()
gesture_placeholder = st.empty()

# Start webcam on button press
if start_cam:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Unable to access webcam. Please check your camera.")
    else:
        st.success("Webcam is live!")
        run = True

        # Loop to show frames
        while run:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to grab frame.")
                break

            # Flip and resize for better display
            frame = cv2.flip(frame, 1)
            resized = cv2.resize(frame, (640, 480))

            # Simulate prediction every 2 seconds
            if int(time.time()) % 2 == 0:
                predicted = predict_dummy_gesture()
                gesture_placeholder.markdown(f"### ✋ Detected Gesture: **{predicted}**")

            # Convert to RGB for Streamlit
            rgb_frame = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(rgb_frame, channels="RGB")

            # Allow stop if user stops the script
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
