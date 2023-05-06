import cv2
import numpy as np

def Face_Detection(frame:np.ndarray):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(50, 0), flags=cv2.CASCADE_SCALE_IMAGE)
    print(type(faces))
    return faces




