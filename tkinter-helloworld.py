## Benjamin Williams <eeu222@bangor.ac.uk>
## Horde Labs
## ---
## A very basic example of using Tkinter to draw a square in the middle of the canvas, and continue drawing it.
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

#And finally, run until the application is terminated, reupdating the canvas.
while True:
	canvas.update();