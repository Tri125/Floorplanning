from SlicingNode import SlicingNode
from Rectangle import Rectangle
from ArrayStack import ArrayStack
from collections import OrderedDict
import random
import math

class SlicingTree:
		def __init__(self):
				self._root = None
				self._rectangles = []
				self._permutations = []
				self._dictionnary = {}
				
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
				
		def PrefixToPostFix(self, prefixExpression):
			stack = ArrayStack()
			operator = ["-", "|"]
			#operator = ["+", "-"]
			stringPostfix = ""
			prefixExpression = prefixExpression[::-1]
			for x in range(0, len(prefixExpression)):
				if (prefixExpression[x] in operator):
					one = stack.pop()
					second = stack.pop()
					stack.push(one+second+prefixExpression[x])
				else:
					stack.push(prefixExpression[x])
			while (not stack.is_empty()):
						stringPostfix += stack.pop()   
			return stringPostfix
			
			
		def PostFixToPrefix(self, postfixExpression):
			stack = ArrayStack()
			operator = ["-", "|"]
			#operator = ["+", "-"]
			stringPrefix = ""
			for x in range(0, len(postfixExpression)):
				if (postfixExpression[x] in operator):
					second = stack.pop()
					one = stack.pop()
					stack.push(postfixExpression[x]+one+second)
				else:
					stack.push(postfixExpression[x])
			while (not stack.is_empty()):
						stringPrefix += stack.pop()
			return stringPrefix
		
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
				
				#Parce que le deuxieme dans la liste est avec les operateurs inverse
				return listPostfixExpression[0]
		
		
		def SwapOperatorOperand(self, postfixExpression):
				indexOperand = []
				operator = ["-", "|"]
				swapList = []
				#print(postfixExpression)
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
				
				#print(postfixExpression)
				return postfixExpression
				#iter = re.finditer('(\w{1})([\-\|]{1})(\w{1})', postfixExpression)
				#indices = [m.start(0) for m in iter]
				#print(indices)
				##print("{} {} {}".format(left, operator, right))

		def AreaComputation(self, postfixExpression):
			stacky = ArrayStack()
			#operator = ["V","H"]
			operator = ["-", "|"]
			BestCandidate = 0
			RealDict = {}
			RealNote = ""
			for y in range(0, 2**len(self._rectangles)):
				rectCounter = 0
				flipDict = {}
				FlipNote = "{0:b}".format(y)
				FlipNote = "0"* (len(self._rectangles)-len(FlipNote)) + FlipNote
				for x in range(0, len(postfixExpression)):
					currentChar = postfixExpression[x]
					if (currentChar not in operator):
						rect = self._dictionnary[currentChar]
						flipDict[currentChar] = "0"
						if (FlipNote[rectCounter] == "1"):
							#print(rectCounter)
							#print(FlipNote)
							#print("Is flipping " + currentChar)
							flipDict[currentChar] = "1"
							rect = rect[::-1] 
						stacky.push(rect)
						rectCounter += 1
					else:
						Rightchild = stacky.pop()
						Leftchild = stacky.pop()
						rightWidth, rightHeight = Rightchild
						leftWidth, leftHeight =	Leftchild
					
						if (currentChar == operator[0]): #Vertical slice
							stacky.push((rightWidth+leftWidth, (max(rightHeight,leftHeight))))
						elif (currentChar == operator[1]): #Horizontal slice
							stacky.push((max(rightWidth,leftWidth),rightHeight+leftHeight))
						else:
							print("Erreur AreaComputation. Invalid Operator in postfixExpression :" + postfixExpression + " " + postfixExpression[x])
				#print(stacky)
				width, height = stacky.pop()
				area = width * height
				#print("Area : " + str(area))
				if (area < BestCandidate or BestCandidate == 0):
					RealDict = flipDict
					BestCandidate = area
					RealNote = FlipNote 
			RectRotation = ""
					
			#print("Best : " + str(BestCandidate))
			ordered = OrderedDict(sorted(RealDict.items(), key=lambda t: t[0]))
			while(len(ordered) != 0):
				key, value = ordered.popitem(False)
				if(value == "1"):
					RectRotation += "0"
				elif (value =="0"):
					RectRotation += "1"
			#print(RectRotation)
			return BestCandidate
			
			
			
		def TestBallotingProperty(self, postfix):
				operator = ["-", "|"]
				#operator = ["H", "V"]
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
				#print(postfix)
				#print(nbOperand)
				#print(nbOperator)
				return True
				
				
						
				
		
		def SwapOperand(self, postfixExpression):
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
				
				#print(postfixExpression)
				return postfixExpression
		
		def StartFloorPlanSolver(self):
			self._dictionnary = {rect.getId(): (rect.getWidth(), rect.getHeight()) for rect in self._rectangles}
			print(self._dictionnary)
			postfix = self.generateInitialSolution()
			bestExpression = self.WongLiuFloorplanning(postfix)
			prefixResult = self.PostFixToPrefix(bestExpression)
			print("Aire minimal " + str(self.AreaComputation(bestExpression)))
			print("Postfix " + bestExpression)
			print("Prefix " + prefixResult)
			
		
		
		def ComputeUphillAverage(self, postfixExpression, K = 20):
			previousExpression = postfixExpression
			deltaAverage = 0
			reject = 0
			for ite in range(0,K):
				OperationChoice = random.randint(1,2)
				if (OperationChoice == 1):
					postfixExpression = self.SwapOperand(postfixExpression)
				elif (OperationChoice == 2):
					done = False
					while(not done):
						tmp = postfixExpression
						tmp = self.SwapOperatorOperand(tmp)
						if self.TestBallotingProperty(tmp):
							done = True
							postfixExpression = tmp
						
							
				else:
					print("Erreur WongLiuFLoorplanning")
					
				deltaAverage += math.fabs(self.AreaComputation(postfixExpression) - self.AreaComputation(previousExpression))
			deltaAverage = deltaAverage/K
			return deltaAverage
		
		def WongLiuFloorplanning(self, postfixExpression, P = 0.80, sigma = 10, r = 0.85, K = 100):
			bestExpression = postfixExpression
			previousExpression = postfixExpression
			deltaAverage = self.ComputeUphillAverage(postfixExpression,K)
			#print("delta avg :" + str(deltaAverage))
			temperature = -deltaAverage/math.log(P)
			#print("delta " + str(deltaAverage))
			#print("starting tmp " + str(temperature))
			loop = True
			while (loop):
				reject = 0
				for ite in range(0,K):
					OperationChoice = random.randint(1,2)
					if (OperationChoice == 1):
						postfixExpression = self.SwapOperand(postfixExpression)
					elif (OperationChoice == 2):
						while(True):
							tmp = postfixExpression
							tmp = self.SwapOperatorOperand(tmp)
							if self.TestBallotingProperty(tmp):
								postfixExpression = tmp
								break
						
							
					else:
						print("Erreur WongLiuFLoorplanning")
					
					deltaCost = self.AreaComputation(postfixExpression) - self.AreaComputation(previousExpression)
					
					if (deltaCost <= 0 or random.randint(0,1) < math.e - deltaCost/temperature):
						previousExpression = postfixExpression
						if self.AreaComputation(postfixExpression) < self.AreaComputation(bestExpression):
							
							bestExpression = postfixExpression
							print("Best" + str(self.AreaComputation(bestExpression)))
					else:
						reject += 1
				temperature = r*temperature
				print(reject)
				if (reject/K > 0.95 or temperature < sigma):
					loop = False
			return bestExpression
			
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
objets.append(("A", 2, 37))
objets.append(("B", 31, 3))
objets.append(("C", 5, 29))
objets.append(("D", 23, 7))
objets.append(("E", 11, 19))
objets.append(("F", 17, 13))

# objets.append(("A", 2, 29))
# objets.append(("B", 23, 3))
# objets.append(("C", 5, 19))
# objets.append(("D", 17, 7))
# objets.append(("E", 11, 13))


teste = SlicingTree()
teste.addRectangle(objets[0])
teste.addRectangle(objets[1])
teste.addRectangle(objets[2])
teste.addRectangle(objets[3])
teste.addRectangle(objets[4])
teste.addRectangle(objets[5])

teste.StartFloorPlanSolver()

#teste.TestBallotingProperty()
	
				
