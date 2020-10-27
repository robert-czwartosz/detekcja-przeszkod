# activating environment
source ~/anaconda3/bin/activate
conda activate secondEnv

# converting to tracklets and Udacity evaluation
cd ./model/eval_results/
python2 trans_labels_to_Udacity.py ./step_*/

# Udacity evaluation
cd ../../../
python ./Didi-Release-2/tracklets/python/evaluate_tracklets.py `pwd`/second.pytorchUdacity/model/eval_results/3/tracklets/ `pwd`/Didi-Release-2/Data/3/TRACKLETS/
