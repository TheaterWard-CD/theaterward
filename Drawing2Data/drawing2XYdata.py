import cv2
import numpy as np
from matplotlib import pyplot as plt



def drawing2XYdata(input_drawing, input_seat_template, input_seat_templateL, input_seat_templateR, result_image_name, dataFile, floor):
    
    #input drawing
    input_image = cv2.imread(input_drawing, cv2.IMREAD_ANYCOLOR)

    #resize drawing
    #input_image = cv2.pyrDown(input_image)
    input_image = cv2.pyrDown(input_image)
    
    #input seat template
    seat_template = cv2.imread(input_seat_template, 0)
    seat_templateL = cv2.imread(input_seat_templateL, 0)
    seat_templateR = cv2.imread(input_seat_templateR, 0)

    #resize seat template
    #seat_template = cv2.pyrDown(seat_template)
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

    image_remove_color = bgr_new


    #change gray
    gray = cv2.cvtColor(image_remove_color, cv2.COLOR_RGB2GRAY)

    '''
    degree = 10
    M1 = cv2.getRotationMatrix2D((w/2, h/2), degree, 1.0)
    M2 = cv2.getRotationMatrix2D((w/2, h/2), -degree, 1.0)
    RotateTemplateL = cv2.warpAffine(seat_template, M1, (w, h))
    RotateTemplateR = cv2.warpAffine(seat_template, M2, (w, h))
    ''' 
    result1 = cv2.matchTemplate(gray, seat_template, cv2.TM_CCOEFF_NORMED)
    resultL = cv2.matchTemplate(gray, seat_templateL, cv2.TM_CCOEFF_NORMED)
    resultR = cv2.matchTemplate(gray, seat_templateR, cv2.TM_CCOEFF_NORMED)
    
    #result2 = cv2.matchTemplate(gray, RotateTemplateL, cv2.TM_CCOEFF_NORMED)
    #result3 = cv2.matchTemplate(gray, RotateTemplateR, cv2.TM_CCOEFF_NORMED)

    f = open(dataFile, 'a', encoding='utf-8')
    

    threshold = 0.75
    
    loc1 = np.where( result1 >= threshold)
    for pt in zip(*loc1[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print( pt[0]+w/2, pt[1]+h/2)
        f.write("%d"%floor)
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))
    locL = np.where( resultL >= threshold)
    for pt in zip(*locL[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wl, pt[1] + hl), (0,0,255), 2)
        print( pt[0]+wl/2, pt[1]+hl/2)
        f.write("%d"%floor)
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))

    locR = np.where( resultR >= threshold)
    for pt in zip(*locR[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wl, pt[1] + hl), (0,0,255), 2)
        print( pt[0]+wl/2, pt[1]+hl/2)
        f.write("%d"%floor)
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))

    '''
    loc2 = np.where( result2 >= threshold)
    for pt in zip(*loc2[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print( pt[0]+w/2, pt[1]+h/2)
        
    loc3 = np.where( result3 >= threshold)
    for pt in zip(*loc3[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print( pt[0]+w/2, pt[1]+h/2)
    '''
    cv2.imwrite(result_image_name, image_remove_color)

    f.close()

    


