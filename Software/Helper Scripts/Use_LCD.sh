#!/usr/bin/bash

# This file uses the LCD screen driver and executes
# the commands to switch from HDMI -> LCD 3.5 display.

sudo apt-get install gnome-terminal

gnome-terminal --geometry=80x20+0+0 --title="Loading..." -- bash -c '
cd ~/LCD-show-kali/
sudo ./LCD35-show 
'
