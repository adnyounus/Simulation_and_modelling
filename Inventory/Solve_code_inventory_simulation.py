# -*- coding: utf-8 -*-
"""011171018.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wWzD7iIGBK5M1xho8937KfVOXA2SAKsf
"""

import numpy as np
import random
import matplotlib.pyplot as plt  

m = int(input()) #Maximum capacity
n= int(input()) #review length

begining_inventory= 3
total_demand= 0
ending_inventory= 0
shortage_quantity= 0
order_quantity= 8  
days_until_order_arrives= 2
shortage_count=0
ending_inventory_array=[]
day_count_array=[]
day_count=0
ending_sum=0

for cycle in range(10):
  print("Cycle no: ",cycle)
  for day in range (1,n+1):
    print("Day no: ", day)

    ##order arrives code: begining_inventory= begining_inventory+ order_quantity    
    days_until_order_arrives=days_until_order_arrives-1
    if days_until_order_arrives == -1:
      begining_inventory= begining_inventory+ order_quantity

    daily_demand= np.random.choice(a=[0,1,2,3,4],p=[0.10,0.25,0.35,0.21,0.09])
    total_demand = daily_demand + shortage_quantity
    if total_demand> begining_inventory:
      shortage_quantity= total_demand-begining_inventory
      ending_inventory=0
      shortage_count+=1
    else:
      ending_inventory= begining_inventory-total_demand
    
    print("Begining Inventory: ",begining_inventory)
    print("Daily Demand: ",daily_demand)
    print("Ending Inventory: ",ending_inventory)
    print("Shortage Quantity: ",shortage_quantity)
    print("Days Until order : ",days_until_order_arrives)
    print("")

    begining_inventory=ending_inventory
    day_count=day_count+1
    ending_sum=ending_sum+ending_inventory
    ending_inventory_array.append(ending_inventory)
    day_count_array.append(day_count)




    ##Review code (Task-1)
    #when day==n: , then you have to place an order. order_quantity; days_until_order_arrives (randomly)
    if day==n:
      order_quantity= m-ending_inventory
      days_until_order_arrives=np.random.choice(a=[1,2,3],p=[0.6,0.3,0.1])
      print("Order has placed for quatity :",order_quantity)
      print("Lead time: ",days_until_order_arrives)
      print("")


#average_ending_inventory

average_ending_inventory=ending_sum/day_count
print("Average ending inventory: ",average_ending_inventory)

#number of days shortage occurs
print("Number of days with Shortage: ",shortage_count)

#ending inventory vs days graph:

plt.plot(day_count_array, ending_inventory_array)

plt.xlabel("Day number") 
plt.ylabel("Ending_inventory of each day")