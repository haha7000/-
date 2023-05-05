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


import numpy as np
import platform
from PIL import ImageFont, ImageDraw, Image
from matplotlib import pyplot as plt
 
import uuid
import json
import time
import cv2
import requests

def plt_imshow(title='image', img=None, figsize=(8 ,5)):
    plt.figure(figsize=figsize)
 
    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []
 
            for i in range(len(img)):
                titles.append(title)
 
        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
 
            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
 
        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()

# def is_chord(text):
#     if text[0].isupper():
#         return True
#     return False

def is_chord(text):
    if text[0].isupper() and text[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        return True

    if len(text) > 1:
        second_char = text[1]

    if text[0].isupper() or second_char in ['#', 'b', 'm', '7', 'sus', 'aug', 'dim', 'M', 'add']:
        return True

    return False

def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
    if type(image) == np.ndarray:
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(color_coverted)
 
    if platform.system() == 'Darwin':
        font = 'AppleGothic.ttf'
    elif platform.system() == 'Windows':
        font = 'malgun.ttf'
        
    image_font = ImageFont.truetype(font, font_size)
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)
 
    #draw.text((x, y), text, font=image_font, fill=color)
    
    numpy_image = np.array(image)
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
 
    return opencv_image


api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

path = 'hj.jpeg'
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

font_italic = "FONT_ITALIC"

for field in result['images'][0]['fields']:
    text = field['inferText']
    if text and text[0].isupper():
        vertices_list = field['boundingPoly']['vertices']
        pts = [tuple(vertice.values()) for vertice in vertices_list]
        topLeft = [int(_) for _ in pts[0]]
        topRight = [int(_) for _ in pts[1]]
        bottomRight = [int(_) for _ in pts[2]]
        bottomLeft = [int(_) for _ in pts[3]]

        cv2.line(roi_img, topLeft, topRight, (0,255,0), 2)
        cv2.line(roi_img, topRight, bottomRight, (0,255,0), 2)
        cv2.line(roi_img, bottomRight, bottomLeft, (0,255,0), 2)
        cv2.line(roi_img, bottomLeft, topLeft, (0,255,0), 2)
        roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)
        
        print(text)

plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))


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



