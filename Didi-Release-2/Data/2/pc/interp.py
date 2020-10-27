
import sys
import time
import numpy
import string
import os
xxx = 1
DirOfTrack = sys.argv[1]
#print(DirOfTrack)
for binDir in [f for f in os.listdir(DirOfTrack)]:
    #print(DirOfTrack + binDir + "/camera/")
    listOfImag = [f for f in os.listdir(DirOfTrack + binDir + "/camera/")]
    listOfImag.sort()
    listOfImagLong = [int(f[:-4]) for f in listOfImag]
    listOfImagLong.sort()
    listOfBin = [f for f in os.listdir(binDir)]
    listOfBin.sort()
    listOfBinLong = [int(f[:-4]) for f in listOfBin]
    listOfBinLong.sort()
    if len(listOfImag)==0:
        continue
    i = 0
    os.system("mkdir pc-" + binDir + "-proc")
    print("Processing " + binDir)
    for img in listOfImag:
        dtMin = 99999999999
        j = -1
        for jj in range(len(listOfBin)):
            dt = abs(listOfBinLong[jj] - listOfImagLong[i])
            if dt < dtMin:
                dtMin = dt
                j = jj
        if xxx==1:
            print(j)
	    print(listOfBinLong[j])
            print("cp ./"+binDir+"/"+listOfBin[j]+" pc-"+binDir+"-proc/"+img[:-4]+".bin")
        os.system("cp ./"+binDir+"/"+listOfBin[j]+" pc-"+binDir+"-proc/"+img[:-4]+".bin")
        i = i+1
    xxx = 0
