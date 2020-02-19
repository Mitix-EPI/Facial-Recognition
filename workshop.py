#!/usr/bin/env python3

import cv2
import getch

cam = cv2.VideoCapture(0)
face = 0
while True:
    ret, fram = cam.read()
    k = cv2.waitKey(33)
    gray_fram = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    res = cascade.detectMultiScale(gray_fram)
    if (k == ord('f') and face == 0):
        print("activated face")
        face = 1
    elif (face == 1 and k == ord('f')):
        face = 0
        print("desactivated face")
    if (face == 1):
        try :
            for i in range(len(res)):
                cv2.rectangle(fram, (res[i][0], res[i][1]), (res[i][0] + res[i][2], res[i][1] + res[i][3]), (0, 255, 0), 2)
        except:
            print("y'a personne")
    if ( k == 27):
        break
    cv2.imshow("frame", fram)
cam.release()
cv2.destroyAllWindows()