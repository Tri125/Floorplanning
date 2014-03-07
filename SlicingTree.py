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
		
	def generateInfix(self, listOperand, listOperator):
		NbOperand = len(self._rectangles)
		expression = ""
		operator = ["-", "|"]
	
		
		for x in range (0, NbOperand -1):
			listOperator.append(operator[x%2])
		
		for x in range (0, NbOperand):
			expression += listOperand[x]
			if (len(listOperator) != x):
				expression += listOperator[x]
		print(expression)
		return expression
		
	
	def operator_perms(self, nbOperator):
		operator = ["-", "|"]
		listOperator = []
		listOperatorPerm = []
		for x in range (0, nbOperator):
			listOperator.append(operator[0])
		listOperatorPerm.append(listOperator)
		
		for x in range (0, 2**nbOperator)
			
		
		print(listOperatorPerm)
		

	
		
	def SlicingPermutations(self):
		operand = ""
		permutations = []
				
		for x in self._rectangles:
			operand += x.getId()

		for x in self.all_perms(operand):
			permutations.append(x)
		
		print(permutations)
		
	#http://code.activestate.com/recipes/252178/	
	def all_perms(self, elements):
		if len(elements) <=1:
			yield elements
		else:
			for perm in self.all_perms(elements[1:]):
				for i in range(len(elements)):
					#nb elements[0:1] works in both string and list contexts
					yield perm[:i] + elements[0:1] + perm[i:]
		
		
objets = []
objets.append(("A", 2, 7))
objets.append(("B", 5, 3))
objets.append(("C", 5, 2))

teste = SlicingTree()
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])


teste.SlicingPermutations()
#teste.generateInfix()
teste.operator_perms(2)
		