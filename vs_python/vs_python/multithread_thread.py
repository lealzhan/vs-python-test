# http://python.jobbole.com/81255/
# thread��threading��thread�ǵͼ�ģ�飬threading�Ǹ߼�ģ�飬��thread�����˷�װ

import thread as th

#------- demo 0 ---------
def worker():
	"""thread worker funciotn"""
	print 'worker'
def start_worker():
    th.start_new_thread(worker,())
#---------------------


