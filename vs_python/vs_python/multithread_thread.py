# http://python.jobbole.com/81255/
# thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装

import thread as th

#------- demo 0 ---------
def worker():
	"""thread worker funciotn"""
	print 'worker'
def start_worker():
    th.start_new_thread(worker,())
#---------------------


