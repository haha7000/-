import functions as fs
import cv2

def recognize_key(image, staves, stats):
    (x, y, w, h, area) = stats
    ts_conditions = (
        staves[0] + fs.weighted(5) >= y >= staves[0] - fs.weighted(5) and  # 상단 위치 조건
        staves[4] + fs.weighted(5) >= y + h >= staves[4] - fs.weighted(5) and  # 하단 위치 조건
        staves[2] + fs.weighted(5) >= fs.get_center(y, h) >= staves[2] - fs.weighted(5) and  # 중단 위치 조건
        fs.weighted(18) >= w >= fs.weighted(10) and  # 넓이 조건
        fs.weighted(45) >= h >= fs.weighted(35)  # 높이 조건
    )
    if ts_conditions:
        return True, 0
    else:  # 조표가 있을 경우 (다장조를 제외한 모든 조)
        stems = fs.stem_detection(image, stats, 20)
        if stems[0][0] - x >= fs.weighted(3):  # 직선이 나중에 발견되면
            key = int(10 * len(stems) / 2)  # 샾
        else:  # 직선이 일찍 발견되면
            key = 100 * len(stems)  # 플랫

    return False, key





def recognize_note(image, staff, stats, stems, direction):
    (x, y, w, h, area) = stats
    notes = []
    pitches = []
    note_condition = (
        len(stems) and
        w >= fs.weighted(10) and  # 넓이 조건
        h >= fs.weighted(35) and  # 높이 조건
        area >= fs.weighted(95)  # 픽셀 갯수 조건
    )
    if note_condition:
        for i in range(len(stems)):
            stem = stems[i]
            head_exist, head_fill, head_center = recognize_note_head(image, stem, direction)
            if head_exist:
                recognize_note_tail(image, i, stem, direction)

    pass





def recognize_note_head(image, stem, direction):
    (x, y, w, h) = stem
    if direction:  # 정 방향 음표
        area_top = y + h - fs.weighted(7)  # 음표 머리를 탐색할 위치 (상단)
        area_bot = y + h + fs.weighted(7)  # 음표 머리를 탐색할 위치 (하단)
        area_left = x - fs.weighted(14)  # 음표 머리를 탐색할 위치 (좌측)
        area_right = x  # 음표 머리를 탐색할 위치 (우측)
    else:  # 역 방향 음표
        area_top = y - fs.weighted(7)  # 음표 머리를 탐색할 위치 (상단)
        area_bot = y + fs.weighted(7)  # 음표 머리를 탐색할 위치 (하단)
        area_left = x + w  # 음표 머리를 탐색할 위치 (좌측)
        area_right = x + w + fs.weighted(14)  # 음표 머리를 탐색할 위치 (우측)

    cnt = 0  # cnt = 끊기지 않고 이어져 있는 선의 개수를 셈
    cnt_max = 0  # cnt_max = cnt 중 가장 큰 값
    head_center = 0
    pixel_cnt = fs.count_rect_pixels(image, (area_left, area_top, area_right - area_left, area_bot - area_top))

    for row in range(area_top, area_bot):
        col, pixels = fs.get_line(image, fs.HORIZONTAL, row, area_left, area_right, 5)
        pixels += 1
        if pixels >= fs.weighted(5):
            cnt += 1
            cnt_max = max(cnt_max, pixels)
            head_center += row

    head_exist = (cnt >= 3 and pixel_cnt >= 50)
    head_fill = (cnt >= 8 and cnt_max >= 9 and pixel_cnt >= 80)
    head_center /= cnt

    return head_exist, head_fill, head_center



def recognize_note_tail(image, index, stem, direction):
    (x, y, w, h) = stem
    if direction:  # 정 방향 음표
        area_top = y  # 음표 꼬리를 탐색할 위치 (상단)
        area_bot = y + h - fs.weighted(15)  # 음표 꼬리를 탐색할 위치 (하단)
    else:  # 역 방향 음표
        area_top = y + fs.weighted(15)  # 음표 꼬리를 탐색할 위치 (상단)
        area_bot = y + h  # 음표 꼬리를 탐색할 위치 (하단)
    if index:
        area_col = x - fs.weighted(4)  # 음표 꼬리를 탐색할 위치 (열)
    else:
        area_col = x + w + fs.weighted(4)  # 음표 꼬리를 탐색할 위치 (열)
        
    pass