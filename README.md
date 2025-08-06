# 👁️ Human Detector and Counter: Enhancing Security with Python-Based Surveillance

This project is a real-time human detection and counting system developed using Python and OpenCV. It helps monitor environments like public spaces, restricted zones, or classrooms by automatically detecting and counting the number of people visible in a live video stream (webcam or video file). It uses a pre-trained Haar Cascade model to recognize human bodies based on visual patterns.

---

## 🎯 Project Objective

The main goal of this project is to provide a basic surveillance system that enhances situational awareness in real-time by:
- Detecting human presence using a camera.
- Drawing bounding boxes around detected individuals.
- Displaying the total human count live on screen.

This system can be useful for simple crowd monitoring, entry tracking, or in classrooms and labs for administrative records.

---

## 🏗️ System Design Overview

The system is built as a modular pipeline with a clear flow from input to detection to output:

![alt text](image-1.png)


### 🔹 1. Video Input Layer
- Captures video from webcam (`cv2.VideoCapture(0)`) or can be modified to use a video file.
- Acts as the data source for the detection pipeline.

### 🔹 2. Processing Engine (`main.py`)
- Reads each frame using OpenCV.
- Converts the frame to grayscale (as Haar Cascades work on grayscale images).
- Enhances contrast using histogram equalization for better detection results.

### 🔹 3. Detection Engine (`haarcascade_fullbody.xml`)
- Uses OpenCV's `CascadeClassifier` to apply the Haar Cascade algorithm.
- The model scans the image to find body-like patterns and returns coordinates.

### 🔹 4. Output Display
- Annotates the original frame by drawing green rectangles around each detected person.
- Displays the real-time human count on the screen using `cv2.putText`.
- Allows the user to quit anytime by pressing the `q` key.

---

## 🔁 Application Workflow (Frame-by-Frame)
1.  **Start Application**: Load the Haar Cascade model and initialize video capture.
2.  **Frame Reading**: Read each frame in a loop from the video stream.
3.  **Preprocessing**: Convert the frame to grayscale and apply histogram equalization.
4.  **Detection**: Use `detectMultiScale()` to detect humans in the image.
5.  **Annotation**: Draw bounding boxes around each detected person and count them.
6.  **Display**: Show the result in a window titled *"Human Detector and Counter"*.
7.  **Exit**: On pressing `q`, the camera feed stops, and all OpenCV windows close.

---

## 📂 Project Structure

human-detector-and-counter/
│
├── main.py # Core Python script
├── haarcascade_fullbody.xml # Pre-trained model for human detection
├── requirements.txt # Dependencies
├── .gitignore # Files/folders to ignore in Git
└── README.md # Project documentation (this file)



---

## ⚙️ How to Run the Project

### ✅ Prerequisites
- Python 3.9 or above installed
- Git (optional, for pushing to GitHub)
- A webcam if using live feed

### 🔧 Setup Steps

```bash
# Step 1: Create and activate virtual environment
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies from requirements.txt
pip install -r requirements.txt

# Or install manually
pip install opencv-python==4.9.0.80 numpy==1.26.4

# Step 3: Run the application
python main.py
