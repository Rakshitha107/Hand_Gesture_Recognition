
# Module for hand recognition functions to get points positions and draw the hands

# import library
import mediapipe as mp
import cv2

# class to initialize values and functions
class handDetector:

    # constructor
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils


    # check for hands and draw them and return the image with drawn one
    def find_hands(self, img, draw=True):
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRgb)
        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)
        return img

    # returns list of position of all the points
    def find_position(self, img, handno=0, draw=True):
        lst = []

        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                l, w, c = img.shape
                cx = int(lm.x * w)
                cy = int(lm.y * l)
                lst.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lst
