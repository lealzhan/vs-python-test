## -*- coding: utf-8 -*-
#import numpy as np
#import matplotlib.pyplot as plt


#a = np.array([[1,2,3],
#			  [4,5,6],
#			  [7,8,9]])
#print a

#b[:,:,0] = a
#b[:,:,1] = a+1
#b[:,:,2] = a+2



#x = np.linspace(0, 10, 1000)
#y = np.sin(x)
#z = np.cos(x**2)

#plt.figure(figsize=(8,4))
#plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
#plt.plot(x,z,"b--",label="$cos(x^2)$")
#plt.xlabel("Time(s)")
#plt.ylabel("Volt")
#plt.title("PyPlot First Example")
#plt.ylim(-1.2,1.2)
#plt.legend()
#plt.show()


# -*- coding: utf-8 -*-
"""
http://blog.csdn.net/Eddy_zheng/article/details/48713449
Created on Thu Sep 24 16:37:21 2015

@author: Eddy_zheng
"""

import scipy.io as sio  
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

mat1 = '4a.mat'
data = sio.loadmat(mat1)
m = data['data']

x,y,z = m[0],m[1],m[2]
ax=plt.subplot(111,projection='3d')

#ax.scatter(x[:1000],y[:1000],z[:1000],c='y')
#ax.scatter(x[1000:4000],y[1000:4000],z[1000:4000],c='r')
#ax.scatter(x[4000:],y[4000:],z[4000:],c='g')

#z.fill(0)

color = ['r','g','b']
for i in range(3000,6000):
    ax.scatter(x[i],y[i],z[i],c=color[i%3])

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()