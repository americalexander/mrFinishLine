import time
import queue

#Controller class
class Controller:
	activePhase = None
	sequence = []
	killed = False
	
	def __init__(self, p):
		self.sequence = p
		self.activePhase = 0
	
	def advance(self):
		extend = self.sequence[self.activePhase].advance()
		if not extend:
			self.activePhase = (self.activePhase + 1) % len(self.sequence)
	
class Phase:
	elapsed = 0.0
	min = 0.0
	max = 0.0
	demand = 0.0
	approach = None
	
	id = None
	def __init__(self,min, max):
		self.min = min
		self.max = max
	
	def extend(self):
		# TODO: get positions of cars
		
		# TODO: get threshold size
		
		# TODO: use CFM to update all vehicle speeds
		
		# TODO: use previous speeds to update positions
		
		# TODO: use new positions to determine if there is a car inside threshold
		
		return self.ext
	
	def advance(self):
		self.elapsed += 0.1
		if self.elapsed >= self.max:
			return True
		elif self.elapsed < self.min:
			self.elapsed = 0.0
			return False
		else:
			ext = self.extend()
			if not ext:
				self.elapsed = 0.0
			return ext
	
	def setApproach(self, approach):
		self.approach = approach

class Approach:
	vehs = []
	length = 0.0
	ts = []
	phase = None
	
	def __init__(self, phase, length, ts):
		self.phase = phase
		self.phase.setApproach(self)
		self.length = length
		self.ts = ts
	
	def generateVeh(self, j):
		if j in self.ts:
			v = Vehicle(self, j)
			if len(vehs) > 0:
				v.vehInFront = vehs[-1]
			vehs.append(v)
	
	def advance(self, j):
		self.generateVeh(j)
		for i in range(len(self.vehs)):
			exited = self.vehs[i].advance(j)
			if exited:
				if self.vehs[i+1] != None:
					self.vehs[i+1].vehInFront = None
				del self.vehs[i]
