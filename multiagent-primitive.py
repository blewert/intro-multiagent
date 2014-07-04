## Benjamin Williams <eeu222@bangor.ac.uk>
## Horde Labs
## ---
## An example which creates an agent, and draws it continously.
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

#Use the pack geometry manager to layout the canvas widget (otherwise nothing would show)
canvas.pack();

class Agent():
	def __init__(self, canvas, position, size):
		#Constructor, set instance variables to the ones passed to constructor.
		self.canvas   = canvas;
		self.position = position;	
		self.heading  = 0.0;
		self.size     = size;
		
		#Then create a shape on the canvas, and pass it's id back to self.shape.
		self.shape    = self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + size, self.position[1] + size, fill="#ff0000");
		
	def update(self):
		#Relocate this agent's shape to it's new coordinates!
		self.canvas.coords(self.shape, (self.position[0], self.position[1], self.position[0] + self.size, self.position[1] + self.size));

#Create an agent at (x: 15.0, y: 15.0) with a size of 5
someAgent = Agent(canvas, (15.0, 15.0), 5);

while True:
	#Update both the agent and canvas
	someAgent.update();
	canvas.update();