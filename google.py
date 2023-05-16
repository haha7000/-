import cv2
import numpy as np

# 이미지를 생성하고 흰색으로 채우기
img = np.zeros((1080, 1920, 3), np.uint8)
img.fill(255)

# 텍스트 삽입
text = "HELLO, MY NAME IS KIMDONGHUN"
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
thickness = 6
color = (200, 10, 120)
position = (50, 200)
cv2.putText(img, text, position, font, fontScale, color, thickness)

# 결과 이미지 출력
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
