#!/bin/bash

echo "This script will install lolcat, use lolcat and remove lolcat. Is this OK [Y/n]"
read -r reply

if [ "$reply" != "Y" ]; then
    exit 0
fi


# Show info about program
sudo apt show lolcat

sleep 4 #give the user 4 seconds to read

# Install program
sudo apt -y install lolcat



echo "Hello! This is lolcat" | lolcat

sleep 2

echo "I will uninstall myself now" | lolcat

sleep 2

echo "Bye!" | lolcat

sleep 1


# Remove program
sudo apt -y remove lolcat


