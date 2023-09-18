from PIL import ImageFont, ImageDraw, Image

import uuid
import json
import time
import cv2
import requests


def transpose_chord(chord, half_steps): # #이 인식되었을 때
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    root_note = chord[0]
    root_index = notes.index(root_note)
    
    new_index = (root_index + half_steps) % 12
    return notes[new_index] + chord[1:]


    notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    
    root_note = chord[:-1]
    accidental = chord[-1] if len(chord) > 1 else ''
    
    root_index = notes.index(root_note)
    
    new_index = (root_index + half_steps) % 12
    new_note = notes[new_index]
    
    return new_note + accidental


def modify_text(text):
    replaced_text = text.replace("t", "#")
    replaced_text = replaced_text.replace("&", "#")
    return replaced_text


api_url = 'your_key'
secret_key = 'your_key'

path = 'hj2.jpeg'
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
        text = modify_text(text)
        change = transpose_chord(text, 2)
        
        new_code = cv2.putText(fill_img, change, (topLeft[0], topLeft[1]+10), font_italic, 0.5, (0,0,0), 2, cv2.LINE_AA)

        print(change)
cv2.imshow("realOri", img)
cv2.imshow('swap', roi_img)
# cv2.imwrite('egknone.png', new_code)
cv2.waitKey(0)
cv2.destroyAllWindows()



# from PIL import ImageFont, ImageDraw, Image

# import uuid
# import json
# import time
# import cv2
# import requests


# def transpose_chord(chord, half_steps):
#     notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
#     root_note = chord[0]
#     root_index = notes.index(root_note)
    
#     new_index = (root_index + half_steps) % 12
#     return notes[new_index] + chord[1:]

# def modify_text(text):
#     replaced_text = text.replace("t", "#")
#     replaced_text = replaced_text.replace("&", "#")
#     replaced_text = replaced_text.replace("H", "#")
#     return replaced_text


# api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
# secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

# path = 'imu.jpeg'
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
# font_italic = cv2.FONT_ITALIC


# import os

# # 저장할 폴더 이름
# save_directory = 'chord_image'
# if not os.path.exists(save_directory):
#     os.makedirs(save_directory)

# for field in result['images'][0]['fields']:
#     text = field['inferText']
#     first_char = text[0] if len(text) > 0 else '' 
#     second_char = text[1] if len(text) > 1 else ''
#     third_char = text[2] if len(text) > 2 else ''

#     if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#         vertices_list = field['boundingPoly']['vertices']
#         pts = [tuple(vertice.values()) for vertice in vertices_list]
#         topLeft = [int(_) for _ in pts[0]]
#         topRight = [int(_) for _ in pts[1]]
#         bottomRight = [int(_) for _ in pts[2]]
#         bottomLeft = [int(_) for _ in pts[3]]
        
#         fill_img = cv2.rectangle(roi_img, tuple(topLeft), tuple(bottomRight), (255,0,255), thickness=1) # 코드(chord)부분을 흰색도형으로 지우기
#         text = modify_text(text)
#         change = transpose_chord(text, -3)
        
#         new_code = cv2.putText(fill_img, change, (topLeft[0], topLeft[1]+10), font_italic, 0.5, (0,0,0), 2, cv2.LINE_AA)

#         # 바운딩 박스 영역 잘라내기
#         crop_img = img[topLeft[1]:bottomRight[1], topLeft[0]:topRight[0]]
        
#         # 잘라낸 이미지를 파일로 저장
#         file_name = f"{save_directory}/{text}.png"
#         cv2.imwrite(file_name, crop_img) 
        


# # ... 나머지 코드
# cv2.imshow("ori", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
