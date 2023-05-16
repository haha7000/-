# import numpy as np
# import platform
# from PIL import ImageFont, ImageDraw, Image
# from matplotlib import pyplot as plt
 
# import uuid
# import json
# import time
# import cv2
# import requests

# def plt_imshow(title='image', img=None, figsize=(8 ,5)):
#     plt.figure(figsize=figsize)
 
#     if type(img) == list:
#         if type(title) == list:
#             titles = title
#         else:
#             titles = []
 
#             for i in range(len(img)):
#                 titles.append(title)
 
#         for i in range(len(img)):
#             if len(img[i].shape) <= 2:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
#             else:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
 
#             plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
#             plt.title(titles[i])
#             plt.xticks([]), plt.yticks([])
 
#         plt.show()
#     else:
#         if len(img.shape) < 3:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#         else:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#         plt.imshow(rgbImg)
#         plt.title(title)
#         plt.xticks([]), plt.yticks([])
#         plt.show()


# def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
#     if type(image) == np.ndarray:
#         color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(color_coverted)
 
#     if platform.system() == 'Darwin':
#         font = 'AppleGothic.ttf'
#     elif platform.system() == 'Windows':
#         font = 'malgun.ttf'
        
#     image_font = ImageFont.truetype(font, font_size)
#     font = ImageFont.load_default()
#     draw = ImageDraw.Draw(image)
 
#     draw.text((x, y), text, font=image_font, fill=color)
    
#     numpy_image = np.array(image)
#     opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
 
#     return opencv_image


# api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
# secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

# path = 'fly.png'
# files = [('file', open(path,'rb'))]

# request_json = {'images': [{'format': 'jpg',
#                                 'name': 'demo'
#                                }],
#                     'requestId': str(uuid.uuid4()),
#                     'version': 'V2',
#                     'timestamp': int(round(time.time() * 1000))
#                    }
 
# payload = {'message': json.dumps(request_json).encode('UTF-8')}
 
# headers = {
#   'X-OCR-SECRET': secret_key,
# }
 
# response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
# result = response.json()


# img = cv2.imread(path)
# roi_img = img.copy()

# font_italic = "FONT_ITALIC"

# for field in result['images'][0]['fields']:
#     text = field['inferText']
#     vertices_list = field['boundingPoly']['vertices']
#     pts = [tuple(vertice.values()) for vertice in vertices_list]
#     topLeft = [int(_) for _ in pts[0]]
#     topRight = [int(_) for _ in pts[1]]
#     bottomRight = [int(_) for _ in pts[2]]
#     bottomLeft = [int(_) for _ in pts[3]]
 
#     cv2.line(roi_img, topLeft, topRight, (0,255,0), 2)
#     cv2.line(roi_img, topRight, bottomRight, (0,255,0), 2)
#     cv2.line(roi_img, bottomRight, bottomLeft, (0,255,0), 2)
#     cv2.line(roi_img, bottomLeft, topLeft, (0,255,0), 2)
#     roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)
    
#     print(text)
 
# plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))


#--------------------------------------------------------------------------------------
# 진짜 테스트 하던것 

#-------------------------------------------------------------------------------------------








# import numpy as np
# import platform
# from PIL import ImageFont, ImageDraw, Image
# from matplotlib import pyplot as plt
 
# import uuid
# import json
# import time
# import cv2
# import requests

# def plt_imshow(title='image', img=None, figsize=(8 ,5)):
#     plt.figure(figsize=figsize)
 
#     if type(img) == list:
#         if type(title) == list:
#             titles = title
#         else:
#             titles = []
 
#             for i in range(len(img)):
#                 titles.append(title)
 
#         for i in range(len(img)):
#             if len(img[i].shape) <= 2:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
#             else:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
 
#             plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
#             plt.title(titles[i])
#             plt.xticks([]), plt.yticks([])
 
#         plt.show()
#     else:
#         if len(img.shape) < 3:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#         else:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#         plt.imshow(rgbImg)
#         plt.title(title)
#         plt.xticks([]), plt.yticks([])
#         plt.show()


# def is_chord(text):
#     first_char = text[0] if len(text) > 0 else ''
#     second_char = text[1] if len(text) > 1 else ''
#     third_char = text[2] if len(text) > 2 else ''

#     if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#         return True

#     if second_char in ['#', 'b', 'm', '7', 'sus', 'aug', 'dim', 'M', 'add']:
#         return True

