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
		listExpression = []
		
		for x in listOperand:
			expression = ""
			expressionInvertOp = ""
			for y in range (0, len(x)):
				expression += x[y]
				expressionInvertOp += x[y]
				if (y != len(x)-1):
					expression += listOperator[0][y]
					expressionInvertOp += listOperator[1][y]
			listExpression.append(expression)
			listExpression.append(expressionInvertOp)
				
		return listExpression
		
		
	def InfixToPostFix(self, infixExpression):
		pass
		
		
	
	def operator_perms(self, nbOperator):
		operator = ["-", "|"]
		listOperator = []
		listOperatorReverse = []
		listOperatorPerm = []
		for x in range (0, nbOperator):
			listOperator.append(operator[x%2])
			listOperatorReverse.append(operator[(x+1)%2])
		listOperatorPerm.append(listOperator)
		listOperatorPerm.append(listOperatorReverse)
		
		return listOperatorPerm
		

	
		
	def SlicingPermutations(self):
		operand = ""
		permutations = []
				
		for x in self._rectangles:
			operand += x.getId()

		for x in self.all_perms(operand):
			permutations.append(x)
		listOperatorPerm = self.operator_perms(len(self._rectangles)-1)
		listInfixExpression = self.generateInfix(permutations, listOperatorPerm)
		
		for x in listInfixExpression:
			print(x)
		
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
#objets.append(("A", 2, 7))
#objets.append(("B", 5, 3))
#objets.append(("C", 5, 2))
objets.append(("0", 5, 2))
objets.append(("8", 5, 2))
objets.append(("9", 5, 2))
objets.append(("1", 5, 2))
objets.append(("3", 5, 2))
objets.append(("5", 5, 2))
objets.append(("7", 5, 2))




teste = SlicingTree()
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])
teste.addRectangle(objets[3])
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])
teste.addRectangle(objets[3])
teste.addRectangle(objets[4])
teste.addRectangle(objets[5])
teste.addRectangle(objets[6])
teste.SlicingPermutations()
		