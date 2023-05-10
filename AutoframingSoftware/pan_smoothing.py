from InterfaceStruct import ROI
from InterfaceStruct import MaxCamSpeedXY
from InterfaceStruct import MaxCamSpeedWH
import copy
import time

def CamSmoothing(Pos_Now:ROI,Pos_Target:ROI):

    Pos_Now.x = _movingXY(Pos_Now.x,Pos_Target.x)
    Pos_Now.y = _movingXY(Pos_Now.y,Pos_Target.y)
    Pos_Now.w = _movingWH(Pos_Now.w,Pos_Target.w)
    Pos_Now.h = _movingWH(Pos_Now.h,Pos_Target.h)

    time.sleep(0.001)


def _movingXY(Now:int,Target:int):
    if Now!=Target:
        if abs(Target-Now)<=1:
            return Target
        elif abs(Target-Now)*0.5<MaxCamSpeedXY:
            return Now + round((Target-Now)*0.5)
        else:
            dir = 1 if Now<Target else -1
            return Now + dir*MaxCamSpeedXY
    else:
        return Target
def _movingWH(Now:int,Target:int):
    if Now!=Target:
        if abs(Target-Now)<=1:
            return Target
        elif abs(Target-Now)*0.5<MaxCamSpeedWH:
            return Now + round((Target-Now)*0.5)
        else:
            dir = 1 if Now<Target else -1
            return Now + round(dir*MaxCamSpeedWH)
    else:
        return Target
    """
    if abs(Now-Target)>CamSpeed:
        dir = 1 if Now<Target else -1
        return Now + dir*CamSpeed
    else:
        return Target
    """
