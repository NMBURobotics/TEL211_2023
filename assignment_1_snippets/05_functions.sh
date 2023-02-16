#!/bin/bash


hello_printer() {
    echo "hello_world"	
}


arg_printer() {
    echo "$@"
}


hello_printer

arg_printer hi there old friend

arg_printer "$@"
