import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import mglearn


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

        #read data
        if (split_line[0] == "stage"):      stage_xy.append((int(split_line[1].strip("[""]")), int(split_line[2].strip("[""]"))))
        elif (split_line[0] == "1"):        floor1_xy.append((int(split_line[1]), int(split_line[2])))
        elif (split_line[0] == "2"):        floor2_xy.append((int(split_line[1]), int(split_line[2])))
        elif (split_line[0] == "3"):        floor3_xy.append((int(split_line[1]), int(split_line[2])))
        elif (split_line[0] == "1point"):   floor1_point_xy.append((int(split_line[1]), int(split_line[2]), int(split_line[3]) - int(split_line[1])))
        elif (split_line[0] == "2point"):   floor2_point_xy.append((int(split_line[1]), int(split_line[2]), int(split_line[3]) - int(split_line[1])))
        elif (split_line[0] == "3point"):   floor3_point_xy.append((int(split_line[1]), int(split_line[2]), int(split_line[3]) - int(split_line[1])))
        elif (split_line[0] == "stage_h"):  stage_h = (int(split_line[1].strip("[""]")), int(split_line[2].strip("[""]")))
        elif (split_line[0] == "wall_h"):   wall_h = (int(split_line[1].strip("[""]")), int(split_line[2].strip("[""]")))
        elif (split_line[0] == "h"):        seat_z.append(int(split_line[2]))

    fr.close()
    

    #processing to link each floor
    stage_xyz = []
    wall_xyz = []

    stage_x_min = stage_h[0]
    stage_x_max = max(stage_xy, key=lambda x:x[0])[0]
    stage_y_min = min(stage_xy, key=lambda x:x[1])[1]
    stage_y_max = max(stage_xy, key=lambda x:x[1])[1]
    stage_z_min = stage_h[1]
    stage_z_max = max(seat_z)

    stage_xyz.append((stage_x_min, stage_y_min, stage_z_max - stage_z_min))
    stage_xyz.append((stage_x_min, stage_y_min, stage_z_max - stage_z_max))
    stage_xyz.append((stage_x_min, stage_y_max, stage_z_max - stage_z_min))
    stage_xyz.append((stage_x_min, stage_y_max, stage_z_max - stage_z_max))
    stage_xyz.append((stage_x_max, stage_y_min, stage_z_max - stage_z_min))
    stage_xyz.append((stage_x_max, stage_y_min, stage_z_max - stage_z_max))
    stage_xyz.append((stage_x_max, stage_y_max, stage_z_max - stage_z_min))
    stage_xyz.append((stage_x_max, stage_y_max, stage_z_max - stage_z_max))
    
    wall_xyz.append((wall_h[0], stage_y_min, stage_z_max - wall_h[1]))
    wall_xyz.append((wall_h[0], stage_y_min, stage_z_max - stage_z_max))
    wall_xyz.append((wall_h[0], stage_y_max, stage_z_max - wall_h[1]))
    wall_xyz.append((wall_h[0], stage_y_max, stage_z_max - stage_z_max))
    wall_xyz.append((wall_h[0] + 32, stage_y_min, stage_z_max - wall_h[1]))
    wall_xyz.append((wall_h[0] + 32, stage_y_min, stage_z_max - stage_z_max))
    wall_xyz.append((wall_h[0] + 32, stage_y_max, stage_z_max - wall_h[1]))
    wall_xyz.append((wall_h[0] + 32, stage_y_max, stage_z_max - stage_z_max))

    diff_2 = (min(floor2_point_xy, key=lambda x:x[0])[0] - min(floor1_point_xy, key=lambda x:x[0])[0] ,
              min(floor2_point_xy, key=lambda x:x[1])[1] - min(floor1_point_xy, key=lambda x:x[1])[1])
    diff_3 = (min(floor3_point_xy, key=lambda x:x[0])[0] - min(floor1_point_xy, key=lambda x:x[0])[0] ,
              min(floor3_point_xy, key=lambda x:x[1])[1] - min(floor1_point_xy, key=lambda x:x[1])[1])

    for pt in floor2_xy: fixed_floor2_xy.append((pt[0] - diff_2[0], pt[1] - diff_2[1]))
    for pt in floor3_xy: fixed_floor3_xy.append((pt[0] - diff_3[0], pt[1] - diff_3[1]))
    
    #sorting 
    seat_z.sort()
    floor1_xy.sort()
    fixed_floor2_xy.sort()
    fixed_floor3_xy.sort()

    sorted_floor1_seat = sorted(floor1_xy, key=lambda x:x[1])
    sorted_floor2_seat = sorted(fixed_floor2_xy, key=lambda x:x[1])
    sorted_floor3_seat = sorted(fixed_floor3_xy, key=lambda x:x[1])

    floor1_left_seat = []
    floor1_center_seat = []
    floor1_right_seat = []
    floor2_left_seat = []
    floor2_center_seat = []
    floor2_right_seat = []
    floor3_left_seat = []
    floor3_center_seat = []
    floor3_right_seat = []
    
    for pt in seat_z:
        fixed_pt = stage_z_max - pt
        zidx = seat_z.index(pt)
        seat_z[zidx] = fixed_pt
    seat_z.reverse()

    # data processing for making z coordinates
    boundary_value1 = []
    boundary_value2 = []
    boundary_value3 = []
    temp = sorted_floor1_seat[0]

    #특정한 값을 넘어가는 간격은 boundary로 설정
    for (x,y) in sorted_floor1_seat:
        if(abs(temp[1]-y)>15): boundary_value1.append((x,y))    
        temp=(x,y)

    temp = sorted_floor2_seat[0]
    for (x,y) in sorted_floor2_seat:
        if(abs(temp[1]-y)>15): boundary_value2.append((x,y))    
        temp=(x,y)

    temp = sorted_floor3_seat[0]
    for (x,y) in sorted_floor3_seat:
        if(abs(temp[1]-y)>15): boundary_value3.append((x,y))    
        temp=(x,y)

    #각 층의 boundary값을 기준으로 구역을 나눔
    for (x,y) in sorted_floor1_seat:
        if(y<boundary_value1[0][1]): floor1_left_seat.append((x,y,0))
        elif(y>=boundary_value1[1][1]): floor1_right_seat.append((x,y,0))
        else: floor1_center_seat.append((x,y,0))

    for (x,y) in sorted_floor2_seat:
        if(y<boundary_value2[0][1]): floor2_left_seat.append((x,y,0))
        elif(y>=boundary_value2[1][1]): floor2_right_seat.append((x,y,0))
        else: floor2_center_seat.append((x,y,0))

    for (x,y) in sorted_floor3_seat:
        if(y<boundary_value3[0][1]): floor3_left_seat.append((x,y,0))
        elif(y>=boundary_value3[1][1]): floor3_right_seat.append((x,y,0))
        else: floor3_center_seat.append((x,y,0))
    
    #z값 부여하기
    new_f1ls = make_z_coord(seat_z, floor1_left_seat, 0, 22)
    new_f1cs = make_z_coord(seat_z, floor1_center_seat, 0, 22)
    new_f1rs = make_z_coord(seat_z, floor1_right_seat, 0, 22)

    new_f2ls = make_z_coord(seat_z, floor2_left_seat, 22, 10)
    new_f2cs = make_z_coord(seat_z, floor2_center_seat, 22, 10)
    new_f2rs = make_z_coord(seat_z, floor2_right_seat, 22, 10)

    new_f3ls = make_z_coord(seat_z, floor3_left_seat, 32, 6)
    new_f3cs = make_z_coord(seat_z, floor3_center_seat, 32, 6, fragment=1)
    new_f3rs = make_z_coord(seat_z, floor3_right_seat, 32, 6)

    #좌석 합치기
    final_seats = new_f1ls + new_f1cs + new_f1rs + new_f2ls + new_f2cs + new_f2rs + new_f3ls + new_f3cs + new_f3rs

    # x,y,z = zip(*final_seats)

    # # 3D 산점도 그리기
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(x, y, z, c='r', marker='o')

    # # 축 레이블 설정
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')

    # # 그래프 보여주기
    # plt.show()



    #rewriting data
    f = open(dataFile, 'w')

    for pt in floor1_point_xy:
        f.write("point ")
        f.write("%d "%pt[0])
        f.write("%d\n"%pt[1])

    for pt in stage_xyz:
        f.write("stage ")
        f.write("%d "%pt[0])
        f.write("%d "%pt[1])
        f.write("%d\n"%pt[2])

    for pt in wall_xyz:
        f.write("wall ")
        f.write("%d "%pt[0])
        f.write("%d "%pt[1])
        f.write("%d\n"%pt[2])
    
    for pt in seat_z:        
        f.write("h ")
        f.write("%d\n"%pt)

    for pt in final_seats:
        f.write("seat ")
        f.write("%d "%pt[0])
        f.write("%d "%pt[1])
        f.write("%d\n"%pt[2])

    f.close()


