#!/bin/bash

  rm -r ./second.pytorchUdacity/data/KITTI/training/velodyne/
  mkdir ./second.pytorchUdacity/data/KITTI/training/velodyne/
  rm -r ./second.pytorchUdacity/data/KITTI/training/calib/
  mkdir ./second.pytorchUdacity/data/KITTI/training/calib/
  rm -r ./second.pytorchUdacity/data/KITTI/training/label_2/
  mkdir ./second.pytorchUdacity/data/KITTI/training/label_2/
  rm -r ./second.pytorchUdacity/data/KITTI/training/image_2/
  mkdir ./second.pytorchUdacity/data/KITTI/training/image_2/

  rm -r ./second.pytorchUdacity/data/KITTI/testing/velodyne/
  mkdir ./second.pytorchUdacity/data/KITTI/testing/velodyne/
  rm -r ./second.pytorchUdacity/data/KITTI/testing/calib/
  mkdir ./second.pytorchUdacity/data/KITTI/testing/calib/
  rm -r ./second.pytorchUdacity/data/KITTI/testing/label_2/
  mkdir ./second.pytorchUdacity/data/KITTI/testing/label_2/
  rm -r ./second.pytorchUdacity/data/KITTI/testing/image_2/
  mkdir ./second.pytorchUdacity/data/KITTI/testing/image_2/


cd ./Didi-Release-2/Data/

 for dir in *
 do

  cd ./$dir/
  ./packets_to_pc2.sh
  sleep 10

  SET="training"
  if [ "$dir" = "3" ]; then
    SET="testing"
  fi

  echo "Directory $dir: Creating .bin files"
  cd pc
  python2 pcl_from_bag.py
  python2 interp.py ../TRACKLETS/

  echo "Directory $dir: Creating labels"
  cd ..
  python2 xml_to_label.py ./TRACKLETS/

  echo "Directory $dir: Copying .bin files to ./second.pytorchUdacity/data/KITTI/$SET/velodyne/"

  for dirr in ./pc/pc-*-proc
  do
    cp $dirr/*.bin ../../../second.pytorchUdacity/data/KITTI/$SET/velodyne/
  done

  echo "Directory $dir: Copying labels to ./second.pytorchUdacity/data/KITTI/$SET/label_2/"

  for dirr in label-*
  do
    cd ./$dirr/
    for file in *.txt
    do
      cp $file ../../../../second.pytorchUdacity/data/KITTI/$SET/label_2/"$file"-"$dir"-"$dirr"-.txt
    done
    cd ..
  done

  cd ../
 done



for dir in *
do
  cd ./$dir/
  SET="training"
  if [ "$dir" = "3" ]; then
    SET="testing"
  fi
  rm -f ./TRACKLETS/*.xml

  echo "Directory $dir: Copying images to second.pytorchUdacity/data/KITTI/$SET/image_2/"
  for dirr in ./TRACKLETS/*  
  do
    echo "cp "$dirr"/camera/*.jpg ../../../second.pytorchUdacity/data/KITTI/$SET/image_2/"
    cp "$dirr"/camera/*.jpg ../../../second.pytorchUdacity/data/KITTI/"$SET"/image_2/
  done

  cd ./TRACKLETS/
  echo "Directory $dir: Copying tracklet files"
  for dirrr in *; do cp ./$dirrr/tracklet_labels.xml ./$dirrr.xml; done
  cd ..

  cd ..
done



echo "Moving to second.pytorchUdacity/data/KITTI/testing/"
cd ../../second.pytorchUdacity/data/KITTI/testing/


python2 KITTI_Udacity_inds.py
echo "Creating calibration files"
python2 create_calib.py 
echo "Renaming files to KITTI indices"
python2 trans_inds_to_KITTI.py
python2 test_inds.py



echo "Moving to second.pytorchUdacity/data/KITTI/training/"
cd ../training/


python2 KITTI_Udacity_inds.py
echo "Creating calibration files"
python2 create_calib.py 
echo "Renaming files to KITTI indices"
python2 trans_inds_to_KITTI.py
python2 split_train.py 0


