from SlicingNode import SlicingNode
from Rectangle import Rectangle
from ArrayStack import ArrayStack
import random
import re

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
				indexOperand = []
				operator = ["-", "|"]
				swapList = []
				print(postfixExpression)
				for x in range(0, len(postfixExpression)):
					if (postfixExpression[x] in operator):
						if x != 0 and postfixExpression[x-1] not in operator:
							swapList.append( (x, x-1))
						if x != len(postfixExpression)-1 and postfixExpression[x+1] not in operator:
							swapList.append( (x, x+1))
				
				random.shuffle(swapList)
				selection = random.randint(0, len(swapList)-1)
				one, second = swapList[selection]
				tmp = list(postfixExpression)   
				tmp[one], tmp[second] = tmp[second], tmp[one]
				postfixExpression = ''.join(tmp)
				
				print(postfixExpression)
				#iter = re.finditer('(\w{1})([\-\|]{1})(\w{1})', postfixExpression)
				#indices = [m.start(0) for m in iter]
				#print(indices)
				##print("{} {} {}".format(left, operator, right))
				
		def TestBallotingProperty(self):
				postfix = "12H34H5HV"
				#operator = ["-", "|"]
				operator = ["H", "V"]
				nbOperand = [0]*len(postfix)
				nbOperator = [0]*len(postfix)
				OperandCounter = 0
				OperatorCounter = 0
				for x in range(0, len(postfix)):
						if (postfix[x] in operator):
								OperatorCounter += 1
						else:
								OperandCounter += 1
						nbOperator[x] = OperatorCounter
						nbOperand[x] = OperandCounter
						
						if(nbOperator[x] >= nbOperand[x]):
								return False
				print(postfix)
				print(nbOperand)
				print(nbOperator)
				return True
				
				
						
				
		
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


#teste.generateInitialSolution()
#teste.TestBallotingProperty()
#for x in range(0, 100000):
teste.SwapOperatorOperand("12|4-5|3-")
				
