#!/bin/bash -xv
# SPDX-FileCopyrightText: 2023 Ryousuke Ochiai 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Listen: 5'

timeout 5 ros2 launch mypkg DOW_talk_listen.launch.py > /tmp/DOW_mypkg.log

cat /tmp/DOW_mypkg.log #| grep ' (Mon)\| (Tue)\| (Wed)\| (Thu)\| (Fri)\| (Sat)\| (Sun)'

judge=false

for day in Mon Tue Wed Thu Fri Sat Sun; do
    if cat /tmp/DOW_mypkg.log | grep -q " ($day)"; then
        judge=true
    else
        judge=false
        break
    fi
done

if $judge; then
    exit 0
else
    exit 1
fi
