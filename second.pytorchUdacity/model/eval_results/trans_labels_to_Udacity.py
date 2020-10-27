import os, sys

os.system("cp ../../data/KITTI/testing/KITTI_Udacity_inds_dict.txt ./")
Dir = sys.argv[1]
listOfFiles = [f for f in os.listdir(Dir) ]
Len = len(listOfFiles)
print "Converting KITTI labels to Udacity tracklets. This may take several minutes..."
with open("KITTI_Udacity_inds_dict.txt") as myfile:
    for i in range(Len):
	if i%5000==0 and i>0:
	    print str(i)+" files processed"
        Line = myfile.readline()
        List = Line.split()
	#command = "mv "+train_vel+List[0]+".bin "+train_vel+List[1]+".bin"
	#print command
        os.system("mkdir -p "+List[2])
        os.system("mkdir -p "+"./"+List[2]+"/"+List[3])
        os.system("cp "+Dir+"/"+List[1]+".txt "+List[2]+"/"+List[3]+"/"+List[0]+".txt")
#os.system("python2 labels_to_xml.py ./1/")
#os.system("python2 labels_to_xml.py ./2/")
os.system("python2 labels_to_xml.py ./3/")
