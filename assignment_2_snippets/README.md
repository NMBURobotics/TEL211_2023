# TEL211 Assignments 2
Refer to these example codes while working on the assignment 1.

## ROS Topic example
Make sure that you have executed `git pull` under TEL211 repository for up to date code. 

You can build the code with;

```bash
source /opt/ros/melodic/setup.bash
cd ~/catkin_ws
catkin_make -j2

```

You can run nodes with either given launch file;

```bash
source ~/catkin_ws/devel/setup.bash
roslaunch talker_listener_pkg start_nodes.launch
```

Or You can run nodes `rosrun`;

```bash
source ~/catkin_ws/devel/setup.bash
rosrun talker_listener_pkg talker.py
```
and in a seperate terminal 

```bash
source ~/catkin_ws/devel/setup.bash
rosrun talker_listener_pkg listener.py
```

## Rext to speech example

A simple python script to convert a string to speech. 
Install required packages with ;

```bash
 sudo apt install python3-pip
 sudo apt install mpg321
 sudo pip3 install gTTS
```

Then just `cd` into correct folder and do; 

```bash
python3 text_to_speech.py
```

