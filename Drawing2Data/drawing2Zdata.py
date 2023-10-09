import cv2
import numpy as np
from matplotlib import pyplot as plt

def drawing2Zdata(input_side_drawing, input_side_seat_template, result_image_name, dataFile):

    #input drawing
    input_image = cv2.imread(input_side_drawing, cv2.IMREAD_ANYCOLOR)

    #resize drawing
    input_image = cv2.pyrDown(input_image)

    #input seat template
    seat_template = cv2.imread(input_side_seat_template, 0)

    #resize seat template
    seat_template = cv2.pyrDown(seat_template)

    w, h = seat_template.shape[::-1]

    #change gray
    gray = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

    #match template
    result = cv2.matchTemplate(gray, seat_template, cv2.TM_CCOEFF_NORMED)


    #file open
    f = open(dataFile, 'a', encoding='utf-8')
    
    #set threshold
    threshold = 0.75

    #
    loc = np.where( result >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(input_image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print( pt[0]+w/2, pt[1]+h/2)
        f.write("h")        
        f.write("    %f"%(pt[0]+w/2))
        f.write("    %f\n"%(pt[1]+h/2))

    #make result image
    cv2.imwrite(result_image_name, input_image)
            
    #file close
    f.close()
