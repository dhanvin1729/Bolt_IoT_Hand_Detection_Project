import cv2
import HandTrackingModule as htm
from boltiot import Bolt

mybolt = Bolt("cb95c493-f7d0-4045-852c-1ffb7d3efd12", "BOLT9101957")

wCam,hCam=(640,480)

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

detector=htm.handDetector(detectionCon=0.75)

tipIds=[4,8,12,16,20]

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img, draw=False)
    
    if len(lmList)!=0:
        fingers=[]
        if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        for i in range(1,5):
            if lmList[tipIds[i]][2]<lmList[tipIds[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingers=fingers.count(1)
        for i in fingers:
            if fingers[i]==1:
                mybolt.digitalWrite(str(i),'HIGH')
            else:
                mybolt.digitalWrite(str(i),'LOW')

        


    cv2.imshow("IMAGE",img)
    cv2.waitKey(20)




        
