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
python2 split_train.py 0.5
cd ../
rm -r gt_database
rm *.pkl
cd ../../

python create_data.py create_kitti_info_file --data_path=./data/KITTI/
python create_data.py create_groundtruth_database --data_path=./data/KITTI/

# run training
python train.py train --config_path=./second/configs/car.tiny.config --model_dir=`pwd`/model/

# run KITTI evaluation
python train.py evaluate --config_path=./second/configs/car.tiny.config.test --model_dir=`pwd`/model/ --pickle_result=False

# converting to tracklets and Udacity evaluation
cd ./model/eval_results/
python2 trans_labels_to_Udacity.py ./step_*/

# Udacity evaluation
cd ../../../
python ./Didi-Release-2/tracklets/python/evaluate_tracklets.py `pwd`/second.pytorchUdacity/model/eval_results/3/tracklets/ `pwd`/Didi-Release-2/Data/3/TRACKLETS/


#python ./Didi-Release-2/tracklets/python/evaluate_tracklets.py `pwd`/second.pytorchUdacity/model/eval_results/tracklets/step_276101.xml `pwd`/second.pytorchUdacity/data/KITTI/testing/tracklets/label_2.xml
