from multiprocessing.dummy import Pool as ThreadPool #thread pool
#from multiprocessing import Pool as ThreadPool     #process pool

import time

#------- demo 0 ---------
def worker(x):
	"""thread worker funciotn"""
	print "worker start" 
	a=0;
	while 1>0 :
		a += 1
		a -= 1
		a /= 1
	print 'worker'

testTP=range(0,100)
pool = ThreadPool(5)
results = pool.map(worker, testTP)
pool.close()
pool.join()

# no gpu usage improved...

#---------------------