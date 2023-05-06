import cv2
import numpy as np
from typing import List
from InterfaceStruct import ROI

def Face_Detection(frame:np.ndarray) -> np.ndarray:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
    FaceArray = np.empty(len(faces), dtype=object)

    for index,(x, y, w, h) in enumerate(faces):
        FaceArray[index]=ROI(x,y,w,h)
    return FaceArray




