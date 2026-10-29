cmake_minimum_required(VERSION 3.14)
project(kingkong_jumper_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY urdf xacro meshes DESTINATION share/${PROJECT_NAME})
install(FILES README.md LICENSE NOTICE DESTINATION share/${PROJECT_NAME})

ament_package()
