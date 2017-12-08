import time
import queue
from vehicle import *
#Controller class
class Controller:
	activePhase = None
	sequence = []
	killed = False
	
	def __init__(self, p):
		self.sequence = p
		self.activePhase = 0
	
	def advance(self):
		for i in range(len(self.sequence)):
			self.sequence[i].advance()
		if self.sequence[self.activePhase].isRed[-1]:
			self.activePhase = (self.activePhase + 1) % len(self.sequence)
			self.sequence[self.activePhase].start()
	
class Phase:
	elapsed = 0.0
	min = 0.0
	max = 0.0
	demand = 0.0
	approach = None
	isRed = [True]*7
	
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
		
		return False
	
	def advance(self):
		if self.isRed[-1]:
			self.isRed.append(True)
		else:
			self.elapsed += 0.1
			if self.elapsed >= self.max:	#Reached max limit
				self.isRed.append(True)		#Turn red
			elif self.elapsed < self.min:	#Still in min time
				self.isRed.append(False)	#Stay green
			elif self.extend():				#Extension based on V2I
				self.isRed.append(False)	#Stay green
			else:							#No extension
				self.isRed.append(True)		#Turn red
		del self.isRed[0]
	
	def setApproach(self, approach):
		self.approach = approach
	
	def start(self):
		self.isRed[-1] = False
		self.elapsed = 0.0

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
			if len(self.vehs) > 0:
				v.vehInFront = self.vehs[-1]
			self.vehs.append(v)
	
	def advance(self, j):
		self.generateVeh(j)
		exited = [False] * len(self.vehs)
		for i in range(len(self.vehs)):
			exited[i] = self.vehs[i].advance(j)
		for i in range(len(exited)):
			if exited[i]:
				if self.vehs[i+1] != None:
					self.vehs[i+1].vehInFront = None
				del self.vehs[i]
