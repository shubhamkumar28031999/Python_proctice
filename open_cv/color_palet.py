import cv2
import numpy as np

def main():
    image = np.zeros((512,512,3),np.uint8)
    window_name='color palet'
    cv2.namedWindow(window_name)
    cv2.createTrackbar('B',window_name,0,255,)
    while(True):
        cv2.imshow(window_name,image)


        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()

main()
