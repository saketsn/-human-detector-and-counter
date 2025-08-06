import cv2
import numpy as np
import os

# === 1. SELECT CASCADE ===
# Recommended: use face or upperbody if you're not detecting the full body
# Available options: 'haarcascade_frontalface_default.xml', 'haarcascade_upperbody.xml', 'haarcascade_fullbody.xml'
cascade_file = 'haarcascade_frontalface_default.xml'  # <- Change here if needed

# === 2. VERIFY CASCADE FILE ===
if not os.path.exists(cascade_file):
    print(f"Error: Cascade file '{cascade_file}' not found in the current directory.")
    exit()

# === 3. LOAD CASCADE ===
human_cascade = cv2.CascadeClassifier(cascade_file)
if human_cascade.empty():
    print("Error: Failed to load the cascade classifier.")
    exit()

# === 4. INITIATE WEBCAM ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access the webcam.")
    exit()

print("Press 'q' to quit...")

# === 5. MAIN LOOP ===
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Detect humans/faces
    humans = human_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)  # Tweak for small faces/bodies
    )

    # Draw rectangles
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display count
    count = len(humans)
    cv2.putText(frame, f'Human Count: {count}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the video
    cv2.imshow('Human Detector and Counter', frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === 6. CLEANUP ===
cap.release()
cv2.destroyAllWindows()
