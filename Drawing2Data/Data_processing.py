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
    fixed_floor2_xy = []
    fixed_floor3_xy = []
    seat_z = []


    fr = open(dataFile, 'r')
    lines = fr.readlines()
    for line in lines:
        line = line.strip()  # remove newline
        split_line = line.split(' ')
        split_line = [item for item in split_line if item!=""]
        split_line = [item for item in split_line if item!="[["]

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
    
    stage_xyz = []
    wall_xyz = []

    stage_x_min = stage_h[0]
    stage_x_max = max(stage_xy, key=lambda x:x[0])[0]
    stage_y_min = min(stage_xy, key=lambda x:x[1])[1]
    stage_y_max = max(stage_xy, key=lambda x:x[1])[1]
    stage_z_min = stage_h[1]
    stage_z_max = max(seat_z)

    stage_xyz.append((stage_x_min, stage_y_min, stage_z_min))
    stage_xyz.append((stage_x_min, stage_y_min, stage_z_max))
    stage_xyz.append((stage_x_min, stage_y_max, stage_z_min))
    stage_xyz.append((stage_x_min, stage_y_max, stage_z_max))
    stage_xyz.append((stage_x_max, stage_y_min, stage_z_min))
    stage_xyz.append((stage_x_max, stage_y_min, stage_z_max))
    stage_xyz.append((stage_x_max, stage_y_max, stage_z_min))
    stage_xyz.append((stage_x_max, stage_y_max, stage_z_max))
    
    wall_xyz.append((wall_h[0], stage_y_min, wall_h[1]))
    wall_xyz.append((wall_h[0], stage_y_min, stage_z_max))
    wall_xyz.append((wall_h[0], stage_y_max, wall_h[1]))
    wall_xyz.append((wall_h[0], stage_y_max, stage_z_max))
    wall_xyz.append((wall_h[0] + 32, stage_y_min, wall_h[1]))
    wall_xyz.append((wall_h[0] + 32, stage_y_min, stage_z_max))
    wall_xyz.append((wall_h[0] + 32, stage_y_max, wall_h[1]))
    wall_xyz.append((wall_h[0] + 32, stage_y_max, stage_z_max))
    
    diff_2 = (min(floor2_point_xy, key=lambda x:x[0])[0] - min(floor1_point_xy, key=lambda x:x[0])[0] ,
              min(floor2_point_xy, key=lambda x:x[1])[1] - min(floor1_point_xy, key=lambda x:x[1])[1])
    diff_3 = (min(floor3_point_xy, key=lambda x:x[0])[0] - min(floor1_point_xy, key=lambda x:x[0])[0] ,
              min(floor3_point_xy, key=lambda x:x[1])[1] - min(floor1_point_xy, key=lambda x:x[1])[1])

    for pt in floor2_xy:
        fixed_floor2_xy.append((pt[0] - diff_2[0], pt[1] - diff_2[1]))

    for pt in floor3_xy:
        fixed_floor3_xy.append((pt[0] - diff_3[0], pt[1] - diff_3[1]))

    
    seat_z.sort()
    floor1_xy.sort()
    fixed_floor2_xy.sort()
    fixed_floor3_xy.sort()


    sorted_floor1_seat = sorted(floor1_xy, key=lambda x:x[1])
    sorted_floor2_seat = sorted(fixed_floor2_xy, key=lambda x:x[1])
    sorted_floor3_seat = sorted(fixed_floor3_xy, key=lambda x:x[1])
    

    f = open(dataFile, 'w')

    for pt in floor1_point_xy:
        f.write("point ")
        f.write("%f "%pt[0])
        f.write("%f\n"%pt[1])

    for pt in stage_xyz:
        f.write("stage ")
        f.write("%f "%pt[0])
        f.write("%f "%pt[1])
        f.write("%f\n"%pt[2])

    for pt in wall_xyz:
        f.write("wall ")
        f.write("%f "%pt[0])
        f.write("%f "%pt[1])
        f.write("%f\n"%pt[2])
    
    for pt in seat_z:
        f.write("h ")
        f.write("%f\n"%pt)

    for pt in floor1_xy:
        f.write("1 ")
        f.write("%f "%pt[0])
        f.write("%f\n"%pt[1])
        
    for pt in fixed_floor2_xy:
        f.write("2 ")
        f.write("%f "%pt[0])
        f.write("%f\n"%pt[1])

    for pt in fixed_floor3_xy:
        f.write("3 ")
        f.write("%f "%pt[0])
        f.write("%f\n"%pt[1])

    

    f.close()
