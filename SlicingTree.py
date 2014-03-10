from SlicingNode import SlicingNode
from Rectangle import Rectangle
from ArrayStack import ArrayStack
import random

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
		
		for x in range (0, 100000):
			self.SwapMove(listPostfixExpression[0])
	
	
	def SwapOperatorOperand(self, postfixExpression):
		pass
		
		
	def TestBallotingProperty(self, postfixExpression):
		pass
	
	def SwapMove(self, postfixExpression):
		indexOperand = []
		operator = ["-", "|"]
		#print(postfixExpression)
		for x in range (0,len(postfixExpression)):
			if (postfixExpression[x] not in operator):
				indexOperand.append(x)
		#print(indexOperand)
		one = indexOperand[random.randint(0, len(indexOperand) -1)]
		second = -1
		#Si on choisit un operand à la fin de l'expression
		if (one == indexOperand[len(indexOperand) -1] and len(indexOperand) > 1):
			#print("operand à la fin")
			second = indexOperand[indexOperand.index(one)-1]
		#Si c'est le premier operand
		elif (one == 0 and len(indexOperand) > 1):
			#print("operand au debut")
			second = indexOperand[one+1]
		else:
			#print("choix")
			choix = random.randint(0,1)
			if (choix == 0):
				#print("switch à gauche")
				second = indexOperand[indexOperand.index(one) -1]
			elif(choix == 1):
				#print("switch à droite")
				second = indexOperand[indexOperand.index(one)+1]
		#print(one)
		#print(second)
		tmp = list(postfixExpression)	
		tmp[one], tmp[second] = tmp[second], tmp[one]
		postfixExpression = ''.join(tmp)
		
		print(postfixExpression)
		
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
objets.append(("D", 5, 2))
objets.append(("E", 5, 2))
objets.append(("F", 5, 2))




teste = SlicingTree()
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])
teste.addRectangle(objets[3])
teste.addRectangle(objets[4])
teste.addRectangle(objets[5])


teste.generateInitialSolution()
		