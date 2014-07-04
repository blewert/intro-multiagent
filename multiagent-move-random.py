## Benjamin Williams <eeu222@bangor.ac.uk>
## Horde Labs
## ---
## A simple example which involves drawing multiple agents moving around an environment, randomly.
## 

#Import tkinter module for python 2.7, if you're running 3, use Tkinter as the module name.
import tkinter as tk
import math
import random

#The environment width and height that we wish to simulate
environment_width  = 400;
environment_height = 400;

#Firstly, initialize a tkinter window to attach widgets to.
window = tk.Tk();

#Then, create a canvas with the specified width and height inside the window that was just created.
canvas = tk.Canvas(window, width=environment_width, height=environment_height);

#Use the pack geometry manager to layout the canvas widget (otherwise nothing would show), and update (to initially show).
canvas.pack();
canvas.update();

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
		
	def fd(self, amount):
		#Moving forward. Firstly calculate the coordinate in front of the agent (with the relative angle as the agent's heading),
		#and wrap to the canvas width/height.
		calcX = (self.xcor() + math.cos(self.heading) * amount) % self.canvas.winfo_width();
		calcY = (self.ycor() + math.sin(self.heading) * amount) % self.canvas.winfo_height();

		#Then simply relocate the agent!
		self.position = (calcX, calcY);
	
	def xcor(self):
		#Return the first number in the position tuple
		return self.position[0];
	
	def ycor(self):
		#Return the second number in position tuple
		return self.position[1];
	
	def setheading(self, heading):
		#Set their heading to the one specified clamped between 0 <-> 360
		self.heading = (heading % 360.0);
		
	def randomturn(self, magnitude):
		#Randomly turn the agent by the magnitude
		self.heading += random.uniform(-magnitude, +magnitude);
	
	def randomxy(self):
		#Generate a random numbers between 0 and the width/height of the canvas
		randX = random.uniform(0.0, self.canvas.winfo_width());
		randY = random.uniform(0.0, self.canvas.winfo_height());
		
		#.. and set this agent's position to them!
		self.position = (randX, randY);
	
	def randomheading(self):
		#Simply generate a random number between 0 and 360 and set this agent's heading to it
		self.heading = random.uniform(0.0, 360.0);
		
#Generate 15 agents in a list
agents = [ Agent(canvas, (0.0, 0.0), 10) for i in range(0, 55) ];

#Firstly, set all their positions/heading to random
for agent in agents:
	agent.randomxy();
	agent.randomheading();
	
while True:
	#And then, each step move each agent forward, turn them and relocate them.
	for agent in agents:
		agent.randomturn(0.5);
		agent.fd(2);
		agent.update();
	
	#Then redraw!
	canvas.update();
	