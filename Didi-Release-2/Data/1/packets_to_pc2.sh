#!/bin/bash
roscore &
sleep 10
rosrun velodyne_pointcloud cloud_node _calibration:=/opt/ros/kinetic/share/velodyne_pointcloud/params/32db.yaml &
sleep 3
mkdir pc
for file in *.bag
do
echo "${file}"
rosrun rosbag record -O "./pc/${file}" /velodyne_points &
rosbag play -q "${file}"
sleep 10
PIDREC=$(ps -ae | grep record | cut -b 1-5)
kill -2 $PIDREC

done
PIDCLN=$(ps -ae | grep cloud_node | cut -b 1-5)
PIDROS=$(ps -ae | grep roscore | cut -b 1-5)
kill -2 $PIDCLN
kill -2 $PIDROS

