import cv2

img = cv2.imread("fly.png",1)

cv2.imshow("fly", img)
cv2.waitKey(0)
cv2.destroyAllWindows()