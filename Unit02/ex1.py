# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:09:59 2022

@author: ASUS
"""
import matplotlib.pyplot as plt
days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "r-o")
plt.grid(True)
plt.show()