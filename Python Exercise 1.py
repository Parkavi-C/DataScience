#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
For example: List = [54, 44, 27, 79, 91, 41]


# In[64]:


List = [54, 44, 27, 79, 91, 41]
List_cons = [54, 44, 27, 79, 91, 41]
print("Original list",List)
List_Var = List
List_Var.pop(4)
print("List After removing element at index 4",List_Var)
List_Var.insert(2,List_cons[4])
print("List after Adding element at index 2",List_Var)


# In[ ]:


Exercise Question 2: Given a two list of equal size create a list of unique elements from both the lists into a seperate list
    
First List  [2, 3, 4, 5, 6, 7, 8]
Second List  [4, 9, 16, 25, 36, 49, 64]
[64, 2, 3, 4, 5, 6, 7, 8, 9, 36, 16, 49, 25]


# In[34]:


List1 = [2, 3, 4, 5, 6, 7, 8]
List2 = [4, 9, 16, 25, 36, 49, 64]
List = List1+List2
print(list(set(List)))


# In[ ]:


Exercise Question 3: Remove duplicate from a list and create a tuple and find the minimum and maximum number (Hint: Try Functions Min() and Max() )
    
    Original list [87, 52, 44, 53, 54, 87, 52, 53]


# In[72]:


List =  [87, 52, 44, 53, 54, 87, 52, 53]
print("Original list ",List)
tuple = (87, 52, 44, 53, 54, 87, 52, 53)
unique_list = []
for x in List: 
        if x not in unique_list: 
         unique_list.append(x) 
print("unique list", unique_list)
print("tuple ",tuple)
print("Minimum number is: ",max(tuple))
print("Maximum number is: ",min(tuple))


# In[ ]:


Exercise Question 4: Display the each word in the string Count the number of words in a string and display it (Including the white spaces)
    
The sample string: Welcome to Python    


# In[42]:


a = "Welcome to Python"
print("Printing each words seperately: ",*a)
print("The Length of the string ",len(a))


# In[ ]:


Exercise Question 5: Write a Python program to access dictionary keys element by index. i.e. Use indexing methods to print the first key
The dictionary is:  {'physics': 80, 'math': 90, 'chemistry': 86}    


# In[52]:


Dic = {'physics': 80, 'math': 90, 'chemistry': 86}
print("The dictionary is:  ",Dic)
print("The key element accesed by index: ",list(Dic.keys())[0])

