Maze Solving with MyCobot Pro 600 – Instructions
1. Image Capture & Processing

1.1 Connect the camera to your laptop
Use the appropriate USB or Ethernet cable to connect the camera. Ensure it is powered on and recognized by your system.

1.2 Capture the maze image
Run the following script to capture an image containing the maze:

python3 Maze_capture.py

1.3 Extract the maze from the image
Run the extraction script:

python3 Maze_extract.py
Adjust the crop variables in the script if needed to accurately isolate the maze.
2. Robot Setup (MyCobot Pro 600)

2.1 Connect peripherals
Connect the MyCobot Pro 600 to a monitor, keyboard, and mouse.

2.2 Power on and log in
Turn on the robot and log into the system (Roboflow OS) using:

Password: elephant

2.3 Connect via Ethernet
Connect the robot to your computer using an Ethernet cable.

2.4 Enable TCP Server
On the robot interface:

Go to Tools → Configuration → Network/Serial Port
Under TCP Server, click Start

2.5 Move robot to home position
Use the Return to Home function to initialize the robot’s position.

3. Execute Maze Solving

3.1 Run the control script

python3 maze_solver_2.py
This script connects your computer to the robot via its IP address using socket programming.
It sends movement commands to solve the maze.

3.2 Adjust kinematics if needed

Modify the set_angles() function in the script if adjustments are required for accurate robot motion.
