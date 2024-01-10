#!/bin/bash -xv
# SPDX-FileCopyrightText: 2023 Ryousuke Ochiai 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
export MYPKG_TEST_FIXED_DATE="2024-01-01"
timeout 10 ros2 launch mypkg DOW_talk_listen.launch.py > /tmp/DOW_mypkg.log

cat /tmp/mypkg.log |
	grep 'Listen: 10'
cat /tmp/DOW_mypkg.log |
	grep '2024/01/11 (Thu)'
