from SlicingNode import SlicingNode
from Rectangle import Rectangle
from ArrayStack import ArrayStack

class SlicingTree:
	def __init__(self):
		self._root = None
		self._rectangles = []
		self._permutations = []

	def addRectangle(self, rect):
		id, width, height = rect
		rect = Rectangle(id, width, height)
		self._rectangles.append(rect)
		
	
	def generateInfix(self, stringOperand, listOperator):
		listExpression = []
		expression = ""
		expressionInvertOp = ""
		for x in range(0,len(stringOperand)):
			expression += stringOperand[x]
			expressionInvertOp += stringOperand[x]
			if (x != len(stringOperand)-1):
				expression += listOperator[0][x]
				expressionInvertOp += listOperator[1][x]
		listExpression.append(expression)
		listExpression.append(expressionInvertOp)
				
		return listExpression
		
		
	def InfixToPostFix(self, infixExpression):
		stackyStack = ArrayStack()
		operator = ["-", "|"]
		stringPostfix = ""
		
		for character in infixExpression:
			if (character not in operator):
				stringPostfix += character
			elif stackyStack.is_empty():
				stackyStack.push(character)
			else:
				stringPostfix += stackyStack.pop()
				stackyStack.push(character)
				
				
		while (not stackyStack.is_empty()):
			stringPostfix += stackyStack.pop()		
			
		return stringPostfix
		
	
	def operatorGeneration(self, nbOperator):
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
		
		
	def generateInitialSolution(self):
		stringOperand = []
		listInfixExpression = []
		listPostfixExpression = []
		
		for x in self._rectangles:
			stringOperand+=(x.getId())
			
		listOperator = self.operatorGeneration(len(stringOperand) - 1)
		listInfixExpression = self.generateInfix(stringOperand, listOperator)
		
		for expression in listInfixExpression:
			listPostfixExpression.append(self.InfixToPostFix(expression))
			
		
		print(listOperator)
		print(stringOperand)
		print(listInfixExpression)
		print(listPostfixExpression)
	
		
	# def SlicingPermutations(self):
		# operand = ""
		# permutations = []
				
		# for x in self._rectangles:
			# operand += x.getId()

		# for x in self.all_perms(operand):
			# permutations.append(x)
		# listOperatorPerm = self.operator_perms(len(self._rectangles)-1)
		# listInfixExpression = self.generateInfix(permutations, listOperatorPerm)
		
		# for x in listInfixExpression:
			# print(x)
		
	#http://code.activestate.com/recipes/252178/	
	# def all_perms(self, elements):
		# if len(elements) <=1:
			# yield elements
		# else:
			# for perm in self.all_perms(elements[1:]):
				# for i in range(len(elements)):
					#nb elements[0:1] works in both string and list contexts
					# yield perm[:i] + elements[0:1] + perm[i:]
		
		
objets = []
objets.append(("A", 2, 7))
objets.append(("B", 5, 3))
objets.append(("C", 5, 2))




teste = SlicingTree()
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])


teste.generateInitialSolution()
		