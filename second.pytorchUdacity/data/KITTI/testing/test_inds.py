import os
import random

listOfFilesTest = [f for f in os.listdir('./velodyne/')]
listOfFilesTest.sort()
os.system("rm ../../ImageSets/test.txt")
for filename in listOfFilesTest:
    with open("../../ImageSets/test.txt", "a") as myfile:
    	myfile.write(filename[:-4]+"\n")

