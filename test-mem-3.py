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
# source : https://www.geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/
# Python3 program to implement basic operations  
# (search, insert and delete) on a BST that handles  
# duplicates by storing count with every node  
la=[]
# A utility function to create a new BST node  
class newNode:  
  
    # Constructor to create a new node  
    def __init__(self, data):  
        self.key = data 
        self.count = 1
        self.left = None
        self.right = None
  
# A utility function to do inorder  
# traversal of BST  

def inorder(root): 
    if root != None: 
        inorder(root.left) 
        #print(root.key,"(", root.count,")",  end = " ")
        la.append([root.key,root.count])
        inorder(root.right) 
  
# A utility function to insert a new node  
# with given key in BST 

def insert(node, key): 
      
    # If the tree is empty, return a new node  
    if node == None: 
        k = newNode(key) 
        return k 
  
    # If key already exists in BST, increment 
    # count and return  
    if key == node.key: 
        (node.count) += 1
        return node 
  
    # Otherwise, recur down the tree  
    if key < node.key:  
        node.left = insert(node.left, key)  
    else: 
        node.right = insert(node.right, key) 
  
    # return the (unchanged) node pointer  
    return node 
  
    return root 
  
import numpy as np
m1 = memory_profiler.memory_usage()
start_time = time.time()
angka = Rand(5000)
root = None

for n in angka:
    root = insert(root, n) 
    
#print("Inorder traversal of the given tree")  
inorder(root) 
la = np.array(la)
la_sort = la[la[:,1].argsort()[::-1]]
t2 = time.time()
m2 = memory_profiler.memory_usage()
mem_diff = m2[0] - m1[0]
print("Time : --- %s seconds ---" % (time.time() - start_time))
print("Memory Usage : --- %s MB ---" % (mem_diff))
