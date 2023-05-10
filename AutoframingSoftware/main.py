import cv2

from InterfaceStruct import ROI
from InterfaceStruct import Layout
from InterfaceStruct import InputResolution
from InterfaceStruct import OutputResolution
from InterfaceStruct import InputOutputRatio
from Output_Module import CropOutput
from pan_smoothing import CamSmoothing
from InterfaceStruct import Min_Change_Score

import Object_Detection_Module
import Ultility

Mouse_Pos = ROI(0,0,0,0)
Cam_Pos = ROI(0,0,1,1)
#Prev_ROI_List = [ROI(0,0,1,1) for i in range(10)]

def Mouse_Callback(event, x, y, flags, param):
    """
    Height, width = 0 indicate that my Pos was overwriten by mouse instead of previous box.

    Args:
        event (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
        flags (_type_): _description_
        param (_type_): _description_
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        global isMouseInterupt;isMouseInterupt=True
        Mouse_Pos.x = x
        Mouse_Pos.y = y

def main():
    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow('Video')
    cv2.setMouseCallback('Video', Mouse_Callback)
    global isMouseInterupt;isMouseInterupt=True
    BoundROI=ROI(0,0,1,1)
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (InputResolution.w,InputResolution.h), interpolation = cv2.INTER_LINEAR)
        FaceArray = Object_Detection_Module.Face_Detection(frame)
        dist = float('inf')
        #print(isMouseInterupt)
        if isMouseInterupt:
            #print("")
            #print("face Change")
            for face in FaceArray:
                face = face.to_Centroid()
                (x,y) = (face.x_Centroid,face.y_Centroid)
                Cur_dist = Ultility.sq_dist(x,y,Mouse_Pos.x*InputOutputRatio,Mouse_Pos.y*InputOutputRatio)
                #print("x",x,"y",y)
                #print("xM",Mouse_Pos.x*InputOutputRatio,"yM",Mouse_Pos.y*InputOutputRatio)
                #print("dist",Cur_dist)
                if dist > Cur_dist:
                    dist = Cur_dist
                    BoundROI = face.to_Standard()
                #print("xB",BoundROI.x,"yB",BoundROI.y)
                #print("")
                
                #isMouseInterrupt in the loop means that isMouseInterrupt would not be disable if last iteration were skip due to AI issue.
                isMouseInterupt=False
        else:
            #Since import code were in loop, if FaceArray is empty due to detection problem, the iteration were safely skip
            #BoundROI of previous iterate would be return instead.
            ClosestROI,Score = Ultility.Most_Similar_ROI(FaceArray,BoundROI,Ultility.Score_Method_Manhattan_dist)
            #Prev_ROI_List.pop(0)
            #Prev_ROI_List.append(ClosestROI)
            BoundROI = ClosestROI if Score>Min_Change_Score else BoundROI

        CamSmoothing(Cam_Pos,BoundROI)
        OutputImg = CropOutput(frame,
                               Layout([ROI(0,0,InputResolution.w,InputResolution.h),
                                       Cam_Pos],
                                      [ROI(0,0,OutputResolution.w,OutputResolution.h),
                                       ROI(OutputResolution.w+10,0,OutputResolution.h,OutputResolution.h)]))
        cv2.imshow('Video',OutputImg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    # closing all open windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
