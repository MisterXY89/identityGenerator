
import math
import random
from collections import deque

class GaussianChoice:
	def __init__(self, length):
		self.total = 2.5
		self.length = length
		self.leftProbs = self._genProbs()
		self.rightProbs = self.leftProbs[::-1]
		self.centerProbs = self.leftProbs[int(len(self.leftProbs)/2):] + [self.leftProbs[int(len(self.leftProbs)/2)]]

	def _p(self, x):
		# 2 == 100%
		a = 1/(0.5)*math.sqrt(2 * math.pi)
		return math.sqrt(a/(math.pi))*math.pow(math.e, (-a*math.pow(x,2)))/(self.total)

	def _genProbs(self):
		probs = []
		for x in range(0, self.length):
			probs.append(self._p( ( x / (self.length + (0) ))) / (1) )
		normProbs = [float(i)/sum(probs) for i in probs]
		return normProbs

	def getIndex(self, distribution="l"):
		probs = []
		if distribution == "l":
			probs = self.leftProbs
		elif distribution == "r":
			probs = self.rightProbs
		elif distribution == "c":
			probs = self.centerProbs

		r = random.random()
		index = 0
		while(r >= 0 and index < len(probs)):
			r -= probs[index]
			index += 1
		return index - 1
