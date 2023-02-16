# TEL211 Assignments 3
Refer to these example codes while working on the assignment 3.


## Text to speech example

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

## ROS services example
In this example package(`service_server_client_pkg`), we create a service server where you provide a directory path, and the server returns you all folders in this directory. 

First make sure to build and source the `service_server_client_pkg` package with catkin workspace.
Then you can make sure the service definition is there with;

See the service definition with; 
```bash
rossrv show service_server_client_pkg/ListFolders
```

You should see; 
```bash
string path
---
string[] folders
```

In a terminal launch the serve node;

> rosrun service_server_client_pkg list_folders_server.py

In a seperate terminal call the service with; 

> rosservice call /list_folders /home/tel211/catkin_ws/

All folders must be outputted to terminal.

E.g.;

```bash
tel211@tel211-VirtualBox:~/catkin_ws$ rosservice call /list_folders /home/tel211/catkin_ws/
folders: [logs, src, .catkin_tools, build, devel]
```

