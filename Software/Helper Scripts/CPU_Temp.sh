#!/usr/bin/bash

gnome-terminal --geometry=11x4+0+0 --title="System Temps" -- bash -c \
  'watch -t -c -b -d -n 1 '\''cpu=$(cat /sys/class/thermal/thermal_zone0/temp); echo "             -----------"; printf "             CPU: %.1f c\n" $(echo "$cpu/1000" | bc -l); echo "             GPU: $(vcgencmd measure_temp | cut -d = -f2)"; echo "             -----------" '\'''

