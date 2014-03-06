from Node import Node

class SlicingNode(Node):

	def __init__(self, data, left = None, right = None):
		super(SlicingNode, self).__init__(data, left, right)
	
	def _setHSlice(self):
		self._data = "-"
		
	def _setVSlice(self):
		self._data = "|"
		
	def setSlice(self, type):
		if (type == "-"):
			self._SetHSlice
		elif (type == "|"):
			self._SetVSlice
		else:
			return False
		
		
		