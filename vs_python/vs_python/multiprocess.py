## -*- coding: UTF-8 -*-   
  
#from multiprocessing import Pool, Lock, Value  
#import os  
  
#tests_count = 80  
  
#lock = Lock()  
  
#counter = Value('i', 0) # int type???൱??java??????ԭ?ӱ???  
  
  
#def run(fn):  
#    global tests_count, lock, counter  
#    with lock:  
#        counter.value += 1  
  
#    print 'NO. (%d/%d) test start. PID: %d ' %(counter.value, tests_count,  os.getpid())  
#    # do something below ...  
  
  
#if __name__ == "__main__":  
#    pool = Pool(10)  
#    # 80?????񣬻?????run()80?Σ?ÿ?δ???xrange????һ??Ԫ??  
#    pool.map(run, xrange(80))
#    pool.close()  
#    pool.join()  




## -*- coding: UTF-8 -*-   
  
#from multiprocessing import Pool, Lock, Value  
#import os  

#global tests_count, lock, counter
#tests_count = 80  
  
#lock = Lock()  
  
#counter = Value('i', 0) # int type???൱??java??????ԭ?ӱ???  
  
  
#def run(i):
#    print "process:",i

#    with lock:  
#        counter.value += 1  
  
#    print 'NO. (%d/%d) test start. PID: %d ' %(counter.value, tests_count,  os.getpid())  
#    # do something below ...  
  
#if __name__ == "__main__":  
#    pool = Pool()  
#    # 80?????񣬻?????run()80?Σ?ÿ?δ???xrange????һ??Ԫ??  
#    pool.map(run, xrange(80))
#    pool.close()  
#    pool.join()  



## modified from official documentation  
#import multiprocessing  
  
#def f(n, a):  
#    n.value   = 3.14  
#    a[0]      = 5

#def f1(n, a):  
#    n.value   = 5.0 
#    a[0]      = 5
 
#if __name__ == "__main__":
#	num   = multiprocessing.Value('d', 0.0)  
#	arr   = multiprocessing.Array('i', range(10))  

#	p0 = multiprocessing.Process(target=f, args=(num, arr)) 
#	p1 = multiprocessing.Process(target=f1, args=(num, arr))  
#	p0.start()  
#	p0.join()  
#	p1.start()  
#	p1.join()  

#	print num.value  
#	print arr[:]


##coding: utf-8
#import multiprocessing
#import time

#def func(msg):
#    print "msg:", msg
#    time.sleep(3)
#    print "end"

#if __name__ == "__main__":
#    pool = multiprocessing.Pool(processes = 3)
#    for i in xrange(4):
#        msg = "hello %d" %(i)
#        pool.apply_async(func, (msg, ))   #ά??ִ?еĽ???????Ϊprocesses????һ??????ִ?????Ϻ????????µĽ??̽?ȥ

#    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
#    pool.close()
#    pool.join()   #????join֮ǰ???ȵ???close??????????????????ִ????close?󲻻????µĽ??̼??뵽pool,join?????ȴ??????ӽ??̽???
#    print "Sub-process(es) done."



##coding: utf-8
#import multiprocessing
#import time

#def func(msg,num):
#    print "msg:", msg
#    time.sleep(3)
#    print "end"

#if __name__ == "__main__":
#	num   = multiprocessing.Value('d', 0.0)
#	pool = multiprocessing.Pool(processes = 3)
#	for i in xrange(4):
#		msg = "hello %d" %(i)
#		pool.apply_async(func, (msg,num, ))   #ά??ִ?еĽ???????Ϊprocesses????һ??????ִ?????Ϻ????????µĽ??̽?ȥ

#	print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
#	pool.close()
#	pool.join()   #????join֮ǰ???ȵ???close??????????????????ִ????close?󲻻????µĽ??̼??뵽pool,join?????ȴ??????ӽ??̽???
#	print "Sub-process(es) done."



## http://stackoverflow.com/questions/5549190/is-shared-readonly-data-copied-to-different-processes-for-python-multiprocessing/5550156#5550156
#import multiprocessing
#import ctypes
#import numpy as np

##-- edited 2015-05-01: the assert check below checks the wrong thing
##   with recent versions of Numpy/multiprocessing. That no copy is made
##   is indicated by the fact that the program prints the output shown below.
### No copy was made
###assert shared_array.base.base is shared_array_base.get_obj()

#shared_array = None

#def init(shared_array_base):
#    global shared_array
#    shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
#    shared_array = shared_array.reshape(10, 10)

## Parallel processing
#def my_func(i):
#    shared_array[i, :] = i

#if __name__ == '__main__':
#    shared_array_base = multiprocessing.Array(ctypes.c_double, 10*10)

#    pool = multiprocessing.Pool(processes=4, initializer=init, initargs=(shared_array_base,))
#    pool.map(my_func, range(10))

#    shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
#    shared_array = shared_array.reshape(10, 10)
#    print shared_array


# http://stackoverflow.com/questions/5549190/is-shared-readonly-data-copied-to-different-processes-for-python-multiprocessing/5550156#5550156
import multiprocessing
import ctypes
import numpy as np

#-- edited 2015-05-01: the assert check below checks the wrong thing
#   with recent versions of Numpy/multiprocessing. That no copy is made
#   is indicated by the fact that the program prints the output shown below.
## No copy was made
##assert shared_array.base.base is shared_array_base.get_obj()

#lock = multiprocessing.Lock()

shared_array = None

a = np.array(range(0,10))

def init(shared_array_base, l):
    global shared_array
    shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
    shared_array = shared_array.reshape(10, 10)
    global lock #make your lock instance global in all the child workers
    lock = l

# Parallel processing
def my_func(i):
#    shared_array[i, :] = i * a[i]
	#for x in range(100000):
	#	shared_array[0, :] = i
	for x in range(10000):
		m = 0/1
		m = 0*1
		m = 0/1

	lock.acquire()
	for x in range(10000):
		shared_array[0, 0] = shared_array[0, 0] - i
		shared_array[0, 0] = shared_array[0, 0] + i
	lock.release()

if __name__ == '__main__':
    shared_array_base = multiprocessing.Array(ctypes.c_double, 10*10)
	#todo: share lock between process
    l_main = multiprocessing.Lock()
	#shared_value_base = multiprocessing.Value(multiprocessing.Lock, lock)
	

    pool = multiprocessing.Pool(processes=8, initializer=init, initargs=(shared_array_base,l_main,))
    pool.map(my_func, range(0,1000))

    shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
    shared_array = shared_array.reshape(10, 10)
    print shared_array