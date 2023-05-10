import cv2
import numpy as np
from typing import List
from InterfaceStruct import ROI
from InterfaceStruct import InputResolution
from Ultility import DebugImagePrint

def Face_Detection(frame:np.ndarray) -> np.ndarray:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #scaleFactor need to var
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
    FaceArray = np.empty(len(faces), dtype=object)
    
    for index,(x, y, w, h) in enumerate(faces):
        #padding
        CentroidROI = ROI(x,int(y-w*0.1),w,h).to_Centroid()
        #2.0 need to be var
        CentroidROI.h_Centroid = int(max(CentroidROI.h_Centroid,CentroidROI.w_Centroid)*2.0)
        CentroidROI.w_Centroid = CentroidROI.h_Centroid
        StandardROI = CentroidROI.to_Standard()
        #boundary_Handling
        StandardROI.x = StandardROI.x if StandardROI.x>0 else 0
        StandardROI.y = StandardROI.y if StandardROI.y>0 else 0

        StandardROI.x = StandardROI.x if StandardROI.x+StandardROI.w<InputResolution.w else InputResolution.w - StandardROI.w
        StandardROI.y = StandardROI.y if StandardROI.y+StandardROI.h<InputResolution.h else InputResolution.h - StandardROI.h
        if StandardROI.x<0 or StandardROI.y<0:
            #skip this iteration
            return []
        #StandardROI.h = StandardROI.h if StandardROI.y+StandardROI.h < InputResolution.h else InputResolution.h
        #StandardROI.w = StandardROI.h

        FaceArray[index]=StandardROI
    #DebugImagePrint(frame,FaceArray)
    return FaceArray




