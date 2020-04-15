#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 

# In[3]:


get_ipython().system('pip install pandas')


# In[2]:


import numpy as np
import pandas as pd

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
index = ['a','b','c','d','e','f','g','h','i','j']

data = pd.DataFrame(exam_data,index) 
data


# In[1]:





# In[ ]:





# ## Exercise 2: Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
# ##### Use Data from previous problem

# In[2]:





# In[21]:



result = data[(data["score"]>15) & (data["attempts"]<2)]
print(result)


# ## Exerise 3: Change the value in row 'd' to 11.5
# ##### Use Data from previous questions

# In[3]:





# In[14]:


import numpy as np
import pandas as pd

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
index = ['a','b','c','d','e','f','g','h','i','j']

data = pd.DataFrame(exam_data,index) 
#data.iloc[3]
data.at['d','score'] = "11.5"
print(data)


# ## Exercise 4: Write a Pandas program to calculate the sum of the examination attempts by the students.
# data: d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

# In[4]:





# In[20]:


import numpy as np
import pandas as pd
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame\n",df)
r = input("Rows for colum1 value ==")
new = df["col1"].isin([r])
df[new]


# ## Exercise 5: Drop a list of rows from a specified DataFrame
# ###### data: 
# d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

# In[5]:





# In[32]:


import numpy as np
import pandas as pd
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame\n",df)
print("New DataFrame after removing 2nd & 4th rows:")
#new = df.drop([df.index[2],df.index[4]])
new = df.drop([2,4])
new


# ## Exercise 6:  Check whether a given column is present in a DataFrame or not
# ###### data: 
# d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

# In[6]:





# In[34]:


import numpy as np
import pandas as pd
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame\n",df)
ip = input(("Enter the column: "))
if ip in df.columns:
    print(ip,"is present in DataFrame.")
else:
    print(ip,"is not present in DataFrame.")


# ## Exercise 7: Get column index from column name of a given DataFrame
# 
# ###### data: 
# d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
# 
# ##### HINT: Try using a function called get_loc():
# Syntax: 
# dataframe.columns.get_loc()

# In[8]:





# In[40]:


import numpy as np
import pandas as pd
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame\n",df)
ip = input(("Index of "))
result = df.columns.get_loc(ip)
print(result)


# ## Exercise 8: Write a Pandas program to select all columns, except one given column in a DataFrame.
# ###### Use same data as previous problem

# In[9]:





# In[42]:


import numpy as np
import pandas as pd
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame\n",df)
ip = input(("All columns except"))
df.pop(ip)
df


# ## Exercise 9:  Write a Pandas program to remove last n rows of a given DataFrame.

# In[10]:





# In[45]:


import numpy as np
import pandas as pd
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame\n",df)
ip = int(input())
df.tail(ip)


# ## Exercise 10: Display the movies longer than 30 minutes and shorter than 360 minutes

# In[15]:





# In[63]:


import numpy as np
import pandas as pd
data = pd.read_csv("https://github.com/Laxminarayen/Inceptz-Batch13-Analytics_and_Python/raw/master/05%20-%20Day%205%20-%20Pandas%20with%20Exercises/IMDB-Movie-Data.csv")
df_all = pd.DataFrame(data)
df = df_all.loc[:,['Title','Runtime (Minutes)']]
new_data = df[(df["Runtime (Minutes)"]>30) & (df["Runtime (Minutes)"]<360) ]
print(new_data)

