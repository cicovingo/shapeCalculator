#import shape for inherit to triangle class
from Shape import Shape

#create Triangle class and extend Shape
class Triangle(Shape):
	#initialize method mandatory for all class
	def __init__(self, height, width, color):
		#use super() method for calling abstract class initialize method
		super().__init__(height, width, color)
		
	#create show area method, if you have no parameter a method you have to use self, if you can use instance object
	def show_area(self):
		#triangle area formula
		area = self.height*self.width/2
		#if you write a parameter with text you use f" and parameter name between { and }
		print(f"This triangle area is {area}\n")