import cv2
import numpy as np
from matplotlib import pyplot as plt
from drawing2XYdata import drawing2XYdata
from drawing2Zdata import drawing2Zdata




if __name__ == "__main__":

    drawing_floor1 = "stage_drawing\stage_drawing_bluesqure/bluesqure1.jpg"
    drawing_floor2 = "stage_drawing\stage_drawing_bluesqure/bluesqure2.jpg"
    drawing_floor3 = "stage_drawing\stage_drawing_bluesqure/bluesqure3.jpg"
    drawing_side = "stage_drawing\stage_drawing_bluesqure/bluesqure_side.jpg"
    
    seat_template = "stage_drawing\stage_drawing_bluesqure/seat_template.jpg"
    seat_templateL = "stage_drawing\stage_drawing_bluesqure/seat_templateL.jpg"
    seat_templateR = "stage_drawing\stage_drawing_bluesqure/seat_templateR.jpg"
    seat_side_template = "stage_drawing\stage_drawing_bluesqure/seat_side_template.jpg"

    floor1_name = "bluesqure_floor1.jpg"
    floor2_name = "bluesqure_floor2.jpg"
    floor3_name = "bluesqure_floor3.jpg"
    side_name = "bluesqure_side.jpg"

    dataFile = "DrawingData.txt"

    drawing2XYdata(drawing_floor1, seat_template, seat_templateL, seat_templateR, floor1_name, dataFile, 1)
    drawing2XYdata(drawing_floor2, seat_template, seat_templateL, seat_templateR, floor2_name, dataFile, 2)
    drawing2XYdata(drawing_floor3, seat_template, seat_templateL, seat_templateR, floor3_name, dataFile, 3)

    
    print(1)




'''

#원본 도면 
input_image = cv2.imread("stage_drawing\stage_drawing_bluesqure/bluesqure1.jpg",cv2.IMREAD_ANYCOLOR)
height, width, channel = input_image.shape

#범위내 도면 재설정
changed_image = cv2.pyrDown(input_image)
bluesqure_floor_1 = changed_image[450:1250, 400:1700].copy()


#seat이미지 저장
input_seat_template = cv2.imread("stage_drawing\stage_drawing_bluesqure/seat_template1.jpg", 0)
seat_template = cv2.pyrDown(input_seat_template)

w, h = seat_template.shape[::-1]


#빨간색 제거
bgr = bluesqure_floor_1[:,:,0:3]
mask_red = cv2.inRange(bgr, (40,40,185), (255,255,255))
bgr_red = bgr.copy()
bgr_red[mask_red==255] = (255,255,255)

bluesqure_floor_1_stage = bgr_red

mask_blue = cv2.inRange(bgr_red, (185,40,40), (255,255,255))
bgr_new = bgr_red.copy()
bgr_new[mask_blue==255] = (255,255,255)

cv2.imwrite('bgr_new.jpg', bgr_new)

bluesqure_floor_1 = bgr_new

#흑백으로 변환
gray = cv2.cvtColor(bluesqure_floor_1, cv2.COLOR_RGB2GRAY)

result = cv2.matchTemplate(gray, seat_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( result >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(bluesqure_floor_1, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print( pt[0]+w/2, pt[1]+h/2)
cv2.imwrite('result_image.jpg', bluesqure_floor_1)

'''