#dbscan을 이용하여 각 좌석의 z값 만들기
def make_z_coord(seat_z, seats, row_init, row_num, fragment = 0):
    model = DBSCAN(eps=22, min_samples=3, metric='manhattan')
    
    labels = model.fit_predict(np.array(seats))    
    for (x,y,z) in seats:
        idx = seats.index((x,y,z))
        seats[idx] = (x,y,labels[idx])

    from mpl_toolkits.mplot3d import Axes3D
    # 데이터를 튜플로 변환
    x, y, z = zip(*seats)
    # 각 클러스터의 x 값 평균 계산
    cluster_x_means = {label: np.mean([xi for xi, yi, zi in zip(x, y, z) if zi == label]) for label in set(z)}

    if fragment!=0:

        # 평균값의 차이가 5 이하인 클러스터를 합치기 위한 딕셔너리 초기화
        merged_clusters = {label: label for label in set(z)}

        # 클러스터를 x 값 평균에 대해 정렬
        sorted_clusters = sorted(cluster_x_means.keys(), key=lambda k: cluster_x_means[k])

        count = 0
        # 평균값의 차이가 5 이하인 클러스터를 합치기
        for i in range(0, len(sorted_clusters)):
            cur_cluster = sorted_clusters[i]
            next_cluster = sorted_clusters[i+1]
            current_mean = cluster_x_means[cur_cluster]
            next_mean = cluster_x_means[next_cluster]

            #값의 차이가 5 이하이면 보다 큰 클러스터링 넘버를 작은값으로 바꾸고 그보다 큰값들의 클러스터링 넘버를 1씩 감소
            if abs(current_mean - next_mean)<=5:
                if(next_cluster>cur_cluster):
                    merged_clusters[next_cluster] = cur_cluster
                    for j in range(next_cluster+1, len(sorted_clusters)):
                        if merged_clusters[j]==0: continue
                        merged_clusters[j] = merged_clusters[j]-1
                else:
                    merged_clusters[cur_cluster] = next_cluster
                    for j in range(cur_cluster+1, len(sorted_clusters)):
                        if merged_clusters[j]==0: continue
                        merged_clusters[j] = merged_clusters[j]-1
                count += 1
            if fragment==count: break;
   
        for (xi,yi,zi) in seats:
            idx = seats.index((xi,yi,zi))
            seats[idx] = (xi,yi, merged_clusters[labels[idx]])
            
        x, y, z = zip(*seats)
        # 각 클러스터의 x 값 평균 계산
        cluster_x_means = {label: np.mean([xi for xi, yi, zi in zip(x, y, z) if zi == label]) for label in set(z)}

    # 클러스터를 x 값 평균에 대해 정렬
    sorted_clusters = sorted(cluster_x_means.keys(), key=lambda k: cluster_x_means[k])
    # 클러스터를 새로운 순서에 따라 z 값을 재설정
    new_z = [sorted_clusters.index(zi) for zi in z]

    # 결과 출력
    new_seats = []
    for point, new_z_value in zip(seats, new_z):
        new_pt = (point[0], point[1], seat_z[row_init + row_num - 1 - new_z_value])
        new_seats.append(new_pt)


    
    return new_seats