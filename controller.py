import time
import queue

#Controller class
class Controller:
	activePhase = None
	sequence = []
	killed = False
	
	def __init__(self, p):
		if len(p) > 0:
			self.sequence = p
			self.activePhase = 0
			#self.run()
		else:
			print("No controller sequence!!!")
	
	def run(self):
		self.killed = False
		while not self.killed:
			self.sequence[self.activePhase].start()
			self.activePhase = (self.activePhase + 1) % len(self.sequence)
	
	def stop(self):
		self.killed = True
	
class Phase:
	elapsed = 0.0
	min = 0.0
	max = 0.0
	ext = True
	vehicles = queue.Queue()
	demand = 0.0
	
	id = None
	def __init__(self,min, max, id):
		self.min = min
		self.max = max
		self.id = id
	
	def start(self):
		print("start of phase "+str(self.id))
		self.elapsed = 0.0
		for i in range(self.min):
			time.sleep(1)
			self.elapsed += 1
			self.evaluateExtension()
		while self.extend() and self.elapsed < self.max:
			time.sleep(0.1)
			self.elapsed += 0.1
	
	def extend(self):
		# TODO: get positions of cars
		
		# TODO: get threshold size
		
		# TODO: use CFM to update all vehicle speeds
		
		# TODO: use previous speeds to update positions
		
		# TODO: use new positions to determine if there is a car inside threshold
		
		return self.ext

class Generator:
	def generateVehicles():
		# Use random number generator to create new vehicles randomly according to demand w/ random attributes
		
		# Be sure to ensure that if the link is full that no new vehicles are generated
		pass