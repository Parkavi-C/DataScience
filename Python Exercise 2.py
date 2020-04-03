#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700(both included)


# In[20]:


List = []
for x in range(1500,2700,1):
    if(x%5 == 0 and x%7==0):
        List.append(x)
print(*List, sep=", ")



# In[ ]:


###Write a Python program to construct the following pattern, using a nested for loop.


# In[12]:


a = int (input())
for x in range (1,a+1):
    for y in range (1,x+1):
        print("*",end=" ")       
    print("\r")
    
for x in range (a,0,-1):
    for y in range(0,x-1):
        print("*",end=" ")
    print("\r")


# In[ ]:


###Write a Python program to count the number of even and odd numbers from a series of numbers.


# In[ ]:


x = int (input())
y = int (input())
even = 0
odd = 0
for i in range(x,y+1):
    if(i%2 == 0):
        even += 1
    else:
            odd += 1
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)


# In[ ]:


###Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.


# In[9]:


a=[]
for x in range(100,401):
    s = str(x)
    if(int(s[0])%2 == 0 and int(s[1])%2 == 0 and int(s[2])%2 == 0):
        a.append(x)
        
print(*a,sep=", ") 
        


# In[ ]:


### Write a Python program to calculate a dog's age in dog's years. Go to the editor
### Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.


# In[4]:


age = int(input("Input a dog's age in human years: "))
cal_age = 0
if(age > 2):
    cal_age = ((age-2)*4) + (2*10.5)
elif(age<=2):
    cal_age = age*10.5
print("The dog's age in dog's years is ",cal_age)


# In[ ]:


###Write a Python function to find the Max of three numbers.


# In[7]:


a = []
for x in range(0,3):
       a.append(input())
def max_function(a):
   print("The Three numbers are: ",tuple(a))
   print(max(a))
max_function(a)  



# In[ ]:


###Write a Python function that takes a number as a parameter and check the number is prime or not.


# In[16]:


num = int(input("The number is: "))

def prime_function(a):
    if(a > 1):
        for x in range(2,a):
            if(a%x == 0):
                print("False")
                break;
        else:
            print("True")
prime_function(num)


# In[ ]:


###Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor


# In[21]:



input_str = input("Original String : ")
def case_calculator(s):
    upper = 0
    lower = 0
    for x in s:
        if(x.isupper()):
            upper += 1
        elif(x.islower()):
            lower += 1
    print("No. of Upper case characters : ",upper)
    print("No. of Lower case Characters : ",lower)

case_calculator(input_str)


# In[ ]:


###Write a Python program to reverse a string.


# In[29]:


def reverse(s):
    return "".join(reversed(s))
input_str = input("The original string is: ")
print("The reversed string: ",reverse(input_str))


# In[ ]:


###Write a Python program to find the greatest common divisor (gcd) of two integers.


# In[36]:


def gcd(x,y):
    List = []
    small = 0
    if(x>y):
        small = y
    else:
        small = x
    for i in range(1,small+1):
        if(x%i == 0 and y%i == 0):
            List.append(i)
    return max(List)
a = int (input())
b = int (input())
print("The two numbers are:",a,",",b)
print("The GCD of the numbers are:",gcd(a,b))

