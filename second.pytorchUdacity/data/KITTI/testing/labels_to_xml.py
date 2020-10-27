import os, sys

Dirs = sys.argv[1].split()
# Dirs = [f for f in os.listdir(Dir)  if "." not in f and f!="tracklets"]
os.system("mkdir tracklets")
print Dirs
for dirr in Dirs:
	print dirr
        Labels = [f for f in os.listdir("./"+dirr+"/") ]
	Labels.sort()
	with open("."+"/"+dirr+"/"+Labels[0]) as myfile:
	    line = myfile.readline()
	Infos = None
        if len(line.split())!=0:
            Infos = line.split()
        else:
            if Infos == None:
                Infos = ["Car","-1","-1","0","1","2","1","2","1","1","1","0","0","0","0"]
	Obj = Infos[0]
	truncation = Infos[1]
	occlusion = Infos[2]
	w = Infos[8]
	l = Infos[9]
	h = Infos[10]
	x = Infos[11]
        y = Infos[12]
        z = Infos[13]
	
	Text = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?>\n"
	Text = Text + "<!DOCTYPE boost_serialization>\n"
	Text = Text + "<boost_serialization signature=\"serialization::archive\" version=\"9\">\n"
	Text = Text + "<tracklets class_id=\"0\" tracking_level=\"0\" version=\"0\">\n"
	Text = Text + "\t<count>1</count>\n"
	Text = Text + "\t<item_version>1</item_version>\n"
	Text = Text + "\t<item class_id=\"1\" tracking_level=\"0\" version=\"1\">\n"
	Text = Text + "\t\t<objectType>"+Obj+"</objectType>\n"
	Text = Text + "\t\t<h>"+h+"</h>\n"
	Text = Text + "\t\t<w>"+w+"</w>\n"
	Text = Text + "\t\t<l>"+l+"</l>\n"
	Text = Text + "\t\t<first_frame>0</first_frame>\n"
	Text = Text + "\t\t<poses class_id=\"2\" tracking_level=\"0\" version=\"0\">\n"
	Text = Text + "\t\t\t<count>"+str(len(Labels))+"</count>\n"
	Text = Text + "\t\t\t<item_version>2</item_version>\n"
	
	Text = Text + "\t\t\t<item class_id=\"3\" tracking_level=\"0\" version=\"2\">\n"
	Text = Text + "\t\t\t\t<tx>"+x+"</tx>\n"
	Text = Text + "\t\t\t\t<ty>"+y+"</ty>\n"
	Text = Text + "\t\t\t\t<tz>"+z+"</tz>\n"
	Text = Text + "\t\t\t\t<rx>0.000000</rx>\n"
	Text = Text + "\t\t\t\t<ry>0.000000</ry>\n"
	Text = Text + "\t\t\t\t<rz>0.000000</rz>\n"
	Text = Text + "\t\t\t\t<state>1</state>\n"
	Text = Text + "\t\t\t\t<occlusion>"+occlusion+"</occlusion>\n"
	Text = Text + "\t\t\t\t<occlusion_kf>-1</occlusion_kf>\n"
	Text = Text + "\t\t\t\t<truncation>"+truncation+"</truncation>\n"
	Text = Text + "\t\t\t\t<amt_occlusion>0.0</amt_occlusion>\n"
	Text = Text + "\t\t\t\t<amt_occlusion_kf>-1</amt_occlusion_kf>\n"
	Text = Text + "\t\t\t\t<amt_border_l>0.0</amt_border_l>\n"
	Text = Text + "\t\t\t\t<amt_border_r>0.0</amt_border_r>\n"
	Text = Text + "\t\t\t\t<amt_border_kf>-1</amt_border_kf>\n"
	Text = Text + "\t\t\t</item>\n"
	
	for lab in Labels[1:]:
	    with open("."+"/"+dirr+"/"+lab) as myfile:
	        line = myfile.readline()
            if len(line.split())!=0:
                Infos = line.split()
            else:
                if Infos == None:
                    Infos = ["Car","-1","-1","0","1","2","1","2","1","1","1","0","0","0","0"]
            x = Infos[11]
	    y = Infos[12]
	    z = Infos[13]
	    Text = Text + "\t\t\t<item>\n"
    	    Text = Text + "\t\t\t\t<tx>"+x+"</tx>\n"
	    Text = Text + "\t\t\t\t<ty>"+y+"</ty>\n"
	    Text = Text + "\t\t\t\t<tz>"+z+"</tz>\n"
	    Text = Text + "\t\t\t\t<rx>0.000000</rx>\n"
	    Text = Text + "\t\t\t\t<ry>0.000000</ry>\n"
	    Text = Text + "\t\t\t\t<rz>0.000000</rz>\n"
	    Text = Text + "\t\t\t\t<state>1</state>\n"
	    Text = Text + "\t\t\t\t<occlusion>"+occlusion+"</occlusion>\n"
	    Text = Text + "\t\t\t\t<occlusion_kf>-1</occlusion_kf>\n"
	    Text = Text + "\t\t\t\t<truncation>"+truncation+"</truncation>\n"
	    Text = Text + "\t\t\t\t<amt_occlusion>0.0</amt_occlusion>\n"
	    Text = Text + "\t\t\t\t<amt_occlusion_kf>-1</amt_occlusion_kf>\n"
	    Text = Text + "\t\t\t\t<amt_border_l>0.0</amt_border_l>\n"
	    Text = Text + "\t\t\t\t<amt_border_r>0.0</amt_border_r>\n"
	    Text = Text + "\t\t\t\t<amt_border_kf>-1</amt_border_kf>\n"
	    Text = Text + "\t\t\t</item>\n"
	
	Text = Text + "\t\t</poses>\n"
	Text = Text + "\t\t<finished>1</finished>\n"
   	Text = Text + "\t</item>\n"
	Text = Text + "</tracklets>\n"
	Text = Text + "</boost_serialization>\n"

        with open("./"+"tracklets/"+dirr+".xml", "w") as myfile:
            myfile.write(Text)
