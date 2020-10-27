import os

Proj_mat = "1362.184692 0.000000 620.575531 0.000000 0.000000 1372.305786 561.873133 0.000000 0.000000 0.000000 1.000000 0.000000"
#Proj_mat = "176.5 0.000000 30 646.5 0.000000 83 84.5 0.000000 0.000000 0.000000 1.000000 0.000000"
rectification = "1 0 0 0 1 0 0 0 1"
Tr_velo_to_cam = "1 0 0 0.4 0 1 0 0 0 0 1 1.27"
Tr_velo_to_cam2 = "1 0 0 0.4 0 1 0 0 0 0 1 0.77"
Tr_imu_to_velo = "1 0 0 -0.8 0 1 0 0 0 0 1 0.8"

Text = "P0: " + Proj_mat + "\n"
Text = Text + "P1: " + Proj_mat + "\n"
Text = Text + "P2: " + Proj_mat + "\n"
Text = Text + "P3: " + Proj_mat + "\n"
Text = Text + "R0_rect: " + rectification + "\n"
Text2 = Text + "Tr_velo_to_cam: " + Tr_velo_to_cam2 + "\n" 
Text = Text + "Tr_velo_to_cam: " + Tr_velo_to_cam + "\n"
Text = Text + "Tr_imu_to_velo: " + Tr_imu_to_velo + "\n"
Text2 = Text2 + "Tr_imu_to_velo: " + Tr_imu_to_velo + "\n" 

with open("KITTI_Udacity_inds_dict.txt") as myfile:
    Lines = myfile.readlines()
    for Line in Lines:
        Info = Line.split()
        with open("./calib/"+Info[1]+".txt", "w") as myfile:
            if Info[2] == '1':
                myfile.write(Text)
            else:
                myfile.write(Text2)

