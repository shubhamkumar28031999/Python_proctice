import cv2
import numpy as np

def main():
    img= np.zeros((512,512,3),np.uint8)
    cv2.line(img,(23,89),(100,300),(255,0,0),2)
    cv2.rectangle(img,(100,60),(200,170),(0,255,0),3)
    cv2.circle(img,(300,300),70,(0,0,255),-1)
    cv2.ellipse(img,(160,260),(50,20),0,0,360,(22,45,155),-1)

    points= np.array([[80,2],[125,5],[179,9],[230,78],[400,400]],np.int32)
    points=points.reshape((-1,1,2))
    cv2.polylines(img,[points],True,(0,255,255))

    cv2.putText(img,'akash',(100,100),cv2.FONT_HERSHEY_DUPLEX,3,(69,240,125))


    cv2.imshow('shubham',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()