#     if third_char == '' or third_char.isdigit():
#         return True

#     return False


# def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
#     if type(image) == np.ndarray:
#         color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(color_coverted)
 
#     if platform.system() == 'Darwin':
#         font = 'AppleGothic.ttf'
#     elif platform.system() == 'Windows':
#         font = 'malgun.ttf'
        
#     image_font = ImageFont.truetype(font, font_size)
#     font = ImageFont.load_default()
#     draw = ImageDraw.Draw(image)
 
#     #draw.text((x, y), text, font=image_font, fill=color)
    
#     numpy_image = np.array(image)
#     opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
 
#     return opencv_image


# api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
# secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

# path = 'see.jpeg'
# files = [('file', open(path,'rb'))]

# request_json = {'images': [{'format': 'jpg',
#                                 'name': 'demo'
#                                }],
#                     'requestId': str(uuid.uuid4()),
#                     'version': 'V2',
#                     'timestamp': int(round(time.time() * 1000))
#                    }
 
# payload = {'message': json.dumps(request_json).encode('UTF-8')}
 
# headers = {
#   'X-OCR-SECRET': secret_key,
# }
 
# response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
# result = response.json()


# img = cv2.imread(path)
# roi_img = img.copy()

# font_italic = "FONT_ITALIC"

# for field in result['images'][0]['fields']:
#     text = field['inferText']
#     if text and text[0].isupper():
#         vertices_list = field['boundingPoly']['vertices']
#         pts = [tuple(vertice.values()) for vertice in vertices_list]
#         topLeft = [int(_) for _ in pts[0]]
#         topRight = [int(_) for _ in pts[1]]
#         bottomRight = [int(_) for _ in pts[2]]
#         bottomLeft = [int(_) for _ in pts[3]]

#         cv2.line(roi_img, topLeft, topRight, (0,255,0), 2)
#         cv2.line(roi_img, topRight, bottomRight, (0,255,0), 2)
#         cv2.line(roi_img, bottomRight, bottomLeft, (0,255,0), 2)
#         cv2.line(roi_img, bottomLeft, topLeft, (0,255,0), 2)
#         roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)
        
#         print(text)

# plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))












#-------------------------------------------------------------------------------------------
# import numpy as np
# import platform
# from PIL import ImageFont, ImageDraw, Image
# from matplotlib import pyplot as plt

# import uuid
# import json
# import time
# import cv2
# import requests


# def plt_imshow(title='image', img=None, figsize=(8 ,5)):
#     plt.figure(figsize=figsize)

#     if type(img) == list:
#         if type(title) == list:
#             titles = title
#         else:
#             titles = []

#             for i in range(len(img)):
#                 titles.append(title)

#         for i in range(len(img)):
#             if len(img[i].shape) <= 2:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
#             else:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

#             plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
#             plt.title(titles[i])
#             plt.xticks([]), plt.yticks([])

#         plt.show()
#     else:
#         if len(img.shape) < 3:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#         else:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#         plt.imshow(rgbImg)
#         plt.title(title)
#         plt.xticks([]), plt.yticks([])
#         plt.show()


# def is_chord(text):
#     second_char = None

#     if len(text) > 1:
#         second_char = text[1]

#     if text[0].isupper() or second_char in ['#', 'b', 'm', '7', 'sus', 'aug', 'dim', 'M', 'add']:
#         return True

#     return False


# def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
#     if type(image) == np.ndarray:
#         color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(color_coverted)

#     if platform.system() == 'Darwin':
#         font = 'AppleGothic.ttf'
#     elif platform.system() == 'Windows':
#         font = 'malgun.ttf'

#     image_font = ImageFont.truetype(font, font_size)
#     font = ImageFont.load_default()
#     draw = ImageDraw.Draw(image)

#     draw.text((x, y), text, font=image_font, fill=color)

#     numpy_image = np.array(image)
#     opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

#     return opencv_image




# api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
# secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

# path = 'rkf.jpeg'
# files = [('file', open(path,'rb'))]

# request_json = {'images': [{'format': 'jpg',
#                             'name': 'demo'
#                            }],
#                 'requestId': str(uuid.uuid4()),
#                 'version': 'V2',
#                 'timestamp': int(round(time.time() * 1000))
#                }

# payload = {'message': json.dumps(request_json).encode('UTF-8')}

