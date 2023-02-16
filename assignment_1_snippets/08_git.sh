#!/bin/bash

echo "This script will clone a github repository to the current folder. Is this OK? [Y/n]"
read -r reply


if [ "$reply" != "Y" ]; then
    exit 0
fi

# check if directory is already there
if test -d "bash_basic_examples"; then
    echo "bash_basic_examples already in directory. Terminating script.."
    exit 0
fi




#This next line is how you clone a github repository. Everything else in this file can be ignored.
git clone https://github.com/NMBURobotics/bash_basic_examples.git




echo "do you want to remove the repo we just cloned? [Y/n]"
read -r reply

if [ "$reply" != "Y" ]; then
    exit 0
fi

rm -rf bash_basic_examples


