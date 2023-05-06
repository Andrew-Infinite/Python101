import cv2
from InterfaceStruct import ROI
from InterfaceStruct import Layout
import Object_Detection_Module

def main():
    img = cv2.imread('Image.jpg')
    img = cv2.resize(img, (780, 540),interpolation = cv2.INTER_LINEAR)
    faces = Object_Detection_Module.Face_Detection(img)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Video',img)
    cv2.waitKey(0)
  
    # closing all open windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()