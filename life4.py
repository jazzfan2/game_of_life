#!/usr/bin/env python2
# Name  : life4.py
# Author: Rob Toscani
# Date  : 14-04-2017
# Description: John Conway's Game of Life, see https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
####################################################################################################
#
# Versie met "bewegende camera" bediend vanuit een aparte terminal waarin het script lifecamera.sh 
# wordt gerund. Punt van onderzoek zou nog kunnen zijn: de portabiliteit (i.v.m. de vereiste 
# terminaltypen), eventueel later.
# De camera wordt bediend met pijltjes-toetsen (pan/tilt), <PAGEUP>/<PAGEDOWN> (zoom in/out) en <HOME>
# (reset, center). Het programma kan worden gestopt met <END> of met Ctrl-C
# Error-handling uitgebreid, tegen te grote opgegeven waarden voor het camera grid.
# Konsole onder Gnome met grid 82 x 48 geeft het beste resultaat.
#
######################################################################################
#
# Copyright (C) 2024 Rob Toscani <rob_toscani@yahoo.com>
#
# life4.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# life4.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
######################################################################################
#

import sys
import subprocess
import os
import signal
import time
universe_size = 120									# Total "universal" grid size
max_width = int(sys.argv[1])						# e.g. 82 for grid of horizontal camera grid 82
max_height = int(sys.argv[2])						# e.g. 48 for grid of vertical camera grid 48
birth_rule = [int(j) for j in str(sys.argv[3])]		# e.g. 3 for B3 
survival_rule = [int(j) for j in str(sys.argv[4])]	# e.g. 23 for S23
grid = []
os.system('clear')
os.system('gnome-terminal -t "CAMERA CONTROL" --geometry 0x5+0+0 -e /home/rob/scripts/lifecamera.sh&')
os.system('echo "" > /dev/shm/control_file')
#
def handleSIGINT(a,b):
    os.system('kill -9 `pgrep lifecamera` 2>/dev/null')
    print '\033[0m'
    os.system('clear')
    sys.exit()
signal.signal(signal.SIGINT, handleSIGINT)
#
"""Empty grid:"""
for y in xrange(universe_size+1):
    grid.append([])
    for x in xrange(universe_size+1):
        grid[y].append(0)
#
"""Start condition by seed part:"""
f = open('life_startcondition.txt')
seed = []
for line in f.readlines():
    if not line:
        break
    seed.append([int(i) for i in str(line[:-1])])		# Minus the \n at the end (-1)
f.close()
#
"""Offsets needed for centering seed part on grid:"""
seedwidth = len(seed[0])
seedheight = len(seed)
offset_x = (universe_size - seedwidth - 1) / 2
offset_y = (universe_size - seedheight - 1) / 2
#
"""Error handling:"""
cols = int(subprocess.check_output(["tput", "cols"])[:-1]) / 2 - 1
lines = int(subprocess.check_output(["tput", "lines"])[:-1]) - 2
if max_width >= cols or max_height >= lines:
    max_width = cols
    max_height = lines
if offset_x < 0 or offset_y < 0:
    print "Seed part too large"
    sys.exit()
#
"""Placement of seed part on grid:"""
for y in xrange(len(seed)):
    for x in xrange(len(seed[y])):
        grid[y + offset_y][x + offset_x] = seed[y][x]
#
"""Second grid with new cell states as a function of the number of live neighbours in first grid:"""
width,height = max_width,max_height
out_w = (universe_size - width) / 2
out_h = (universe_size - height) / 2
while True: 
    grid2 = [x[:] for x in grid]	# Deep copying essential with 2D lists, to avoid referencing !
    for y in xrange(1,universe_size):
        for x in xrange(1,universe_size):
            neighbours = sum(grid[y-1][x-1:x+2]) + grid[y][x-1] + grid[y][x+1] + sum(grid[y+1][x-1:x+2])
            if grid[y][x] == 1 and neighbours not in survival_rule:
                grid2[y][x] = 0
            elif grid[y][x] == 0 and neighbours in birth_rule:
                grid2[y][x] = 1
#
    """Camera control:"""
    f = open('/dev/shm/control_file')
    command = f.readline()[:-1]
    if command == 'left' and out_w > 0:
        out_w -= 1
    elif command == 'right' and out_w + width < universe_size:
        out_w += 1
    elif command == 'up' and out_h > 0:
        out_h -= 1
    elif command == 'down' and out_h + height < universe_size:
        out_h += 1
    elif command == 'in' and out_w + width < universe_size \
    and out_h + height < universe_size and width > 2 and height > 2:
        out_w += 1
        out_h += 1
        width -= 2
        height -= 2
    elif command == 'out' and out_w > 0 and out_h > 0 \
    and out_w + width < universe_size and out_h + height < universe_size \
    and width < max_width - 1 and height < max_height - 1:
        out_w -= 1
        out_h -= 1 
        width += 2
        height += 2
    elif command == 'reset':
        width,height = max_width,max_height
        out_w = (universe_size - width) / 2
        out_h = (universe_size - height) / 2
    elif  command == 'stop':
        print '\033[0m'
        os.system('clear')
        sys.exit()
    f.close()
    os.system('clear')
#
    """Colour representation of second grid:"""
    for y in xrange(out_h, out_h + height+1):
        for x in xrange(out_w, out_w + width+1):                    
            if grid2[y][x] == 1:
#               print '1',
                print '\033[7;36;46m' + '1' + '\033[0m',
#               print '\033[7;36;46m' + '1',
            elif grid2[y][x] == 0:
#               print '0',
                print '\033[3;34;44m' + '0',
            if x == out_w + width:                           
                print '\r'
    time.sleep(0.03)
    grid = [x[:] for x in grid2]
#