# headers = {
#     'X-OCR-SECRET': secret_key,
# }

# response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
# response_json = json.loads(response.text)

# result_list = response_json['images'][0]['fields']

# image = cv2.imread(path)
# # ------------------------

# # ----------------------
# plt_imshow(title='result', img=image)

# cv2.imwrite("detect_chord", image)







# import uuid
# import json
# import time
# import cv2
# import requests


# import numpy as np
# import platform
# from PIL import ImageFont, ImageDraw, Image
# from matplotlib import pyplot as plt

# import cv2

# def is_chord(text):
#     first_char = text[0] if len(text) > 0 else ''
#     second_char = text[1] if len(text) > 1 else ''
#     third_char = text[2] if len(text) > 2 else ''

#     if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#         return True

#     if second_char in ['#', 'b', 'm', '7', 'sus', 'aug', 'dim', 'M', 'add']:
#         return True

#     if third_char == '' or third_char.isdigit():
#         return True

#     return False


# def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
#     if type(image) == np.ndarray:
#         color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(color_coverted)

#     if platform.system() == 'Darwin':
#         font = 'AppleGothic.ttf'
#     elif platform.system() == 'Windows':
#         font = 'malgun.ttf'
        
#     image_font = ImageFont.truetype(font, font_size)
#     font = ImageFont.load_default()
#     draw = ImageDraw.Draw(image)

#     # draw.text((x, y), text, font=image_font, fill=color)

#     numpy_image = np.array(image)
#     opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

#     return opencv_image




# def transpose_chord(chord):
#     if chord == 'C':
#         return 'D'
#     elif chord == 'D':
#         return 'E'
#     elif chord == 'E':
#         return 'F'
#     elif chord == 'F':
#         return 'G'
#     elif chord == 'G':
#         return 'A'
#     elif chord == 'A':
#         return 'B'
#     elif chord == 'B':
#         return 'C'

#     return chord


# api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
# secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

# path = 'see.jpeg'
# files = [('file', open(path,'rb'))]

# request_json = {'images': [{'format': 'jpg',
#                                 'name': 'demo'
#                                }],
#                     'requestId': str(uuid.uuid4()),
#                     'version': 'V2',
#                     'timestamp': int(round(time.time() * 1000))
#                    }
 
# payload = {'message': json.dumps(request_json).encode('UTF-8')}
 
# headers = {
#   'X-OCR-SECRET': secret_key,
# }
 
# response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
# result = response.json()



# img = cv2.imread('see.jpeg')

# for field in result['images'][0]['fields']:
#     text = field['inferText']
#     if is_chord(text):
#         for i in range(len(text)):
#             if text[i].isupper():
#                 text = text[:i] + transpose_chord(text[i]) + text[i+1:]
#                 break
        
#         vertices_list = field['boundingPoly']['vertices']
#         pts = [tuple(vertice.values()) for vertice in vertices_list]
#         topLeft = [int(_) for _ in pts[0]]
#         roi_img = put_text(img, text, topLeft[0], topLeft[1] - 10, font_size=30)
        
#         print(text)

# plt.imshow(roi_img[:, :, ::-1])
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()












# import numpy as np
# import platform
# from PIL import ImageFont, ImageDraw, Image
# from matplotlib import pyplot as plt
 
# import uuid
# import json
# import time
# import cv2
# import requests

# def is_chord(text):
#     first_char = text[0] if len(text) > 0 else ''
#     second_char = text[1] if len(text) > 1 else ''
#     third_char = text[2] if len(text) > 2 else ''

#     if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#         return True

#     if second_char in ['#', 'b', 'm', '7', 'sus', 'aug', 'dim', 'M', 'add']:
#         return True

#     if third_char == '' or third_char.isdigit():
#         return True

#     return False


# def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
#     if type(image) == np.ndarray:
#         color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(color_coverted)
 
#     if platform.system() == 'Darwin':
#         font = 'AppleGothic.ttf'
#     elif platform.system() == 'Windows':
#         font = 'malgun.ttf'
        
#     image_font = ImageFont.truetype(font, font_size)
#     font = ImageFont.load_default()
#     draw = ImageDraw.Draw(image)
 
#     #draw.text((x, y), text, font=image_font, fill=color)
    
#     numpy_image = np.array(image)
#     opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
 
#     return opencv_image


# api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
# secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

# path = 'see.jpeg'
# files = [('file', open(path,'rb'))]

