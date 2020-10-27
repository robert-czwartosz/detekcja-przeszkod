import os
listOfBinFiles = [f for f in os.listdir('./label_2/') ]
listOfBinFiles.sort()
i = 0
os.system("rm KITTI_Udacity_inds_dict.txt")
for name in listOfBinFiles:
            Info = name.split('-')
	    Text = Info[0][:-4] + " " + '%06d' % (i) + " " + Info[1] + " " + Info[3] + "\n"
	    with open("KITTI_Udacity_inds_dict.txt", "a") as myfile:
    	        myfile.write(Text)
	    i = i + 1

