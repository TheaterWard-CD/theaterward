import cv2
import numpy as np
from matplotlib import pyplot as plt



def drawing2XYdata(input_drawing, input_seat_template, input_seat_templateL, input_seat_templateR, result_image_name, dataFile, floor):
    
    #input drawing
    input_image = cv2.imread(input_drawing, cv2.IMREAD_ANYCOLOR)

    #resize drawing
    input_image = cv2.pyrDown(input_image)
    
    #input seat template
    seat_template = cv2.imread(input_seat_template, 0)
    seat_templateL = cv2.imread(input_seat_templateL, 0)
    seat_templateR = cv2.imread(input_seat_templateR, 0)

    #resize seat template
    seat_template = cv2.pyrDown(seat_template)
    seat_templateL = cv2.pyrDown(seat_templateL)
    seat_templateR = cv2.pyrDown(seat_templateR)

    w, h = seat_template.shape[::-1]
    wl, hl = seat_templateL.shape[::-1]
    wr, hr = seat_templateR.shape[::-1]

    #remove color
    bgr = input_image[:,:,0:3]
    
    ##remove red
    bgr = input_image[:,:,0:3]
    mask_red = cv2.inRange(bgr, (40,40,185), (255,255,255))
    bgr_red = bgr.copy()
    bgr_red[mask_red==255] = (255,255,255)

    ##remove blue
    mask_blue = cv2.inRange(bgr_red, (185,40,40), (255,255,255))
    bgr_new = bgr_red.copy()
    bgr_new[mask_blue==255] = (255,255,255)

    #remove color result
    image_remove_color = bgr_new


    #change gray
    gray = cv2.cvtColor(image_remove_color, cv2.COLOR_RGB2GRAY)

    #match template
    result1 = cv2.matchTemplate(gray, seat_template, cv2.TM_CCOEFF_NORMED)
    resultL = cv2.matchTemplate(gray, seat_templateL, cv2.TM_CCOEFF_NORMED)
    resultR = cv2.matchTemplate(gray, seat_templateR, cv2.TM_CCOEFF_NORMED)
    
   
    #datafile open
    f = open(dataFile, 'a', encoding='utf-8')
    
    #set threshold
    threshold = 0.75
    
    #middle block
    loc1 = np.where( result1 >= threshold)
    for pt in zip(*loc1[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print( pt[0]+w/2, pt[1]+h/2)
        f.write("%d"%floor)
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))

    #left block
    locL = np.where( resultL >= threshold)
    for pt in zip(*locL[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wl, pt[1] + hl), (0,0,255), 2)
        print( pt[0]+wl/2, pt[1]+hl/2)
        f.write("%d"%floor)
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))

    #right block
    locR = np.where( resultR >= threshold)
    for pt in zip(*locR[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wr, pt[1] + hl), (0,0,255), 2)
        print( pt[0]+wr/2, pt[1]+hl/2)
        f.write("%d"%floor)
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))

    #make result image
    cv2.imwrite(result_image_name, image_remove_color)
    
    
    #file close
    f.close()

    


