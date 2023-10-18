import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def drawing2Zdata(input_side_drawing, input_side_seat_template, result_image_name, dataFile):

    #file open
    f = open(dataFile, 'a', encoding='utf-8')

    #input drawing
    input_image = cv2.imread(input_side_drawing, cv2.IMREAD_ANYCOLOR)

    #resize drawing
    input_image = cv2.pyrDown(input_image)
    input_image = input_image[80:1580, 90:2390]

    #input seat template
    seat_template = cv2.imread(input_side_seat_template, 0)

    #resize seat template
    seat_template = cv2.pyrDown(seat_template)

    w, h = seat_template.shape[::-1]

    #change gray
    gray = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

    #match template
    result = cv2.matchTemplate(gray, seat_template, cv2.TM_CCOEFF_NORMED)

    #blue(stage)
    mask_blue = cv2.inRange(input_image, (185,40,40), (255,165,165))
    input_image[mask_blue==255] = (0,0,255)

    contours = cv2.findContours(mask_blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)        
    for contour in contours[0]:
        f.write("stage_h %s\n"%contour[0])
        
    #yellow(wall)
    mask_yellow = cv2.inRange(input_image, (0,230,230), (182,255,255))
    input_image[mask_yellow==255] = (0,0,255)

    contours = cv2.findContours(mask_yellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)        
    for contour in contours[0]:
        f.write("wall_h %s\n"%contour[0])


    #set threshold
    threshold = 0.75

    #
    loc = np.where( result >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(input_image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
        
    loc_ = np.stack([np.array(loc[0]), np.array(loc[1])], axis=0)
    seat_h_loc = loc_.T
    kmeans_h = KMeans(n_clusters=38, init="k-means++")
    kmeans_h.fit(seat_h_loc)
    seat_h = kmeans_h.cluster_centers_
    for pt in seat_h:
        point = (round(pt[1]), round(pt[0]))
        cv2.line(input_image, point, point, (255,0,0), 7)
        f.write("h")        
        f.write(" %f"%(point[0]+w/2))
        f.write(" %f\n"%(point[1]+h/2))
        
    

    #make result image
    cv2.imwrite(result_image_name, input_image)
            
    #file close
    f.close()
