## Benjamin Williams <eeu222@bangor.ac.uk>
## Horde Labs
## ---
## An example which draws a rectangle using Tkinter, and moves it diagonally until terminated.
## 

#Import tkinter module for Python 2.7, if you're running Python 3, use Tkinter as the module name instead.
import tkinter as tk

#The environment width and height that we wish to simulate
environment_width  = 400;
environment_height = 400;

#Firstly, initialize a tkinter window to attach widgets to.
window = tk.Tk();

#Then, create a canvas with the specified width and height inside the window that was just created, and update it.
canvas = tk.Canvas(window, width=environment_width, height=environment_height);
canvas.update();

#Next, create a rectangle on the canvas with the specified coordinates and fill colour.
rectangle = canvas.create_rectangle(175, 175, 225, 225, fill="#ff0000");

#Use the pack geometry manager to layout the canvas widget (otherwise nothing would show)
canvas.pack();

#Current x and y coordinates of the square.
x = 5;
y = 5;

#The size of the square
size = 10;

while True:
	#Increment current x and y of the rectangle, and wrap them both to the width/height 
	#of the environment, by using the modulus operator.
	x = (x + 1) % environment_width;
	y = (y + 1) % environment_height;
	
	#Relocate the square by passing coords() it's unique ID, and where to relocate it to.
	canvas.coords(rectangle, x, y, x+size, y+size);
	canvas.update();