class Rectangle:
	def __init__(self, id, width, height):
		self._width = width
		self._height = height
		self._flip = False
		self._id = id
		
	def ToggleFlip(self):
		self._flip = not self._flip
		self._width, self._height = self._height, self._width
		
	def getWidth(self):
		return self._width
	
	def getHeight(self):
		return self._height
		
	def getFlip(self):
		return self._flip
	
	def getId(self):
		return self._id