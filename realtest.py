
from flask import Flask, render_template, request, redirect, url_for
from PIL import ImageFont, ImageDraw, Image
import uuid, json, time, cv2, requests
import function as ft

def transpose_chord(chord, half_steps):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    root_note = chord[0]
    root_index = notes.index(root_note)
    
    new_index = (root_index + half_steps) % 12
    return notes[new_index] + chord[1:]


def modify_text(text):
    replaced_text = text.replace("t", "#")
    replaced_text = replaced_text.replace("&", "#")
    return replaced_text


def N_transpose_chord(text, half_steps):
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        path = f'uploads/{str(uuid.uuid4())}.jpg'
        uploaded_file.save(path)

        api_url = 'https://qrzccj1y9c.apigw.ntruss.com/custom/v1/22243/60e2b8a7e366adc85128cffa9fb17254e9c8e9e4a73a7b6eac9c819a718987a3/general'
        secret_key = 'ZkhvZFJGUXd2WFRkVWNrWExGc0RXbU9EaVRGYXZuRkc='

        files = [('file', open(path,'rb'))]

        request_json = {
            'images': [{'format': 'jpg', 'name': 'demo'}],
            'requestId': str(uuid.uuid4()),
            'version': 'V2',
            'timestamp': int(round(time.time() * 1000))
        }

        payload = {'message': json.dumps(request_json).encode('UTF-8')}
        headers = {'X-OCR-SECRET': secret_key}

        response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
        result = response.json()

        font_italic = cv2.FONT_ITALIC
        img = cv2.imread(path)
        roi_img = img.copy()

        for field in result['images'][0]['fields']:
            text = field['inferText']
            first_char = text[0] if len(text) > 0 else '' 
            second_char = text[1] if len(text) > 1 else '' 
            third_char = text[2] if len(text) > 2 else ''

            if first_char.isupper() and first_char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                vertices_list = field['boundingPoly']['vertices']
                pts = [tuple(vertice.values()) for vertice in vertices_list]
                topLeft = [int(_) for _ in pts[0]]
                bottomRight = [int(_) for _ in pts[2]]

                fill_img = cv2.rectangle(roi_img, tuple(topLeft), tuple(bottomRight), (255,255,255), thickness=-1) # 코드(chord)부분을 흰색도형으로 지우기
                text = modify_text(text)
                change = transpose_chord(text, -2)
        
                new_code = cv2.putText(fill_img, change, (topLeft[0], topLeft[1]+10), font_italic, 0.5, (0,0,0), 2, cv2.LINE_AA)

        cv2.imshow("after", roi_img)
        cv2.imwrite(path, roi_img)

        return render_template('result.html', image_path=path)



N_transpose_chord()