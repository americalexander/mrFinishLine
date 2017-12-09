import time
import queue
from vehicle import *
#Controller class
class Controller:
	
	def __init__(self, p):
		self.sequence = p
		self.activePhase = 0
		self.sequence[self.activePhase].start()
	
	def advance(self):
		for i in range(len(self.sequence)):
			self.sequence[i].advance()
		if self.sequence[self.activePhase].isRed[-1]:
			self.activePhase = (self.activePhase + 1) % len(self.sequence)
			self.sequence[self.activePhase].start()
	
class Phase:
	def __init__(self,min, max):
		self.elapsed = 0.0
		self.approach = None
		self.isRed = [True]*7
		self.min = min
		self.max = max
	
	def extend(self):
		# TODO: get positions of cars
		veh = self.approach.vehs[0]
		if (veh == None) or veh.pastPositions[-1] > veh.commRange:
			return False
		vp = veh.pastPositions[-1]
		
		# TODO: get threshold size
		timeLeft = self.max - self.elapsed
		ttt = timeLeft/10.0 * self.approach.speedLimit
		
		if ttt >= vp:
			return True
		
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
	def __init__(self, phase, length, ts):
		self.vehs = []
		self.length = 0.0
		self.phase = phase
		self.speedLimit = 20.0
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
				if self.vehs[1] != None:
					self.vehs[1].vehInFront = None
				del self.vehs[0]
