#!/bin/bash

cd ./Didi-Release-2/Data/
cd ../tracklets/
chmod u+x ./*.sh
sudo ./build.sh
cd ../Data/

for dir in *
do

  cd ../tracklets/
  sudo ./run-bag_to_kitti.sh -i $(cd .. ; pwd ; cd ./tracklets/)/Data/"$dir"/ -o $(cd .. ; pwd ; cd ./tracklets/)/Data/"$dir"/TRACKLETS/
  

done

sudo chown -R $USER ../Data/
