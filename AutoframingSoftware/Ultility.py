import math
import numpy as np
import cv2
from InterfaceStruct import ROI
from typing import List

sq_dist = lambda x1,y1,x2,y2:(x2 - x1)**2 + (y2 - y1)**2

def Score_Method_Euclidean_dist_sqr(a:ROI,b:ROI) -> float:
    return (a.x - b.x)**2 + (a.y - b.y)**2 + (a.w - b.w)**2 + (a.h - b.h)**2
def Score_Method_Euclidean_dist(a:ROI,b:ROI) -> float:
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.w - b.w)**2 + (a.h - b.h)**2)
def Score_Method_Manhattan_dist(a:ROI,b:ROI) -> float:
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.w - b.w) + abs(a.h - b.h)

def Most_Similar_ROI(Face_List:List[ROI],Prev_ROI:ROI,Dist_Score_Method) -> ROI:
    dist_Score = float('inf')
    ClosestROI=Prev_ROI
    for Object_ROI in Face_List:
        cur_Dist_Score = Dist_Score_Method(Object_ROI,Prev_ROI)
        if dist_Score > cur_Dist_Score:
            ClosestROI = Object_ROI
            dist_Score = cur_Dist_Score
    #print(dist_Score)
    return ClosestROI,dist_Score


def isMovingObject(ListOfROI: List[ROI]) -> bool:
    x = [thisROI.x for thisROI in ListOfROI]
    y = [thisROI.y for thisROI in ListOfROI]
    w = [thisROI.w for thisROI in ListOfROI]
    h = [thisROI.h for thisROI in ListOfROI]

    x = np.diff(x); y = np.diff(y)
    print(x)
    return (isSameSign(x,1)==1) or (isSameSign(y,1)==1)

def isSameSign(ListOfVar: List[float], tolerance:int) -> int:
    positive = 0
    negative = 0
    zero = 0
    for num in ListOfVar:
        if num<0:
            negative = negative + 1
        elif num>0:
            positive = positive + 1
        else:
            zero = zero + 1
    if zero == len(ListOfVar):
        return 0
    elif (positive<=tolerance or negative<=tolerance):
        return 1
    return -1
        
def DebugImagePrint(frame:np.ndarray,ROIArray) -> None:
    img = np.copy(frame)
    for aROI in ROIArray:
        img = cv2.rectangle(img, (aROI.x, aROI.y), (aROI.x+aROI.w, aROI.y+aROI.h),(0, 0, 0),2)
    cv2.imshow('debug',img)
