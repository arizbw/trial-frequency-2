#import library
import random
import time
import memory_profiler
from memory_profiler import profile
import time
#function to generate number

def Rand(num): 
    res = []
    for j in range(num): 
        res.append (random.randint(10, 600))
    return res


import numpy as np
# source : https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/
# Python 3 program to count frequencies 
# of array items 

#https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
start_time = time.time()
import numpy
def countFreq2(number): 
    frekuensi = {}
    i = 0
    for n in number:
        #print(n)
        if n in frekuensi:
            frekuensi[n] += 1
        else:
            frekuensi[n] = 1
        i+=1
    return frekuensi


m1 = memory_profiler.memory_usage()
t1 = time.time()
angka = Rand(5000)
result = countFreq2(angka)
sort_orders = sorted(result.items(), key=lambda x: x[1], reverse=True)[:10]
t2 = time.time()
m2 = memory_profiler.memory_usage()
mem_diff = m2[0] - m1[0]
#print(countMe_sort[:10])
print("Time : --- %s seconds ---" % (time.time() - start_time))
print("Memory Usage : --- %s MB ---" % (mem_diff))