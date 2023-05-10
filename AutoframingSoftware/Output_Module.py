import cv2
import numpy as np
from InterfaceStruct import Layout
from InterfaceStruct import OutputResolution

def CropOutput(frame:np.ndarray,layoutStruct:Layout):
    BackGround = np.zeros((OutputResolution.h,OutputResolution.w + 10 + OutputResolution.h, 3), np.uint8)
    for SrcROI,DstROI in zip(layoutStruct.Src,layoutStruct.Dst):
        #crop -> resize
        x_lo,y_lo,x_hi,y_hi = SrcROI.to_Boundary_Coordinate()
        img = frame[y_lo:y_hi,x_lo:x_hi]
        img = cv2.resize(img, (DstROI.w,DstROI.h), interpolation = cv2.INTER_LINEAR)
        #paste it on output
        x_lo,y_lo,x_hi,y_hi = DstROI.to_Boundary_Coordinate()
        BackGround[ y_lo:y_hi,x_lo:x_hi] = img
    return BackGround
