#Vehicle class
class Vehicle:
	position = None
	velocity = None
	maxAcceleration = None
	maxBraking = None
	length = None
	vehInFront = None
	vehBehind = None
	reactionTime = None
	desiredSpeed = None
	
	def updatePosition(self):
		# Update position based on v(t-1)
		pass
	
	def updateVelocity(self):
		# use car following model to determine new velocity
		pass