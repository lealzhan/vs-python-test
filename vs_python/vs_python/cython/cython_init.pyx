##http://www.2cto.com/kf/201405/304168.html

#from cython.parallel import prange, parallel, threadid
#from libc.stdio cimport printf
 
#def Test():
#    cdef int i = 0
#    cdef int sum = 0
#    for i in prange(1000000, num_threads=2, nogil=True):  
#        printf ("%d\n", i)