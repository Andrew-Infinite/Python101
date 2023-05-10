from typing import List

class ROI:
    def __init__(self, x:int, y:int,w:int,h:int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def to_Centroid(self):
        return ROI_Centroid(self.x+self.w//2,self.y+self.h//2,self.w,self.h)
    def to_Boundary_Coordinate(self):
        return (self.x,self.y,self.x+self.w,self.y+self.h)
class ROI_Centroid:
    def __init__(self, x:int, y:int,w:int,h:int):
        self.x_Centroid = x
        self.y_Centroid = y
        self.w_Centroid = w
        self.h_Centroid = h
    def to_Standard(self) -> ROI:
        return ROI(self.x_Centroid-self.w_Centroid//2,
                   self.y_Centroid-self.h_Centroid//2,
                   self.w_Centroid,
                   self.h_Centroid)
class Layout:
    def __init__(self,Src:List[ROI],Dst:List[ROI]):
        self.Src = Src
        self.Dst = Dst
        #outputStruct
class Layout_Handler:
    def __init__(self,ObjectROI:List[ROI]) -> Layout:
        Output_ROI = [ROI(0,0,1280,720),ROI(0,1280+10,720,720)]
        return Layout()
        #outputStruct


InputResolution = ROI(0,0,1280,720)
OutputResolution = ROI(0,0,854,480)
InputOutputRatio = InputResolution.w/OutputResolution.w
MaxCamSpeedXY = 100
MaxCamSpeedWH = 100
Min_Change_Score = 200
