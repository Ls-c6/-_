import cv2
import numpy as np

img=cv2.cvtColor(cv2.imread("shape.jpg"),cv2.COLOR_BGR2GRAY)
temp=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
canny=cv2.Canny(img,150,200)
# 輪廓,階層=cv2.findContours(變數,輪廓,近似方法)
contours,hierarchy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for i in contours:
    # 畫出輪廓 (-1等於把每個找到的輪廓都畫出來)
    cv2.drawContours(temp,i,-1,(32,52,176),2)
    # 輪廓面積 (輸出0為噪點)
    print(cv2.contourArea(i))
    # 輪廓周長 (第二個參數為輪廓是否閉合)
    print(cv2.arcLength(i,True))

cv2.imshow("Shape",img)
cv2.imshow("Canny",canny)
cv2.imshow("Contours",temp)
cv2.waitKey(0)
