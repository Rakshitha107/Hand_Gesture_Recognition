# Hand_Gesture_Recognition
Developed a model to control media through hand gestures, that utilises mediapipe library for hand recognition and marking. The implementation leverages the MediaPipe framework for hand detection and tracking, and pyautogui and pycaw libraries for controlling keyboard, mouse, and audio functions, respectively.
Hand gestures includes, 
1) Volume control is based on the distance between the thumb and index finger
2) Play/pause based on all fingers and thumb folded
3) Forward based on all fingers and thumb folded except the little finger
4) Backward based on all fingers and thumb folded except the index finger

# Modules
handDetectorModule.py
  * Description: This module processes video input from the system's webcam to detect hands and draw landmarks on them.
  * Functionality:
      -Captures webcam video feed.
      -Detects hands in the input images using MediaPipe's hand detection model.
      -Draws landmarks on the detected hands.
      -Creates and returns a list of landmark positions.
    
2.gestureMediaControl.py
  * Description: This module interprets hand gestures detected by handDetectorModule.py to control media playback.
  * Functionality:
      -Imports pyautogui for keyboard and mouse controls and pycaw for audio controls.
      -Utilizes custom gestures defined using the landmark data from the hand detection module.
      -Implements the gestures.
