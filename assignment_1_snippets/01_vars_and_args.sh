#!/bin/bash


# this is a comment

# assign value to variable
animal=tiger
also_an_animal="snake"
num_var=3
array_var=(9 4 5 6)
multiline_var="This
is a multi line
text"

# assign the output of a command to a varaiable
user=$(whoami)

# use arguments passed to the script
arg_1=$1
arg_2=$2



echo "$animal is a cool animal"
echo "But my fav animal is the ${animal}${also_an_animal}"
echo "I want to have at least $num_var of those, or maybe ${array_var[0]}"

echo "$multiline_var"

echo "Hello ${user}! You passed '$arg_1' and '$arg_2' as arguments to this script."

echo "Number of args: $#"
echo "Args given: $*"
