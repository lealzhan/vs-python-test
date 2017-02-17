# http://python.jobbole.com/81255/
# thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装

import threading as thing
import numpy as np
a = np.array([0,1,2])


lock = thing.Lock()


def worker():
	"""thread worker funciotn"""
	print thing.current_thread().getName()
	
	# 先要获取锁:
	lock.acquire()
	try:
		for x in [0,1000]:
			a[0] = 1
		print thing.current_thread().getName()," done"
	finally:
		# 改完了一定要释放锁:
		lock.release()

	b=0;
	while 1>0 :
		b += 1
		b -= 1
		b /= 1


if __name__ == '__main__':
    print thing.current_thread().getName()
    t0 = thing.Thread(target=worker, name='WorkerThread0')
    t1 = thing.Thread(target=worker, name='WorkerThread1')
    t0.start()
    t1.start()
    t0.join()
    t1.join()
    print a