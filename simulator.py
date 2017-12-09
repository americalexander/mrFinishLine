import random
from controller import *
from vehicle import *
import sys
class Simulator:
	def __init__(self,seed):
		random.seed(seed)
		
		limit = 18000
		demand = 400.0
		ts1 = []
		ts2 = []
		pct = 0.9
		for i in range(int(demand*pct)):
			ts1.append(random.randint(0,limit))
		for i in range(int(demand*(1.0-pct))):
			ts2.append(random.randint(0,limit))
		p1 = Phase(300,500, True)
		app1 = Approach(p1, 4000, ts1)
		p2 = Phase(300,500, False)
		app2 = Approach(p2, 4000, ts2)
		controller = Controller([p1,p2])
		i = 0
		while i < limit:
			i+=1
			app1.advance(i)
			app2.advance(i)
			veh1 = None
			veh2 = None
			if len(app1.vehs)>0 :
				veh1 = app1.vehs[0]
				veh1 = veh1.pastPositions[-1]
			if len(app1.vehs) > 1:
				veh2 = app1.vehs[1]
				veh2 = veh2.pastPositions[-1]
			#print("\r"+str(veh1)+"\t"+str(veh2)+"\t"+str(app1.phase.isRed[-1]))
			controller.advance()
		#print(len(app1.vehs)+len(app2.vehs))