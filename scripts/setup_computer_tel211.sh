#!/bin/bash


clear; echo "Setting up computer for TEL211"; sleep 2

# update package list
sudo apt update


# upgrade packages
sudo apt -y upgrade


# Vim
clear; echo "Installing Vim"; sleep 1
sudo apt install -y vim


# Chromium
clear; echo "Installing Chromium"; sleep 1
sudo apt install -y chromium-browser


# tmux
clear; echo "Installing tmux"; sleep 1
sudo apt install -y tmux


# Shutter
clear; echo "Installing shutter"; sleep 1
sudo apt install -y shutter


# ROS Melodic
clear; echo "Installing ROS Melodic and friends"; sleep 1
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install -y curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install -y ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source /opt/ros/melodic/setup.bash # in case we do some ROS stuff later
sudo apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init
rosdep update
sudo apt install -y python-catkin-tools


# Install Thorvald
clear; echo "Installing Thorvald packages"; sleep 1
curl -s http://lcas.lincoln.ac.uk/repos/public.key | sudo apt-key add -
sudo apt-add-repository http://lcas.lincoln.ac.uk/ubuntu/main
sudo apt-get update
sudo apt-get install -y ros-melodic-thorvald*


# Install other ROS packages
clear; echo "Installing ros controllers"; sleep 1
sudo apt install -y ros-melodic-effort-controllers ros-melodic-velocity-controllers
sudo apt install -y ros-melodic-ros-numpy

#install Git
sudo apt install -y git

# Create and compile catkin ws
clear; echo "Creating catkin workspace"; sleep 1
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src; git clone https://github.com/NMBURobotics/TEL211.git 
cd ~/catkin_ws; rosdep install --from-paths src --ignore-src -r -y
cd ~/catkin_ws; catkin build
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc


## OTHER ROBOTS

# Install Husky packages
clear; echo "Installing Husky packages"; sleep 1
sudo apt install -y ros-melodic-husky*


# Install Open Manipulator
clear; echo "Installing Open maniuplator"; sleep 1
sudo apt install -y ros-melodic-open-manipulator


# vscode
clear; echo "Installing vscode"; sleep 1
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt install -y apt-transport-https
sudo apt update
sudo apt install -y code # or code-insiders



#####sudo snap install --classic code
# setup guide: https://www.youtube.com/watch?v=RXyFSnjMd7M


## OTHER STUFF

# Uncomment if setting up private computer

## Openssh
#clear; echo "Installing openssh-server"; sleep 1
#sudo apt-get -y install openssh-server


## Dialout
#clear; echo "Adding thorvald to dialout group"; sleep 1
#sudo usermod -a -G dialout $USER



# That's it
clear; echo "Finished!"
MUSIC=/usr/lib/libreoffice/share/gallery/sounds/cow.wav
if test -f "$MUSIC"; then
    aplay $MUSIC
fi
sleep 4

