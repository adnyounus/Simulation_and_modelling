# -*- coding: utf-8 -*-
"""Monte_carlo_integral_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q4YLwKvdrjB2cfyLPoe6WZc6sOEUQb_n
"""

import random
import math
import matplotlib.pyplot as plt

n=[100, 1000, 5000, 10000]
error=[]

a=0
b=2

for trials in n:
  func_sum=0
  func_sqrd_sum=0
  for i in range (trials):
    x= random.uniform(a,b)
    func = (x**2)*(math.exp(x))*(math.log(x))
    func_sum= func_sum+func
    func_sqrd_sum = func_sqrd_sum+(func**2)

  func_average = func_sum/trials
  func_sqrd_average = func_sqrd_sum/trials

  integral_value = func_average*(b-a)
  error_value = ((b-a)/(math.sqrt(trials)))*(math.sqrt(func_sqrd_average-(func_average**2)))
  error.append(error_value)

  print(f"For number of points : {trials}")
  print(f"Integral value : {integral_value}")
  print(f"Error value : {error_value}")


x1=["100","1000","5000","10000"]
plt.bar(x1,error)
plt.ylabel("Error Values")
plt.xlabel("Values of N")
plt.show()