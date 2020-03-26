#import shape for inherit to rectangle class
from Shape import Shape

#create Rectangle class and extend Shape
class Rectangle(Shape):

	#initialize method mandatory for all class
	def __init__(self, height, width, color, border_size):
		#use super() method for calling abstract class initialize method
		super().__init__(height, width, color)
		#assign constructor variable
		self.border_size = border_size
		
	#create show perimeter method, if you have no parameter a method you have to use self, if you can use instance object
	def show_perimeter(self):
		#perimeter formula
		perimeter = 2*self.height+2*self.width
		#if you write a parameter with text you use f" and parameter name between { and }  
		print(f"This rectangle perimeter is {perimeter}\n")
		
	#create show border size method, if you have no parameter a method you have to use self, if you can use instance object
	def show_border_size(self):
		#if you write a parameter with text you use f" and parameter name between { and }
		print(f"This rectangle's border size is {self.border_size}\n")