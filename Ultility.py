import math
from InterfaceStruct import ROI
from InterfaceStruct import Min_Change_Score
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
    for Object_ROI in Face_List:
        cur_Dist_Score = Dist_Score_Method(Object_ROI,Prev_ROI)
        if dist_Score > cur_Dist_Score:
            ClosestROI=Object_ROI
            dist_Score = cur_Dist_Score
    print(dist_Score)
    return Prev_ROI if dist_Score<Min_Change_Score else ClosestROI