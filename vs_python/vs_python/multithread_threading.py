# http://python.jobbole.com/81255/
import threading as thing
import numpy as np
a = np.array([0,1,2])

#------- demo 0 ---------
def worker():
	"""thread worker funciotn"""
	print 'worker'

def start_worker():
    t = thing.Thread(target=worker)
    t.start()
#---------------------


