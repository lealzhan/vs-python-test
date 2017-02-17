print("Hello Python")

#import numpy as np
#x = np.arange(0,10)
#y = np.arange(0,10, 0.5)

from numpy import *
x = arange(0,10)
y = arange(0,10, 0.5)

m = range(0,10)
n = range(0,1,0.1)




# plot a sine wave from 0 to 4pi  
from pylab import *   
	#pylab 导入 各个库，创建类似matlab的环境。一次性导入各种库会造成命名空间污染？，所以应该避免使用ptlab
	#=
	#import numpy
	#import matplotlib
	#from matplotlib import pylab, mlab, pyplot
	#np = numpy
	#plt = pyplot
	#from IPython.display import display
	#from IPython.core.pylabtools import figsize, getfigs
	#from pylab import *
	#from numpy import *

x_values = arange(0.0, math.pi * 4, 0.01)  
y_values = sin(x_values)  
plot(x_values, y_values, linewidth=1.0)  
xlabel('x')  
ylabel('sin(x)')  
title('Simple plot')  
grid(True)  
savefig("sin.png")  
show()