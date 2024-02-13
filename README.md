# Name: life4.py
life4.py - Program that visualizes John Conway's "Game of Life" in a command terminal.

# Description:
life4.py visualizes John Conway's "Game of Life" in a command terminal, with additional controls to move the viewpoint and to zoom in and out on the animation.
See for background and details: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which (at any given time) is in one of two possible states, "live" (alternatively "on") or "dead" (alternatively "off").[1] Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. The result is a lifely moving theatre of moving "micro-organism"-like entities.

# How to use life4.py:
Place the file 'life_startcondition.txt' in the same directory as the program life4.py, this is the initial pattern of ones and zeroes, constituing the 'seed' of the system determining how the game will start. 

In order to start the "Game of Life" animation, supply the following command in a command terminal, followed by 4 integer arguments:

	./life4.py 82 48 3 23

The first two arguments are the horizontal and vertical grid sizes of the image "canvas" in the terminal. The values 82 and 48 are an example of a adequate grid size, but can of replaced by be changed into other values, dependent upon terminal-type and terminal/character size.

The third and fourth argument represent the settings so-called "Birth rule" and "Survival rule" respectively.
Respective values 3 and 23 render a good probability that the life action on the canvas will persist for some time before dying out.

Immediately after the command has been given, a small second terminal window pops up that acts as a "camera control". This gives the possibility to control the view point ("camera") on the life animation in the first terminal window, to move upward, downward, leftward or rightward, by means of pressing the corresponding arrow keys. Additionally, zooming in and out as well as resetting the position is possible as follows:

	<PAGEUP>/<PAGEDOWN>   zoom in/out
	<HOME>                reset, center

In order to stop the program, press:

	Ctrl-C

or

	<END>

The zip file 'life_startconditions.zip' contains alternative versions to life_startcondition.txt, by which the game can be made to develop differently.

By editing the contents of 'life_startcondition.txt', or replacing it by any of the alternative startconditions in 'life_startconditions.zip')

# # Author:
Written by Rob Toscani (rob_toscani@yahoo.com).