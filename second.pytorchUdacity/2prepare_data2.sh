# activating environment
source ~/anaconda3/bin/activate
conda activate secondEnv

# preparing data

cd ./data/KITTI/training/
python2 split_train.py 0
cd ../../../
python create_data.py create_kitti_info_file --data_path=./data/KITTI/
python create_data.py create_groundtruth_database --data_path=./data/KITTI/
cd ./data/KITTI/training/
python remove-bad-data.py
cd ../
rm -r gt_database
rm *.pkl
cd ../../



python create_data.py create_kitti_info_file --data_path=./data/KITTI/
python create_data.py create_groundtruth_database --data_path=./data/KITTI/

