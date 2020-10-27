import os, sys
import random

wsp = float(sys.argv[1])

listOfFilesTrain = [f for f in os.listdir('./velodyne/')]
random.shuffle(listOfFilesTrain)
ValList = listOfFilesTrain[:int(len(listOfFilesTrain)*wsp)]
TrainList = listOfFilesTrain[int(len(listOfFilesTrain)*wsp):]
ValList.sort()
TrainList.sort()
listOfFilesTrain.sort()

os.system("rm ../../ImageSets/trainval.txt")
os.system("rm ../../ImageSets/train.txt")
os.system("rm ../../ImageSets/val.txt")

os.system("touch ../../ImageSets/trainval.txt")
os.system("touch ../../ImageSets/train.txt")
os.system("touch ../../ImageSets/val.txt")

for filename in listOfFilesTrain:
    with open("../../ImageSets/trainval.txt", "a") as myfile:
    	myfile.write(filename[:-4]+"\n")
print "../../ImageSets/trainval.txt"
for filename in TrainList:
    with open("../../ImageSets/train.txt", "a") as myfile:
    	myfile.write(filename[:-4]+"\n")
print "../../ImageSets/train.txt"
for filename in ValList:
    with open("../../ImageSets/val.txt", "a") as myfile:
    	myfile.write(filename[:-4]+"\n")
print "../../ImageSets/val.txt"
