# Name: life4.py
life4.py - Program that visualizes John Conway's "Game of Life" in a command terminal.

# Description:
life4.py is a Python program that visualizes John Conway's "Game of Life" in a command terminal, with additional controls to move the viewpoint and to zoom in on or out of the animation.

See for background and details: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Summary: The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which (at any given time) is in one of two possible states, "live" (alternatively "on") or "dead" (alternatively "off"). Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. The way the pattern of cells develops is driven by two rules, the so-called "Birth rule" and "Survival rule". The result looks like a busy scene of moving "micro-organism"-like entities, crawling, expanding, dying out and re-emerging again.

# How to use life4.py:
Place the file 'life_startcondition.txt' in the same directory as the program life4.py. This is the initial pattern of ones and zeroes constituing the 'seed' of the system, determining how the game will start and develop. 

In order to start the "Game of Life" animation, supply the following command in a command terminal, followed by 4 integer arguments:

	./life4.py 82 48 3 23

The first two arguments are the horizontal and vertical grid sizes of the image "canvas" in the terminal. The values 82 and 48 are an example of an adequate grid size, but can of course be replaced by other values, dependent upon terminal-type and terminal/character size.

The third and fourth argument represent the settings of the "Birth rule" and "Survival rule" respectively.
Respective values 3 and 23 render a good probability that the life action on the canvas will persist and develop for quite some time before dying out (that is: dependant upon which start condition has been chosen).

Immediately after the command has been given, a small second terminal window pops up that acts as a "camera control". This gives the possibility to control the view point ("camera") on the life animation in the first terminal window, to move upward, downward, leftward or rightward, by means of pressing the corresponding arrow keys. Additionally, zooming in and out as well as resetting the position is possible as follows:

	<PAGEUP>        zoom in
	<PAGEDOWN>      zoom out
	<HOME>          reset, center

In order to stop the program, press:

	Ctrl-C

or

	<END>

The zip file 'life_startconditions.zip' contains alternative versions to 'life_startcondition.txt', by which the game can be made to develop differently.


# Author:
Written by Rob Toscani (rob_toscani@yahoo.com).