import cv2
from InterfaceStruct import ROI
from InterfaceStruct import Layout
import Object_Detection_Module
import Ultility

trace_Pos = ROI(0,0,0,0)



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
        trace_Pos.x = x
        trace_Pos.y = y
        trace_Pos.height = 0
        trace_Pos.width = 0
def main():
    img = cv2.imread('Image.jpg')
    img = cv2.resize(img, (780, 540),interpolation = cv2.INTER_LINEAR)
    FaceArray = Object_Detection_Module.Face_Detection(img)
    cv2.namedWindow('Video')
    cv2.setMouseCallback('Video', Mouse_Callback)
    
    while True:
        #if w,h=0, is a mouse event, find the closest centroid ROI, else, find the most similar bounding box
        #find 
        dist = Ultility.sq_dist(FaceArray[0].x,FaceArray[0].y,trace_Pos.x,trace_Pos.y)
        BoundROI = ROI(FaceArray[0].x,FaceArray[0].y,FaceArray[0].w,FaceArray[0].h)
        for face in FaceArray:
            face = face.to_Centroid()
            (x,y,w,h) = (face.x_Centroid,face.y_Centroid,face.w_Centroid,face.h_Centroid)
            if dist > Ultility.sq_dist(x,y,trace_Pos.x,trace_Pos.y):
                dist = Ultility.sq_dist(x,y,trace_Pos.x,trace_Pos.y)
                BoundROI = face.to_Standard()

        cv2.rectangle(img, (BoundROI.x, BoundROI.y), (BoundROI.x+BoundROI.w, BoundROI.y+BoundROI.h), (255, 0, 0), 2)
        cv2.imshow('Video',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    # closing all open windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
