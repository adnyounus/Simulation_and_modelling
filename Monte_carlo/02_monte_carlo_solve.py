# -*- coding: utf-8 -*-
"""02. monte_carlo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jp-bFURYbkT9OfFFMG3X8V1EE1dVSSIv
"""

import random
import math
import matplotlib.pyplot as plt

n=[100, 1000, 5000, 10000]

area_triangle = []

miss_theta = []
miss_D = []
hit_theta = []
hit_D = []

for trials in n:
  hits=0
  for i in range(trials):
     x= random.uniform(0,3)
     y= random.uniform(0,5)
     if y<=x+2:
       hits=hits+1
       hit_theta.append(x)
       hit_D.append(y)
     else:
       miss_theta.append(x)
       miss_D.append(y)   



  A= 15* (hits/trials)
  area_triangle.append(A)
  

  print(f"For trial : {trials}")

  print(f"Area of triangle: {A}")
  print("Scatter Plot :")
  plt.scatter(miss_theta,miss_D,c='green', label="miss points")
  plt.scatter(hit_theta,hit_D,c='red', label="hit points")
  plt.legend()
  plt.show()