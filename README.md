# Gesture_Recognition
✋ Real-Time Gesture Recognition System Using MediaPipe & OpenCV

🧠 Classifies hand gestures and finger positions instantly

💻 Tech Stack: Python, OpenCV, MediaPipe, CV2
_________________________________________________________________________________________

💡 What This Project Does

This project detects and classifies hand gestures in real-time using webcam input and computer vision.

It tracks hand landmarks and applies logic to recognize gestures like:
✔️ Thumbs Up
✔️ Peace
✔️ Fist
✔️ Rock
✔️ Palm
✔️ Okay
✔️ Numbers from 1 to 5

🎥 Live Gesture Detection

→ Real-time hand tracking using MediaPipe
→ Gesture classification based on finger states
→ Includes logic for 10+ gestures (can easily scale more)

🧩 Designed to work on CPU — no GPU needed
🪶 Lightweight & fast even on lower-end systems
_________________________________________________________________________________________

🔍 How It Works

The pipeline follows three main stages:

Setup:
MediaPipe Hands + OpenCV for hand tracking and visualization.

Landmark Analysis:
Extracts 21 hand landmarks in real-time and calculates the position of each finger.

Logic (Rule-Based):
Applies boolean logic to determine whether each finger is open or closed, and matches the pattern to a known gesture.
_________________________________________________________________________________________

✋ Gestures Supported

Thumbs Up 👍

Peace ✌️

Stop ✋

Okay 👌

Fist ✊

Palm 🖐️

Rock 🤘

Heart 🤍

Numbers 1️⃣ to 5️⃣

More gestures can be added by tweaking the logic.
_________________________________________________________________________________________

⚙️ What's Unique

✔️ Works in real-time using only your laptop webcam
✔️ No deep learning model needed — rule-based logic
✔️ Supports multiple gesture types
✔️ Automatically displays detected gesture on screen
✔️ Built entirely in Python — beginner friendly
_________________________________________________________________________________________

🛠️ Technologies Used

Python

OpenCV

MediaPipe

CV2
_________________________________________________________________________________________

🔮 What’s Next?

Add gesture-based control features (volume up/down, screen capture, etc.)

Export model to work on web or mobile

Build a GUI or web interface (like Streamlit)

Expand gesture database using AI or ML models
_________________________________________________________________________________________

📁 Project Structure

webcam.py: Main script for real-time webcam detection

README.md: Project documentation

Gesture Recognition System.mp4: Project demo

Screenshots: to see the real time outputs
_________________________________________________________________________________________

🎥 Project Demo

Watch the complete gesture recognition in action on my LinkedIn — showing how a webcam and some logic can create a powerful interactive tool.
_________________________________________________________________________________________

🙋‍♀️ Built by:

Mannat Jain

Computer Science Student | AI & Python Enthusiast

🔗 https://www.linkedin.com/in/mannatjain14/ | https://github.com/Mannat-jain
