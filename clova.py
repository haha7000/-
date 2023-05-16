from PIL import ImageFont, ImageDraw, Image

import uuid
import json
import time
import cv2
import requests

def transpose_chord(chord, half_steps): # 코드 변환 함수
    # 코드를 구성하는 음계 리스트
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    # 코드가 속한 음계와 음계 내에서의 인덱스를 구함
    root_note = chord[0]
    root_index = notes.index(root_note)
    
    # 반음 간격에 따라 음계 인덱스를 조정하고 변환된 코드를 반환
    new_index = (root_index + half_steps) % 12
    return notes[new_index] + chord[1:]

def modify_text(text): #잘못 인식된 코드 바꿔주는 함수
    replaced_text = text.replace("t", "#")
    return replaced_text


api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

path = 'fly.png'
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
        change = transpose_chord(text, 4)
        new_code = cv2.putText(fill_img, change, (topLeft[0], topLeft[1]+20), font_italic, 0.7, (0,0,0), 1, cv2.LINE_AA)
        
        print(change)

cv2.imshow('Original', img)
cv2.imshow('NEW_Chord', new_code)
cv2.imwrite('egknone.png', roi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
