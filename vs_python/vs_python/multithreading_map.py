from multiprocessing.dummy import Pool as ThreadPool

#------- demo 0 ---------
def worker(x):
	"""thread worker funciotn"""
	
	print 'worker'
def start_worker():
    th.start_new_thread(worker,())

a=[0,1,2]
pool = ThreadPool(1)
results = pool.map(worker,a)
pool.close()
pool.join()


#---------------------