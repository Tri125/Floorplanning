
class Node:
	
	def __init__(self, data = None, left = None, right = None):
		self._left = left
		self._right = right
		self._data = data
		
	def setLeft(self, left):
		self._left = left
		
	def setRight(self, right):
		self._right = right
		
	def getData(self):
		return self._data
		
	def getLeft(self):
		return self._left
	
	def getRight(self):
		return self._right
		