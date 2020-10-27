from xml.dom import minidom
import os, sys

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)
Dir_to_tracks = sys.argv[1]
listOfDirs = [f for f in os.listdir(Dir_to_tracks) ]
for Dir in listOfDirs:
    LabDir = "label-"+Dir
    os.system("mkdir"+" "+LabDir)
    print LabDir
    xmldoc = minidom.parse(Dir_to_tracks+Dir+'/tracklet_labels.xml')
    # number of obstacles
    itemlist = xmldoc.getElementsByTagName('count')
    itemlistObj = xmldoc.getElementsByTagName('objectType')
    itemlistH = xmldoc.getElementsByTagName('h')
    itemlistW = xmldoc.getElementsByTagName('w')
    itemlistL = xmldoc.getElementsByTagName('l')
    
    itemlistX = xmldoc.getElementsByTagName('tx')
    itemlistY = xmldoc.getElementsByTagName('ty')
    itemlistZ = xmldoc.getElementsByTagName('tz')
    itemlistOCCL = xmldoc.getElementsByTagName('occlusion')
    itemlistTRUN = xmldoc.getElementsByTagName('truncation')
    
    listOfBinFiles = [f for f in os.listdir('./pc/'+"pc-"+Dir+"-proc") ]
    listOfBinFiles.sort()
    
    Count = len(itemlistObj)
    for i in range(Count):
    	# object type
    	ObjType = getText(itemlistObj[i].childNodes)
    	# height
    	h = getText(itemlistH[i].childNodes)
    	# width
    	w = getText(itemlistW[i].childNodes)
    	# long
    	l = getText(itemlistL[i].childNodes)
	#print len(itemlistX)
	#print len(listOfBinFiles)
	wsp = float(len(listOfBinFiles))/float(len(itemlistX))
    	Frames = len(itemlistX)
    	for j in range(Frames):
	    j=int(float(j)*wsp)
	    # x
	    x = getText(itemlistX[j].childNodes)
	    # y 
	    y = getText(itemlistY[j].childNodes)
	    # z
	    z = getText(itemlistZ[j].childNodes)
	    # occlusion
	    occlusion = getText(itemlistOCCL[int(float(j)*wsp)].childNodes)
	    # truncation
	    truncation = getText(itemlistTRUN[j].childNodes)
	    Text = ObjType+" "+truncation+" "+ occlusion+" 1 "+"2 "+"1 "+"2 "+"1 "+w+" "+l+" "+h+" "+x+" "+y+" "+z+" 0.01" + "\n"
	    with open(LabDir+"/"+listOfBinFiles[j][:-4]+".txt", "w") as myfile:
    	        myfile.write(Text)

