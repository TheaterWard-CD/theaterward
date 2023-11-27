#this file will run in Blender
import numpy as np
import bpy
import bmesh


point = []
stage = []
wall = []
height = []
seats = []


#read data file
fr = open("C:\\Users\\user\\Desktop\\CAU\\CAU_3\\2nd_semester\\capstone_1\\DrawingData.txt", 'r', encoding='utf-8')
lines = fr.readlines()

for line in lines:
    line = line.strip()  # remove newline
    split_line = line.split(' ')
        
    if (split_line[0] == "stage"):
        stage.append( (int(split_line[1]), int(split_line[2]), int(split_line[3])) )
    elif (split_line[0] == "point"):
        point.append( (int(split_line[1]), int(split_line[2])) )
    elif (split_line[0] == "wall"):
        wall.append( (int(split_line[1]), int(split_line[2]), int(split_line[3])) )
    elif (split_line[0] == "h"):
        height.append(int(split_line[1]))
    elif (split_line[0] == "seat"):
        seats.append( (int(split_line[1]), int(split_line[2]), int(split_line[3])) )

stage_x_min = float(min(stage, key=lambda x:x[0])[0])/10
stage_x_max = float(max(stage, key=lambda x:x[0])[0])/10
stage_y_min = float(min(stage, key=lambda x:x[1])[1])/10
stage_y_max = float(max(stage, key=lambda x:x[1])[1])/10
stage_z_min = float(min(stage, key=lambda x:x[2])[2])/10
stage_z_max = float(max(stage, key=lambda x:x[2])[2])/10

wall_x_min = float(min(wall, key=lambda x:x[0])[0])/10
wall_x_max = float(max(wall, key=lambda x:x[0])[0])/10
wall_y_min = float(min(wall, key=lambda x:x[1])[1])/10
wall_y_max = float(max(wall, key=lambda x:x[1])[1])/10
wall_z_min = float(min(wall, key=lambda x:x[2])[2])/10
wall_z_max = float(max(wall, key=lambda x:x[2])[2])/10

point_x_min = float(min(point, key=lambda x:x[0])[0])/10
point_x_max = float(max(point, key=lambda x:x[0])[0])/10
point_y_min = float(min(point, key=lambda x:x[1])[1])/10
point_y_max = float(max(point, key=lambda x:x[1])[1])/10






#make stage
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=((stage_x_max + stage_x_min)/2,(stage_y_max + stage_y_min)/2,(stage_z_max + stage_z_min)/2), 
                                scale=(stage_x_max-stage_x_min,stage_y_max-stage_y_min,stage_z_max-stage_z_min))
bpy.context.active_object.name = "Stage"





#make wall
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                location=((wall_x_max + wall_x_min)/2, (wall_y_max + wall_y_min)/2, (max(height)/10+10)/2),
                                scale=(wall_x_max - wall_x_min, point_y_max - point_y_min, max(height)/10+10))
cube = bpy.context.object
bpy.context.active_object.name = "Wall"

# 구멍? 만들ê¸? ?? 기본 직육면체 추�????
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                location=((wall_x_max + wall_x_min)/2, (wall_y_max + wall_y_min)/2, (max(height)/10)/2),
                                scale=(wall_x_max - wall_x_min, wall_y_max - wall_y_min, max(height)/10))
hole_cube = bpy.context.object
bpy.context.active_object.name = "hole"

# Set the hole cube's origin to its center
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')

# Add a boolean modifier to the main cube
bool_modifier = cube.modifiers.new(name="Boolean", type='BOOLEAN')
bool_modifier.operation = 'DIFFERENCE'
bool_modifier.use_self = True


# Set the hole cube as the target for the boolean modifier
bool_modifier.object = hole_cube

# Apply the boolean modifier
bpy.ops.object.modifier_apply({"object": cube}, modifier='Boolean')

# Delete the hole cube
bpy.data.objects.remove(hole_cube)



bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=((point_x_max + point_x_min)/2,(point_y_max + point_y_min)/2, stage_z_min -1), 
                                scale=(point_x_max-point_x_min,point_y_max-point_y_min, 1))
bpy.context.active_object.name = "floor"

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=((point_x_max + point_x_min)/2,(point_y_max + point_y_min)/2, max(height)/10 + 10 +0.5), 
                                scale=(point_x_max-point_x_min,point_y_max-point_y_min, 1))
bpy.context.active_object.name = "ceiling"


bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=(point_x_max ,(point_y_max + point_y_min)/2, max(height)/20 + 5), 
                                scale=(1,point_y_max-point_y_min, max(height)/10+ 10 ))
bpy.context.active_object.name = "front_wall"

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=(point_x_min ,(point_y_max + point_y_min)/2, max(height)/20 + 5), 
                                scale=(1,point_y_max-point_y_min, max(height)/10+ 10 ))
bpy.context.active_object.name = "back_wall"


bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=((point_x_max + point_x_min)/2 ,point_y_max, max(height)/20 + 5), 
                                scale=(point_x_max-point_x_min, 1, max(height)/10+ 10 ))
bpy.context.active_object.name = "left_wall"

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', 
                                location=((point_x_max + point_x_min)/2 ,point_y_min, max(height)/20 + 5 ), 
                                scale=(point_x_max-point_x_min, 1, max(height)/10+ 10 ))
bpy.context.active_object.name = "right_wall"



#make seats
for (xi,yi,zi) in seats:    

    (x,y,z) = (xi/10, yi/10, zi/10)
    bpy.ops.mesh.primitive_cube_add(size=1.2, enter_editmode=False, align='WORLD', 
                                        location=(x ,y, z ), 
                                        scale=(1, 1, 0.2))
    bpy.ops.mesh.primitive_cube_add(size=1.2, enter_editmode=False, align='WORLD', 
                                        location=(x-0.8 ,y, z + 1 ), 
                                        scale=(0.25, 1, 1.6))
    bpy.context.object.rotation_euler[1] = 2.966
    bpy.ops.mesh.primitive_cylinder_add(radius=0.5,  depth=1.2, enter_editmode=False, align='WORLD', 
                                        location=(x ,y, z -0.5 ), 
                                        scale=(0.2, 0.2, 0.5))
    bpy.ops.mesh.primitive_cube_add(size=1.2, enter_editmode=False, align='WORLD', 
                                        location=(x ,y, z -0.875), 
                                        scale=(0.2, 1, 0.125))
    bpy.ops.mesh.primitive_cube_add(size=1.2, enter_editmode=False, align='WORLD', 
                                        location=(x ,y +0.75, z -0.875), 
                                        scale=(1, 0.2, 0.125))
    bpy.ops.mesh.primitive_cube_add(size=1.2, enter_editmode=False, align='WORLD', 
                                        location=(x ,y -0.75, z -0.875), 
                                        scale=(1, 0.2, 0.125))
        