# request_json = {'images': [{'format': 'jpg',
#                                 'name': 'demo'
#                                }],
#                     'requestId': str(uuid.uuid4()),
#                     'version': 'V2',
#                     'timestamp': int(round(time.time() * 1000))
#                    }
 
# payload = {'message': json.dumps(request_json).encode('UTF-8')}
 
# headers = {
#   'X-OCR-SECRET': secret_key,
# }
 
# response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
# result = response.json()


# img = cv2.imread(path)
# roi_img = img.copy()


# for field in result['images'][0]['fields']:
#     text = field['inferText']
#     if text and text[0].isupper():
#         vertices_list = field['boundingPoly']['vertices']
#         pts = [tuple(vertice.values()) for vertice in vertices_list]
#         topLeft = [int(_) for _ in pts[0]]
#         topRight = [int(_) for _ in pts[1]]
#         bottomRight = [int(_) for _ in pts[2]]
#         bottomLeft = [int(_) for _ in pts[3]]

#         cv2.line(roi_img, topLeft, topRight, (0,255,0), 2)
#         cv2.line(roi_img, topRight, bottomRight, (0,255,0), 2)
#         cv2.line(roi_img, bottomRight, bottomLeft, (0,255,0), 2)
#         cv2.line(roi_img, bottomLeft, topLeft, (0,255,0), 2)
#         roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)
        
#         print(text)

# cv2.imshow('Original', img)
# cv2.imshow('ROI', roi_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()







import numpy as np
import platform
from PIL import ImageFont, ImageDraw, Image

import uuid
import json
import time
import cv2
import requests

# def is_chord(text):
#     first_char = text[0] if len(text) > 0 else ''
#     second_char = text[1] if len(text) > 1 else ''
#     third_char = text[2] if len(text) > 2 else ''

#     if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#         return True

#     if second_char in ['#', 'b', 'm', '7', 'sus', 'aug', 'dim', 'M', 'add']:
#         return True

#     if third_char == '' or third_char.isdigit():
#         return True

#     return False


def transpose_chord(chord, half_steps):
    # 코드를 구성하는 음계 리스트
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    # 코드가 속한 음계와 음계 내에서의 인덱스를 구함
    root_note = chord[0]
    root_index = notes.index(root_note)
    
    # 반음 간격에 따라 음계 인덱스를 조정하고 변환된 코드를 반환
    new_index = (root_index + half_steps) % 12
    return notes[new_index] + chord[1:]



api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

path = 'ekg.png'
files = [('file', open(path,'rb'))]

request_json = {'images': [{'format': 'jpg',
                                'name': 'demo'
                               }],
                    'requestId': str(uuid.uuid4()),
                    'version': 'V2',
                    'timestamp': int(round(time.time() * 1000))
                   }
 
payload = {'message': json.dumps(request_json).encode('UTF-8')}
 
headers = {
  'X-OCR-SECRET': secret_key,
}
 
response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
result = response.json()


img = cv2.imread(path)
roi_img = img.copy()
roi_img2 = img.copy()
font_italic = cv2.FONT_ITALIC

for field in result['images'][0]['fields']:
    text = field['inferText']
    first_char = text[0] if len(text) > 0 else '' # 첫 번째 문자
    second_char = text[1] if len(text) > 1 else '' # 두 번째 문자
    third_char = text[2] if len(text) > 2 else '' # 세 번째 문자

    if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        vertices_list = field['boundingPoly']['vertices']
        pts = [tuple(vertice.values()) for vertice in vertices_list]
        topLeft = [int(_) for _ in pts[0]]
        topRight = [int(_) for _ in pts[1]]
        bottomRight = [int(_) for _ in pts[2]]
        bottomLeft = [int(_) for _ in pts[3]]

        fill_img = cv2.rectangle(roi_img, tuple(topLeft), tuple(bottomRight), (255,255,255), thickness=-1) # 코드(chord)부분을 흰색도형으로 지우기
        change = transpose_chord(text, 4)
        
        new_code = cv2.putText(fill_img, change, (topLeft[0], topLeft[1]+20), font_italic, 1, (0,0,0), 2, cv2.LINE_AA)
        
        print(change)

cv2.imshow('Original', img)
cv2.imshow('ROI', roi_img)
cv2.imshow('NEW_Chord', new_code)
cv2.imwrite('egknone.png', roi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
