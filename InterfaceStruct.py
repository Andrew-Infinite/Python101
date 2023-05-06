from typing import List


class ROI:
    def __init__(self, x:int, y:int,w:int,h:int) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h
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


