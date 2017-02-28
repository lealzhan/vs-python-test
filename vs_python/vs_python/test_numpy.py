# http://old.sebug.net/paper/books/scipydoc/numpy_intro.html

import numpy as np



#array
a = np.array([1,2,3,4])
print a[0]
print a.shape

b = np.array([[1,2],
			  [3,4],
			  [5,6]])
print b

c = np.array((1,2))
print c

d = np.array(((1,2),
			  (3,4),
			  (5,6)))
print d

a = np.array([[1,2]])
print "a=",a[0],a[0][1]
print a.shape

a = np.array([[1,2],[3,4]],dtype=np.float)
print "a=",a
print a.shape

a = np.arange(0,1,0.2)
print "arange",a

a = np.linspace(0,1,12)
print "linspace",a

#print
print "%d %d"%(b.shape[0], b.shape[1])
print "hello my name is %s, I am %d years old" %("LING", 100)

#shape
print a.shape
print np.shape(b)

print "b ="
print b
b.shape = 2,3
print "b ="
print b

#reshape
a = np.array([[1,2],
	  [3,4],
	  [5,6]])
print "a = ",a,"hello",1,2,3

b = a.reshape((1,6))
print "after reshape"
print "a = ", a
print "b = ", b

a[1][0] = 0 #a,b share the same memory
print "a=",a
print "b=",b

#data type
print a.dtype


#2.1.2 data fetch
a = np.linspace(0,10,11)
print "a=",a
#a = np.array([[0,1],[2,3],[4,5],[6,7]])

b = a[0]
print "a[0]=",b
b = a[[0,1,-1]]
print "a[[0,1,-1]]=",b
b = a[np.array([True,False,True])]
print "a",b
#warning, should write in the belowing way
b = a[[True,False,True]] #=a[[1,0,1]]
print "a",b

#-----------
x = np.random.rand(10)
print x
print x>0.5
print x[x>0.5]


#-----colum or row major-------
a = np.array([[1,2],
			  [3,4],
			  [5,6]])
print a

a = a.swapaxes(1,0)
byte = a.tobytes()

print a

a = np.array([[0,1,2],[3,4,5],[6,7,8]], dtype=np.float32)
print a
