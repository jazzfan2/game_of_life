#!/bin/bash
# Name: lifecamera.sh
# Author: Rob Toscani
# Date: 22nd of April 2017
# Description: Control of the visible image ("camera") of life4.py
#
# This process is opened from the life4.py Python script itself.
# See also http://stackoverflow.com/questions/10679188/casing-arrow-keys-in-bash
#
#################################################################################
#
# Copyright (C) 2024 Rob Toscani <rob_toscani@yahoo.com>
#
# lifecamera.sh is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# lifecamera.sh is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
######################################################################################
#
control="/dev/shm/control_file"
trap "echo \"stop\" > $control; exit" SIGINT
cat << EOF
Arrows      = Pan & Tilt
PageUp/Down = Zoom in/out
Home        = Reset camera
End         = Stop Game
EOF
while read -r -n1 -s p; do
    case $p in
        A)	echo "up" > $control ;;
        B)	echo "down" > $control ;;
        C)	echo "right" > $control ;;
        D)	echo "left" > $control ;;
        5)	echo "in" > $control ;;
        6)	echo "out" > $control ;;
        H)	echo "reset" > $control ;;
        F)	echo "stop" > $control; exit ;;
        *)	continue ;;
    esac
    sleep 0.5
    echo "" > $control
done


