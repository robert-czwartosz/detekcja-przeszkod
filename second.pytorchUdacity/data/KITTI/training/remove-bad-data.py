import os
from progress_bar import ProgressBar

vel = './velodyne/'
img = './image_2/'
cal = './calib/'
lab = './label_2/'

listOfGTFiles = [("%06d" % int(f.split("_")[0])) for f in os.listdir("../gt_database/") if os.stat("../gt_database/"+f).st_size == 0 ]

#listOfAllGTFiles = [("%06d" % int(f.split("_")[0])) for f in os.listdir("../gt_database/") ]
#listOfFiles = [ f[:-4] for f in os.listdir("./calib/") if f[:-4] not in listOfAllGTFiles ]

print("Removing bad data. This may take several minutes.")
# removing bad data
prog_bar1 = ProgressBar()
prog_bar1.start(len(listOfGTFiles)) # +len(listOfFiles))
for f in listOfGTFiles:
     os.system("rm -f "+vel+f+".bin ")
     os.system("rm -f "+img+f+".jpg ")
     os.system("rm -f "+cal+f+".txt ")
     os.system("rm -f "+lab+f+".txt ")
     prog_bar1.print_bar()

#for f in listOfFiles:
#     os.system("rm -f "+vel+f+".bin ")
 #    os.system("rm -f "+img+f+".jpg ")
  #   os.system("rm -f "+cal+f+".txt ")
   #  os.system("rm -f "+lab+f+".txt ")
    # prog_bar1.print_bar()


# indexing
print("Indexing files")
listOfBinFiles = [f[:-4] for f in os.listdir(vel) ]
listOfBinFiles.sort()
i = 0
prog_bar = ProgressBar()
prog_bar.start(len(listOfBinFiles))
#Dict = {listOfBinFiles[0]:'0'}
with open("./dict_removed.txt","a") as dictf:
    for f in listOfBinFiles:
        #Dict[f] = ("%06d" % i)
        dictf.write(("%06d" % i)+" "+f+"\n")
        os.system("mv -f "+lab+f+".txt "+lab+("%06d" % i)+".txt ")
        os.system("mv -f "+vel+f+".bin "+vel+("%06d" % i)+".bin ")
        os.system("mv -f "+cal+f+".txt "+cal+("%06d" % i)+".txt ")
        os.system("mv -f "+img+f+".jpg "+img+("%06d" % i)+".jpg ")
        i = i + 1
        prog_bar.print_bar()

os.system("python2 split_train.py 0")
