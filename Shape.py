#create a class
class Shape:

	#initialize method mandatory for all class
	def __init__(self, height, width, color):
		#assign constructor variables
		self.height = height
		self.width = width
		self.color = color
		
	#create show color method, if you have no parameter a method you have to use self, if you can use instance object
	def show_color(self):
		#if you write a parameter with text you use f" and parameter name between { and }
		print(f"This shape's color is {self.color}\n")