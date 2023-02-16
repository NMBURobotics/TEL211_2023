#!/bin/bash

for i in {1..10}; do
    echo "$i"
done




echo "---"




for i in {1..10..2}; do
    echo "$i"
done




echo "---"




for i in apple banana pear tomhanks; do
    echo "$i"
done




echo "---"



for i in "$@"; do
    echo "$i"
done

