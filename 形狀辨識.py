import cv2
import numpy as np

img=cv2.cvtColor(cv2.imread("shape.jpg"),cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(0,0),fx=0.65,fy=0.65)
temp=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
canny=cv2.Canny(img,150,200)
# 輪廓,階層=cv2.findContours(變數,輪廓,近似方法)
contours,hierarchy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for i in contours:
    # 畫出輪廓 (-1等於把每個找到的輪廓都畫出來)
    cv2.drawContours(temp,i,-1,(32,52,176),2)
    # 判斷是否為噪點
    if cv2.contourArea(i)>0:
        # 近似值越大多邊形邊越多 越小則越少
        top=cv2.approxPolyDP(i,cv2.arcLength(i,True)*0.02,True)
        corners=len(top)
        print(len(top))
        # 把圖形框起並畫出 (左上座標,右上座標,寬度,高度)
        x,y,w,h=cv2.boundingRect(top)
        cv2.rectangle(temp,(x,y),(x+w,y+h),(255,0,0),3)
        if corners==3:
            cv2.putText(temp,"triangle",(x-15,y-10),cv2.FONT_HERSHEY_PLAIN,2,(164,33,78),2)
        elif corners==4:
            cv2.putText(temp,"rectangle",(x-15,y-10),cv2.FONT_HERSHEY_PLAIN,2,(164,33,78),2)
        elif corners==5:
            cv2.putText(temp,"pentagon",(x-15,y-10),cv2.FONT_HERSHEY_PLAIN,2,(164,33,78),2)
        else:
            cv2.putText(temp,"circle",(x-15,y-10),cv2.FONT_HERSHEY_PLAIN,2,(164,33,78),2)


cv2.imshow("Contours",temp)
cv2.waitKey(0)
