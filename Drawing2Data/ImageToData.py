import cv2
import numpy as np
from matplotlib import pyplot as plt
from drawing2XYdata import drawing2XYdata
from drawing2Zdata import drawing2Zdata
from Data_processing import data_processing



if __name__ == "__main__":

    #drawing image address
    drawing_floor1 = "stage_drawing\stage_drawing_bluesqure/floor1.jpg"
    drawing_floor2 = "stage_drawing\stage_drawing_bluesqure/floor2.jpg"
    drawing_floor3 = "stage_drawing\stage_drawing_bluesqure/floor3.jpg"
    drawing_side = "stage_drawing\stage_drawing_bluesqure/side_copy3.jpg"
    
    #seat template address
    seat_template = "stage_drawing\stage_drawing_bluesqure/seat_template.jpg"
    seat_templateL1 = "stage_drawing\stage_drawing_bluesqure/seat_templateL.jpg"
    seat_templateR1 = "stage_drawing\stage_drawing_bluesqure/seat_templateR.jpg"
    seat_templateL2 = "stage_drawing\stage_drawing_bluesqure/seat_templateL2.jpg"
    seat_templateR2 = "stage_drawing\stage_drawing_bluesqure/seat_templateR2.jpg"
    seat_side_template = "stage_drawing\stage_drawing_bluesqure/seat_side_template.jpg"

    #real first floor seat number 958      second floor 430     third floor 270 
    seat_num1 = 936
    seat_num2 = 391
    seat_num3 = 256
    

    matching_point = "stage_drawing\stage_drawing_bluesqure/check_point.jpg"

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
    drawing2XYdata(drawing_floor1, seat_template, seat_templateL1, seat_templateR1, matching_point, floor1_name, dataFile, 1, seat_num1)
    drawing2XYdata(drawing_floor2, seat_template, seat_templateL2, seat_templateR2, matching_point, floor2_name, dataFile, 2, seat_num2)
    drawing2XYdata(drawing_floor3, seat_template, seat_templateL2, seat_templateR2, matching_point, floor3_name, dataFile, 3, seat_num3)
    
    #make z data from image file
    drawing2Zdata(drawing_side, seat_side_template, side_name, dataFile)
    
    print("z end")

    data_processing(dataFile)
    print("end")


