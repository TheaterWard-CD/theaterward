import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def drawing2XYdata(input_drawing, input_seat_template, input_seat_templateL, input_seat_templateR, input_matching_point, result_image_name, dataFile, floor, seat_num):
    
    
    #datafile open
    f = open(dataFile, 'a', encoding='utf-8')

    #input drawing
    input_image = cv2.imread(input_drawing, cv2.IMREAD_ANYCOLOR)

    #resize drawing
    input_image = cv2.pyrDown(input_image)
    input_image = input_image[80:1580, 90:2390]

    #input seat template
    seat_template = cv2.imread(input_seat_template, 0)
    seat_templateL = cv2.imread(input_seat_templateL, 0)
    seat_templateR = cv2.imread(input_seat_templateR, 0)
    matching_point = cv2.imread(input_matching_point, 0)

    #resize seat template
    seat_template = cv2.pyrDown(seat_template)
    seat_templateL = cv2.pyrDown(seat_templateL)
    seat_templateR = cv2.pyrDown(seat_templateR)
    matching_point = cv2.pyrDown(matching_point)

    w, h = seat_template.shape[::-1]
    wl, hl = seat_templateL.shape[::-1]
    wr, hr = seat_templateR.shape[::-1]
    wm, hm = matching_point.shape[::-1]

    #remove color
    bgr = input_image[:,:,0:3]
    
    ##remove red
    bgr = input_image[:,:,0:3]
    mask_red = cv2.inRange(bgr, (40,40,185), (165,165,255))
    bgr_red = bgr.copy()
    bgr_red[mask_red==255] = (255,255,255)

    ##remove blue
    mask_blue = cv2.inRange(bgr_red, (185,40,40), (255,165,165))
    #mask_blue = cv2.inRange(bgr_red, (185,40,40), (255,255,255))
    bgr_new = bgr_red.copy()
    bgr_new[mask_blue==255] = (255,255,255)
    
    #remove color result
    image_remove_color = bgr_new
    
    
    #stage data
    if(floor==1):
        contours = cv2.findContours(mask_blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)        
        for contour in contours[0]:
            f.write("stage %s\n"%contour[0])
            #print(floor, contour[0])
    
    
    #set threshold
    threshold = 0.815    
    
    #change gray
    gray = cv2.cvtColor(image_remove_color, cv2.COLOR_RGB2GRAY)

    #match template
    result1 = cv2.matchTemplate(gray, seat_template, cv2.TM_CCOEFF_NORMED)
    resultL = cv2.matchTemplate(gray, seat_templateL, cv2.TM_CCOEFF_NORMED)
    resultR = cv2.matchTemplate(gray, seat_templateR, cv2.TM_CCOEFF_NORMED)
    resultM = cv2.matchTemplate(gray, matching_point, cv2.TM_CCOEFF_NORMED)

    #middle block
    loc1 = np.where( result1 >= threshold)
    for pt in zip(*loc1[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
    #left block
    locL = np.where( resultL >= threshold)
    for pt in zip(*locL[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wl, pt[1] + hl), (0,0,255), 2)
        
    #right block
    locR = np.where( resultR >= threshold)
    for pt in zip(*locR[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wr, pt[1] + hr), (0,0,255), 2)
        

    #seat klustering
    loc1_ = np.stack([np.array(loc1[0]), np.array(loc1[1])], axis=0)
    locL_ = np.stack([np.array(locL[0]), np.array(locL[1])], axis=0)
    locR_ = np.stack([np.array(locR[0]), np.array(locR[1])], axis=0)
    
    seat_loc = np.concatenate((loc1_.T, locL_.T, locR_.T), axis=0)
    kmeans_seat = KMeans(n_clusters=seat_num, init="k-means++")
    kmeans_seat.fit(seat_loc)
    seat = kmeans_seat.cluster_centers_
    for pt in seat:
        point = (round(pt[1]), round(pt[0]))
        cv2.line(image_remove_color, point, point, (255,0,0), 7)
        f.write("%d"%floor)
        f.write(" %f"%(point[0]+w/2))
        f.write(" %f\n"%(point[1]+h/2))
        
    


    locM = np.where( resultM >= 0.9)
    for pt in zip(*locM[::-1]):
        cv2.rectangle(image_remove_color, pt, (pt[0] + wm, pt[1] + hm), (0,0,255), 2)
        #print( pt[0]+wm/2, pt[1]+hm/2)
        
    locM_ = np.stack([np.array(locM[0]), np.array(locM[1])], axis=0)
    point_loc = locM_.T
    kmeans_point = KMeans(n_clusters=13, init="k-means++")
    kmeans_point.fit(point_loc)
    match = kmeans_point.cluster_centers_
    for pt in match:
        point = (round(pt[1]), round(pt[0]))
        cv2.line(image_remove_color, point, point, (0,200,200), 7)
        f.write("%dpoint"%floor)
        f.write(" %f"%(point[0]))
        f.write(" %f,"%(point[1]))
        f.write(" %f"%(point[0]+wm))
        f.write(" %f\n"%(point[1]+hm))



    #make result image
    cv2.imwrite(result_image_name, image_remove_color)
    
    
    #file close
    f.close()

    


