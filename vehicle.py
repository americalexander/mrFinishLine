import math
import random
import sys
#Vehicle class
class Vehicle:
	def __init__(self, approach, time):
		self.maxAcceleration = random.normalvariate(1.7,0.3)
		self.maxBraking = -2*self.maxAcceleration
		self.length = random.normalvariate(6.5,0.3)
		self.desiredSpeed = max(0,random.normalvariate(approach.speedLimit, approach.speedLimit*0.16))
		self.reactionTime = 2.0/3.0
		self.bnminus1est = min(-3,(self.maxBraking-3.0))/2.0
		self.approach = approach
		self.phase = approach.phase
		self.startTime = time
		self.tripDist = 0.0
		self.commRange = random.normalvariate(300,33)
		self.pastVelocities = [self.desiredSpeed] * math.ceil(10*self.reactionTime+1)
		self.pastPositions = []
		self.vehInFront = None
		for i in range(math.ceil(10*self.reactionTime+1)-1,-1,-1):
			self.pastPositions.append(approach.length + self.desiredSpeed*0.1*i)
	
	def advance(self, j):
		if self.vehInFront != None and self.vehInFront.pastPositions[-1] < 0:
			self.vehInFront = None
		
		vclear = self.pastVelocities[0] + 2.5 * self.maxAcceleration * self.reactionTime * (1-self.pastVelocities[0]/self.desiredSpeed) * (0.025 + self.pastVelocities[0]/self.desiredSpeed)**0.5
		vcar = self.getCarV()
		vlight = self.getLightV()
		v = max(0,min(vclear, vcar, vlight))
		self.pastVelocities.append(v)
		del self.pastVelocities[0]
		curPosition = self.pastPositions[-1]-v*0.1
		self.pastPositions.append(curPosition)
		del self.pastPositions[0]
		if curPosition < 0:
			sys.stdout.write(str(j-self.startTime)+","+str(self.phase.ext)+"\n")
			return True
	
	def delay(self):
		ffTime = self.tripDist/self.desiredSpeed
		return travelTime - ffTime
	
	def getCarV(self):
		if (not self.vehInFront == None):
			return self.maxBraking * self.reactionTime + max(0,((self.maxBraking**2)*(self.reactionTime**2)-self.maxBraking*(2*(-self.vehInFront.pastPositions[0]+self.vehInFront.length+self.pastPositions[0])-self.pastVelocities[0]*self.reactionTime-self.vehInFront.pastVelocities[0]**2/self.bnminus1est)))**0.5
		else:
			return float('inf')
	
	def getLightV(self):
		if self.phase.isRed[0]:
			vlight = self.maxBraking * self.reactionTime + max(0,((self.maxBraking**2)*(self.reactionTime**2)-self.maxBraking*(2*(self.pastPositions[0])-self.pastVelocities[0]*self.reactionTime)))**0.5
			if self.pastPositions[-1] < 1:
				vlight = vlight * (self.pastPositions[-1])
		else:
			vlight = float('inf')
		return vlight