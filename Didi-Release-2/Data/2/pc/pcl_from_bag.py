import sensor_msgs.point_cloud2 as pc2
import rosbag, sys, csv
import time
import numpy
import string
import os #for file management make directory
import shutil #for file management, copy file

listOfBagFiles = [".bag"]
listOfBagFiles = [f for f in os.listdir(".") if f[-4:] == ".bag"]
for BagFile in listOfBagFiles:
    bag = rosbag.Bag(BagFile)
    print "Processing "+BagFile
    dirname = BagFile[:-4]
    command = "mkdir "+dirname
    os.system(command)
    for subtopic, msg, t in bag.read_messages("/velodyne_points"):
    	array = numpy.empty([1000000,4])
    	i=0
    	#print "Reading points to array"
    	for p in pc2.read_points(msg, field_names = ("x", "y", "z", "intensity"), skip_nans=True):
      	    #print "%f %f %f %f" %(p[0],p[1],p[2],p[3])
    	    array[i][0] = p[0]
	    array[i][1] = p[1]
	    array[i][2] = p[2]
	    array[i][3] = p[3]
	    i = i+1
       	#print i
    	#print "Saving array to binary file"
    	array[:i][:].astype('float32').tofile(dirname+"/"+str(msg.header.stamp)+".bin")

