#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np
a=np.arange(10)
a.reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[3]:


a=np.arange(10).reshape(2,5)
b=np.ones(10, dtype=int).reshape(2,5)
np.vstack((a,b))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[4]:


a=np.arange(10).reshape(2,5)
b=np.ones(10, dtype=int).reshape(2,5)
np.hstack((a,b))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[5]:


arr=np.arange(10).reshape(2,5)
arr.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[10]:


a=np.arange(15).reshape(1,3,5)
a.flatten()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[7]:


a=np.arange(15)
a.reshape(1,5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[12]:


a=np.arange(25).reshape(5,5)
np.square(a)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[13]:


a=np.arange(30).reshape(5,6)
a.mean()


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[14]:


a=np.arange(30).reshape(5,6)
a.std()


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[16]:


a=np.arange(30).reshape(5,6)
np.median(a)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[17]:


a=np.arange(30).reshape(5,6)
np.transpose(a)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[20]:


a=np.arange(16).reshape(4,4)
np.trace(a)


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[22]:


a=np.arange(16).reshape(4,4)
np.linalg.det(a)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[23]:


a=np.arange(100)
np.percentile(a,5)
np.percentile(a,95)


# ## Question:15

# ### How to find if a given array has any null values?

# In[41]:


a=np.ones(12).reshape(3,4)
b=np.sum(a)
np.isnan(b)

