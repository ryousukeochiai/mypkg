# SPDX-FileCopyrightText: 2023 Ryousuke Ochiai 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    DOW_talker = launch_ros.actions.Node(
        package='mypkg',
        executable='DOW_talker',
        )
    DOW_listener = launch_ros.actions.Node(
        package='mypkg',
        executable='DOW_listener',
        output='screen'
        )

    return launch.LaunchDescription([DOW_talker, DOW_listener])
