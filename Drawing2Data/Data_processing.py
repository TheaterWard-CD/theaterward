import cv2
import numpy as np
from matplotlib import pyplot as plt

def data_processing(dataFile):

    stage_xy = []
    floor1_xy = []
    floor2_xy = []
    floor3_xy = []
    floor1_point_xy = []
    floor2_point_xy = []
    floor3_point_xy = []
    seat_z = []


    fr = open(dataFile, 'r')
    lines = fr.readlines()
    for line in lines:
        line = line.strip()  # remove newline
        split_line = line.split(' ')

        if (split_line[0] == "stage"):            
            stage_xy.append((float(split_line[1].strip("[""]")), float(split_line[2].strip("[""]"))))
        elif (split_line[0] == "1"):
            floor1_xy.append((float(split_line[1]), float(split_line[2])))
        elif (split_line[0] == "2"):
            floor2_xy.append((float(split_line[1]), float(split_line[2])))
        elif (split_line[0] == "3"):
            floor3_xy.append((float(split_line[1]), float(split_line[2])))
        elif (split_line[0] == "1point"):
            floor1_point_xy.append((float(split_line[1]), float(split_line[2]), float(split_line[3]) - float(split_line[1])))
        elif (split_line[0] == "2point"):
            floor2_point_xy.append((float(split_line[1]), float(split_line[2]), float(split_line[3]) - float(split_line[1])))
        elif (split_line[0] == "3point"):
            floor3_point_xy.append((float(split_line[1]), float(split_line[2]), float(split_line[3]) - float(split_line[1])))
        elif (split_line[0] == "stage_h"):
            stage_h = (float(split_line[1].strip("[""]")), float(split_line[2].strip("[""]")))
        elif (split_line[0] == "wall_h"):
            wall_h = (float(split_line[1].strip("[""]")), float(split_line[2].strip("[""]")))
        elif (split_line[0] == "h"):
            seat_z.append(float(split_line[2]))

        print(line)
    fr.close()

    stage_xy = stage_xy.sort()
    floor1_xy = floor1_xy.sort()
    floor2_xy = floor2_xy.sort()
    floor3_xy = floor3_xy.sort()
    floor1_point_xy = floor1_point_xy.sort()
    floor2_point_xy = floor2_point_xy.sort()
    floor3_point_xy = floor3_point_xy.sort()
    seat_z = seat_z.sort()

    
    stage_xyz = []
    wall_xyz = []

    stage_x_min = stage_h[0]
    stage_x_max = max(stage_xy, key=lambda x:x[0])
    stage_y_min = min(stage_xy, key=lambda x:x[1])
    stage_y_max = max(stage_xy, key=lambda x:x[1])
    stage_z_min = stage_h[1]
    stage_z_max = max(seat_z)

    
    
    

    32


    f = open(dataFile, 'w')

    



    f.close()


    
    

