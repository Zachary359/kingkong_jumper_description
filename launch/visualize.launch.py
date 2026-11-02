# SPDX-License-Identifier: Apache-2.0
"""Display Jumper at its reference joint pose with interactive joint sliders."""
import json
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from robot_common_launch import create_rmw_zenohd_node
import xacro


def generate_launch_description():
    package = Path(get_package_share_directory('kingkong_jumper_description'))
    description = xacro.process_file(str(package / 'xacro/robot.xacro')).toxml()
    home = json.loads((package / 'config/home.json').read_text())
    nodes = []
    router = create_rmw_zenohd_node()
    if router is not None:
        nodes.append(router)
    nodes.extend([
        Node(
            package='robot_state_publisher', executable='robot_state_publisher',
            name='robot_state_publisher', output='screen',
            parameters=[{'robot_description': description}],
        ),
        Node(
            package='joint_state_publisher_gui', executable='joint_state_publisher_gui',
            name='joint_state_publisher', output='screen',
            parameters=[{'robot_description': description, 'zeros': home}],
        ),
        Node(
            package='rviz2', executable='rviz2', output='screen',
            arguments=['-d', str(package / 'config/jumper.rviz')],
        ),
    ])
    return LaunchDescription(nodes)
