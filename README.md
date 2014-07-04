intro-multiagent
================

This is a repository of sample code used throughout the introduction to creating a multi-agent system in Python. Each of the snippets of code in the blog post has been expanded upon, and provide fully working examples for Python 2.7. Note that if you want these examples to run using Python 3, you have to change Tkinter's module name from `tkinter` (lowercase) to `Tkinter` (sentence case).

The following examples of code are provided:
* **tkinter-helloworld.py** - An example which uses Tkinter to draw a square in the middle of a Tkinter Canvas widget, and updates it indefinitely.
* **tkinter-move.py** - An example which creates a square within a Tkinter Canvas widget, and moves it diagonally by relocating it with `Canvas.coords(...)`.
* **multiagent-primitive.py** - An example which introduces a class to represent a single agent out of many, creates an agent and continously redraws it.
* **multiagent-move.py** - An example which creates 15 agents within an environment, and moves them around the canvas without randomly turning them.
* **multiagent-move-random.py** - An example which creates 55 agents within an environment, and randomly moves them around the canvas whilst randomly turning them (almost like a wander behaviour).

