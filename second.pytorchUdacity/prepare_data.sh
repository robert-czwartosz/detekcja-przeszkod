# activating environment
source ~/anaconda3/bin/activate
conda activate secondEnv



python create_data.py create_kitti_info_file --data_path=./data/KITTI/
python create_data.py create_groundtruth_database --data_path=./data/KITTI/

