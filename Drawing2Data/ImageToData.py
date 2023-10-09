import cv2
import numpy as np
from matplotlib import pyplot as plt
from drawing2XYdata import drawing2XYdata
from drawing2Zdata import drawing2Zdata




if __name__ == "__main__":

    #drawing image address
    drawing_floor1 = "stage_drawing\stage_drawing_bluesqure/bluesqure1.jpg"
    drawing_floor2 = "stage_drawing\stage_drawing_bluesqure/bluesqure2.jpg"
    drawing_floor3 = "stage_drawing\stage_drawing_bluesqure/bluesqure3.jpg"
    drawing_side = "stage_drawing\stage_drawing_bluesqure/bluesqure_side.jpg"
    
    #seat template address
    seat_template = "stage_drawing\stage_drawing_bluesqure/seat_template.jpg"
    seat_templateL1 = "stage_drawing\stage_drawing_bluesqure/seat_templateL.jpg"
    seat_templateR1 = "stage_drawing\stage_drawing_bluesqure/seat_templateR.jpg"
    seat_templateL2 = "stage_drawing\stage_drawing_bluesqure/seat_templateL2.jpg"
    seat_templateR2 = "stage_drawing\stage_drawing_bluesqure/seat_templateR2.jpg"
    seat_side_template = "stage_drawing\stage_drawing_bluesqure/seat_side_template.jpg"

    #result jpg file name
    floor1_name = "bluesqure_floor1.jpg"
    floor2_name = "bluesqure_floor2.jpg"
    floor3_name = "bluesqure_floor3.jpg"
    side_name = "bluesqure_side.jpg"

    #datafile name
    dataFile = "DrawingData.txt"

    #reset datafile
    f = open(dataFile, 'w', encoding='utf-8')
    f.write("")
    f.close()

    #make xy data from image file
    drawing2XYdata(drawing_floor1, seat_template, seat_templateL1, seat_templateR1, floor1_name, dataFile, 1)
    drawing2XYdata(drawing_floor2, seat_template, seat_templateL2, seat_templateR2, floor2_name, dataFile, 2)
    drawing2XYdata(drawing_floor3, seat_template, seat_templateL2, seat_templateR2, floor3_name, dataFile, 3)

    drawing2Zdata(drawing_side, seat_side_template, side_name)
    
    print("end")



