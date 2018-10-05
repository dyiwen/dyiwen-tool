# -*- coding:utf8 -*-
# !/usr/bin/env python


import matplotlib.pyplot as plt
import time
import numpy as np
import pylab

plt.ion()
x = np.linspace(0,50,1000)
plt.figure(1)
plt.plot(x,np.sin(x))
# plt.draw()
plt.show()
#time.sleep(5)
#plt.close(1)
# plt.figure(2)
# plt.plot(x,np.cos(x))
# plt.draw()
# time.sleep(5)
#print 'it is ok'