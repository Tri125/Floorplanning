from SlicingNode import SlicingNode
from Rectangle import Rectangle

class SlicingTree:
	def __init__(self):
		self._root = None
		self._rectangles = []
		self._permutations = []

	def addRectangle(self, rect):
		id, width, height = rect
		rect = Rectangle(id, width, height)
		self._rectangles.append(rect)
		
	def generateRandomInfix(self):
		postfix = []
		operand = len(self._rectangles)
		expression = ""
		operator = ["-", "|"]
		
		for x in range (0, operand):
			if (x != (operand) and x != 0):
				expression += operator[x%2]		
			
			expression += self._rectangles[x].getId() 
			
			 
		print(expression)
		
	def permutations(self, infix):
		pass
		
		
		
		
		
objets = []
objets.append(("A", 2, 7))
objets.append(("B", 5, 3))
objets.append(("C", 5, 2))

teste = SlicingTree()
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])


teste.generateRandomInfix()
		