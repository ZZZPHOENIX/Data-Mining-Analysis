# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:50:04 2018

@author: ZhangWP
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0, 5.0, 0.02)

plt.subplot(2,1,1)
plt.plot(a, f(a))

plt.subplot(2,1,2)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.savefig('img1', dip=800)
plt.show()