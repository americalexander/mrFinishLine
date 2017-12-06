import math
#Vehicle class
class Vehicle:
	maxAcceleration = None
	maxBraking = None
	length = None
	vehInFront = None
	reactionTime = None
	desiredSpeed = None
	bnminus1est = None
	phase = None
	startTime = None
	tripDist = None
	pastPositions = []
	pastVelocities= []
	travelTime = None
	
	def __init__(self, approach, time):
		self.maxAcceleration = random.normalvariate(1.7,0.3)
		self.maxBraking = -2*self.maxAcceleration
		self.length = random.normalvariate(6.5,0.3)
		self.desiredSpeed = random.normalvariate(20.0, 3.2)
		self.reactionTime = 2.0/3.0
		self.bnminus1est = min(-3,(self.maxBraking-3.0))/2.0
		self.phase = approach.phase
		self.startTime = time
		self.tripDist = approach.length
		self.pastVelocities = [self.desiredSpeed] * math.ceil(10*self.reactionTime)
		for i in range(math.ceil(10*self.reactionTime)-1,-1,-1):
			self.pastPositions.append(approach.length + self.velocity*0.1*i)
	
	def advance(self, j):
		pass
	
	def delay(self):
		ffTime = self.tripDist/self.desiredSpeed
		return travelTime - ffTime