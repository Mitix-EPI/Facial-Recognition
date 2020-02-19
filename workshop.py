#!/usr/bin/env python3

import cv2

# img = cv2.imread("charlie.jpg")
# cv2.imshow("img", img)
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cam = cv2.VideoCapture(0)
# while True:
#     ret, fram = cam.read()
#     k = cv2.waitKey(1)
#     cv2.imshow("frame", fram)
#     if ( k == 27):
#         break
# cam.release()
# cv2.destroyAllWindows()



# img = cv2.imread("charlie.jpg")
# tml = cv2.imread("waldo.jpg")

# res = cv2.matchTemplate(img, tml, cv2.TM_CCOEFF)
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(res)

# print(minVal)
# print(maxVal)
# print(minLoc)
# print(maxLoc)

# width = tml.shape[1]
# height = tml.shape[0]

# cv2.rectangle(img, maxLoc, (maxLoc[0] + width, maxLoc[1] + height), (255, 0, 0), 2)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


cam = cv2.VideoCapture(0)
while True:
    ret, fram = cam.read()
    k = cv2.waitKey(1)
    gray_fram = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    res = cascade.detectMultiScale(gray_fram)
    try :
        for i in range(len(res)):
            cv2.rectangle(fram, (res[i][0], res[i][1]), (res[i][0] + res[i][2], res[i][1] + res[i][3]), (0, 255, 0), 2)
    except:
        print("y'a personne")
    cv2.imshow("frame", fram)
    # print(res)
    if ( k == 27):
        break
cam.release()
cv2.destroyAllWindows()