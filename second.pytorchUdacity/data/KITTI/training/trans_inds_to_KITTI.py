import os
vel = './velodyne/'
img = './image_2/'
cal = './calib/'
lab = './label_2/'
#vre = './velodyne_reduced/'

listOfBinFiles = [f for f in os.listdir(vel) ]
LenTrain = len(listOfBinFiles)
print "Translating to KITTI indices. This may take several minutes..."
with open("KITTI_Udacity_inds_dict.txt") as myfile:
    for i in range(LenTrain):
        Line = myfile.readline()
        List = Line.split()
	#command = "mv "+train_vel+List[0]+".bin "+train_vel+List[1]+".bin"
	#print command
        os.system("mv "+vel+List[0]+".bin "+vel+List[1]+".bin")
        #os.system("mv "+vre+List[0]+".bin "+vre+List[1]+".bin")
        os.system("mv "+img+List[0]+".jpg "+img+List[1]+".jpg")
        #os.system("mv "+cal+List[0]+".txt "+cal+List[1]+".txt")
        os.system("mv "+lab+List[0]+"* "+lab+List[1]+".txt")

