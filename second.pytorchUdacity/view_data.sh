# activating environment
source ~/anaconda3/bin/activate
conda activate secondEnv

# python plot_img.py ./data/KITTI/testing/image_2/000000.jpg &
python plot_img.py &
python viewer.py 
