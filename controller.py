import time

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
	elapsed = 0
	min = 0
	max = 0
	extend = True
	
	id = None
	def __init__(self,min, max, id):
		self.min = min
		self.max = max
		self.id = id
	
	def start(self):
		print("start of phase "+str(self.id))
		self.elapsed = 0
		for i in range(self.min):
			time.sleep(1)
			self.elapsed += 1
			self.evaluateExtension()
		while self.extend and self.elapsed < self.max:
			time.sleep(1)
			self.elapsed += 1
			self.evaluateExtension()
		
	def evaluateExtension(self):
		pass