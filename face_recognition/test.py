import cv2
import os
import numpy as np
import face_recognition as fr
test_image=cv2.imread('image4.jpg')
faces_dectected,gray_img=fr.faceDetection(test_image)
print('face_detected:',faces_dectected)

# for(x,y,w,h) in faces_dectected:
#     cv2.rectangle(test_image,(x,y),(x+w,y+h),(0,255,0),thickness=5)
#
#
# resized_img=cv2.resize(test_image,(650,450))
# cv2.imshow('face detection',resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

faces,faceID=fr.label('images/')
face_recognizer=fr.train_classifier(faces,faceID)
name={'shubham':'shubham',

      }
for face in faces_dectected:
    (x,y,w,h)=face
    roi_graay=gray_img[y:y+h,x:x+h]
     label,confidence=face_recognizer.predict(roi_graay)
    print()




