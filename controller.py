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
			self.run()
		else:
			print("No controller sequence!!!")
	
	def run(self):
		while not self.killed:
			self.sequence[self.activePhase].start()
			self.activePhase = (self.activePhase + 1) % len(sequence)
	
	def stop(self):
		self.killed = True
	
class Phase:
	length = 0
	id = None
	def __init__(self,l, id):
		self.length = l
		self.id = id
	
	def start(self):
		print("start ofphase "+str(self.id))
		t0 = time.time()
		while time.time() < t0 + self.length:
			time.sleep(0.5)