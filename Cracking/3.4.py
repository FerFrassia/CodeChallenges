import Queue

tower1 = Queue.LifoQueue()
tower2 = Queue.LifoQueue()
tower3 = Queue.LifoQueue()

tower1aux = Queue.LifoQueue()
tower2aux = Queue.LifoQueue()
tower3aux = Queue.LifoQueue()

def show(t1, t2, t3):
	while (not t1.empty()):
		top1 = t1.get()
		top2 = t2.get()
		top3 = t3.get()

		tower1aux.put(top1)
		tower2aux.put(top2)
		tower3aux.put(top3)

		print '  ' + str(top1) + '		  ' + str(top2) + ' 		  ' + str(top3)

	putback(t1, tower1aux)
	putback(t2, tower2aux)
	putback(t3, tower3aux)

def putback(t, taux):
	while (not taux.empty()):
		topAux = taux.get()
		t.put(topAux)	


tower1.put(13)
tower1.put(12)
tower1.put(11)

tower2.put(23)
tower2.put(22)
tower2.put(21)

tower3.put(33)
tower3.put(32)
tower3.put(31)
print 'tower1 	        tower2          tower3'
show(tower1, tower2, tower3)

