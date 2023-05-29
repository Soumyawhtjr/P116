import cv2
img=cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.putText(img,"Sun",(1000,300),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,255))
#cv2.putText(img,"Mercury",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))
#cv2.putText(img,"Venus",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))
#cv2.putText(img,"Earth",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))
#cv2.putText(img,"Mars",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))
#cv2.putText(img,"Jupiter",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))
#cv2.putText(img,"Saturn",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))
#cv2.putText(img,"Neptune",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,255,255))

cv2.imshow()
#cv2.imwrite("Solar_systemwithname.jpg",img)




