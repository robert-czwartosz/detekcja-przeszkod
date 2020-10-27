# activating environment
source ~/anaconda3/bin/activate
conda activate secondEnv


python train.py evaluate --config_path=./second/configs/car.tiny.config --model_dir=`pwd`/model/
