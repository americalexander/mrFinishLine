class Simulator:
	random.seed(1831)
	
	limit = 18000
	demand = 200
	ts1 = []
	ts2 = []
	for i in range(demand):
		ts1.append(random.randint(0,limit))
		ts2.append(random.randint(0,limit))
	p1 = Phase(300,500)
	app1 = Approach(p1, 4000, ts1)
	p2 = Phase(300,500)
	app2 = Approach(p2, 4000, ts2)
	i = 0
	while i < limit:
		i+=1
		app1.advance(i)
		app2.advance(i)
		controller.advance()