#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1: NumPy: Create an array with values ranging from 12 to 38

# In[2]:


import numpy as np


# In[9]:


numpy_array = np.array([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38])
print(numpy_array)


# # Using arange()

# In[22]:


i = int(input())
j = int(input())
x= np.arange(i,j+1)
print(x)


# ## Exercise 2: Add a border around an existing array
# ##### Hint: np.pad()

# In[53]:


x = np.ones([3,3])
print("Original array:\n",x)
x = np.pad(x,((1,2),(2,1)),mode='constant',constant_values='5')
print("0 on the border and 1 inside in the array\n",x)


# In[54]:


x = np.ones([3,3])
print("Original array:\n",x)
x = np.pad(x,pad_width= 1,mode='constant')
print("0 on the border and 1 inside in the array\n",x)


# ## Exercise 3: Convert a list and tuple into arrays

# In[58]:


List = [1, 2, 3 ,4, 5, 6, 7 ,8]
print("List to array:\n",np.asarray(List))
tuple = ((8, 4, 6),(1, 2 ,3))
print("Tuple to array:\n",np.asarray(tuple))


# In[6]:





# ## Also try np.asarray for the problem above! 

# ## Exercise 4:  Convert the values of Centigrade degrees into Fahrenheit degrees

# In[12]:


x = [0.,   12.,   45.21, 34.,   99.91]
print("Values in Fahrenheit degrees:\n",x)
c=[]
for i in  x  :
    c.append(round(((i-32)*5/9),8))
print("Values in  Centigrade degrees:\n",c)
    


# In[4]:





# ## Exercise 5: Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements. 

# In[ ]:


import numpy as np
s = int(input())
x = []
for i in range (s):
    x.append(int(input(i)))
a = np.asarray(x)
print("Size of the array:",len(a))
print("Length of one array element in bytes:",a.itemsize)
print("Total bytes consumed by the elements of the array:",a.nbytes)


# In[7]:





# ## Exercise 6: Get the unique elements of an array

# In[9]:





# In[13]:


import numpy as np

x = int(input("Enter the number of rows:"))
y= int(input("Enter the number of columns:"))
matrix = []
unique_list = []
for i in range (x):
    a = []
    for j in range (y):
        ip = int(input())
        a.append(ip)
        unique_list.append(ip)
    if(x>1):
        matrix.append(a)
    elif(x==1):
        matrix = a
    
print("Original array:\n",matrix)
print("Unique elements of the above array:\n",np.unique(unique_list))     


# # Exercise 7: Change the dimension of an array
# 

# In[11]:





# In[5]:



import numpy as np
list_size = int(input("Enter the list size: "))
a = []
for i in range (list_size):
    a.append(int(input()))
print("Original array:\n",a)
print(np.array(a).reshape(int(input("Change array shape to rows: ")),int(input("columns: "))))


# ##### Exercise 8: Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive

# In[12]:





# In[7]:


import numpy as np
a = np.linspace(2.5,6.5,30)
print(a)


# ## Exercise 9: Convert 1-D arrays as columns into a 2-D array

# In[2]:


import numpy as np
s = int(input("Array Size: "))
a1 = []
a2 = []
for i in range (s):
    a1.append(int(input()))
a = np.array(a1)
for i in range (s):
    a2.append(int(input())) 
b = np.array(a2)
print("Array1: ",a)
print("Array2: ",b)
print("Converted array \n", np.stack((a,b),axis=1))


# # Exercise 10: Create a 5x5 matrix with row values ranging from 0 to 4

# In[22]:





# In[5]:


import numpy as np

a = np.zeros([5,5])
print("Original array:\n",a)
a[:,:] = range(0,5)
print("Row values ranging from 0 to 4 \n",a)


# ## Exercise 11: Sum of all the multiples of 3 or 5 below 100

# In[23]:





# In[11]:


import numpy as np

a = []
sum =0
for i in range (1,100):
    if(i%3 ==0 or i%5 ==0):
        a.append(i)
        sum += i
print(a)
print(sum)


# ## Exercise 12: Combine a one and a two dimensional array together and display their elements
# ##### Hint : np.nditer()

# In[28]:


x = np.arange(4)
y = np.arange(4)
for a, b in np.nditer([x,y]):
    print(a)
    print(b)


# In[29]:





# In[6]:


import numpy as np

x = np.arange(4)
y = np.arange(8).reshape(2,4)
for i,j in np.nditer([x,y]):
    print(i,":",j)


# ## Exercise 13: Write a NumPy program to replace all elements of NumPy array that are greater than specified array.

# In[30]:





# In[15]:


import numpy as np
new_a = []
a = np.array([[0.42436315, 0.48558583, 0.32924763],
 [0.7439979,  0.58220701, 0.38213418],
 [0.5097581,  0.34528799, 0.1563123 ]])
new_a = np.where(a<0.5 , a, 0.5)
print("Original array:\n",a)
print("Replace all elements of the said array with .5 which are greater than .5\n",new_a)


# In[ ]:





# ## Exercise 14: Add a new row to an empty numpy array

# In[34]:





# In[25]:


import numpy as np
a = np.array([])
print("Empty array:\n",a)
a = np.append(a,[[10, 20, 30],[40, 50, 60]])


print("After adding two new arrays:\n",a)


# ## Exercise 15: Write a NumPy program to join a sequence of arrays along a new axis. 

# In[35]:





# In[1]:


import numpy as np
r = int(input("no.of rows"))
c = int(input("no.of columns"))
matrix1 = []
matrix2 = []
for i in range(r):
    matrix1 += [0]
for i in range(r):
    matrix1 [i] = [0]*c
for i in range(r):
    for j in range(c):
        matrix1 [i][j] = int(input())
     
    
for i in range(r):
    matrix2 += [0]
for i in range(r):
    matrix2[i] = [0]*c
for i in range(r):
    for j in range(c):
        matrix2[i][j] = int(input())
    

print("Original arrays: \n",matrix1)
print(matrix2)
print("Sequence of arrays along a new axis:\n",np.vstack((matrix1,matrix2)))


# In[ ]:





# In[ ]:




