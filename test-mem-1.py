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


#settings to generate amount of number
num = 100000
#amount of number that will be generated
start = 10
#start number
end = 600
#end number


import numpy as np
# source : https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/
# Python 3 program to count frequencies 
# of array items
def countFreq(arr, n): 
    u =0
    a = []
    # Mark all array elements as not visited 
    visited = [False for i in range(n)] 
  
    # Traverse through array elements  
    # and count frequencies 
    for i in range(n): 
          
        # Skip this element if already  
        # processed 
        if (visited[i] == True): 
            continue
  
        # Count frequency 
        count = 1
        for j in range(i + 1, n, 1): 
            if (arr[i] == arr[j]): 
                visited[j] = True
                count += 1
          
        #print(arr[i], count) 
        a.append([arr[i],count])
        #arr_counter[i][0] = arr[i] 
        #arr_counter[i][1] = count
    a = np.array(a)
    return a

import memory_profiler
import time
angka = Rand(5000)
start_time = time.time()
m1 = memory_profiler.memory_usage()
countMe = countFreq(angka, len(list(angka)) ) 
countMe_sort = countMe[countMe[:,1].argsort()[::-1]]
m2 = memory_profiler.memory_usage()
mem_diff = m2[0] - m1[0]
#print(countMe_sort[:10])
print("Time : --- %s seconds ---" % (time.time() - start_time))
print("Memory Usage : --- %s MB ---" % (mem_diff))