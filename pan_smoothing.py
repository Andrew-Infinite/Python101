from InterfaceStruct import ROI
from InterfaceStruct import MaxCamSpeed
import time

def CamSmoothing(Pos_Now:ROI,Pos_Target:ROI):
    Pos_Now.x = _moving(Pos_Now.x,Pos_Target.x)
    Pos_Now.y = _moving(Pos_Now.y,Pos_Target.y)
    Pos_Now.w = _moving(Pos_Now.w,Pos_Target.w)
    Pos_Now.h = _moving(Pos_Now.h,Pos_Target.h)
    time.sleep(0.01)


def _moving(Now:int,Target:int):
    if Now!=Target:
        if abs(Target-Now)<=1:
            return Target
        elif abs(Target-Now)*0.1<MaxCamSpeed:
            return Now + round((Target-Now)*0.1)
        else:
            dir = 1 if Now<Target else -1
            return Now + dir*MaxCamSpeed
    else:
        return Target
    """
    if abs(Now-Target)>CamSpeed:
        dir = 1 if Now<Target else -1
        return Now + dir*CamSpeed
    else:
        return Target
    """
