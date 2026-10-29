# Jumper description

ROS 2 description package for the Jumper hexapod: 41 links, 22 revolute joints,
and 18 fixed joints. The root frame is `base_link`.

## Source

Model and meshes: https://github.com/KingKongRobotics/jumper

Source commit: `b2e58669848a3ba4f209597cd6bebdfe9d0533a4`.
Source model: `assets/jumper/urdf/jumper/urdf/jumper.urdf`.
Model revision: `V1.6-1`. Mesh resource URIs have been adapted for ROS.
Movable joints use `<PREFIX>_joint<index>` (for example, `LF_joint0`),
corresponding to upstream `<PREFIX>_J<index>_joint` names.
Limits corrected to match the training model: LM joint0 lower -0.75 rad,
RF joint4 lower -0.1 rad, and RF joint2 upper 2.2 rad.
The LF palm mass attribute has its trailing whitespace removed.
Joint ordering, transforms, inertias, colors, and mesh bytes are preserved.
Visual and collision geometry use the same original STL meshes.
The upstream NOTICE is retained for attribution; its repository-wide inventory
also mentions components that are not included in this model-only package.

## Build and view

```bash
cd /home/fiveages/dev_ws/fa-deploy-ws
source /opt/ros/jazzy/setup.bash
colcon build --packages-select kingkong_jumper_description --symlink-install
source install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=kingkong_jumper
```

The visualization command requires the workspace's `robot_common_launch` package.
The common model entry point is `xacro/robot.xacro`.

## Scope

This package provides the robot model only. It does not configure ros2_control,
a hardware driver, OCS2 locomotion, or reinforcement-learning inference.
A successful model load does not validate contact dynamics or real hardware.
