#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[1]:


import numpy as np


# 2. Create a null vector of size 10 

# In[6]:


null_vector=np.zeros(10)


# 4. Find the shape of previous array in question 3

# In[ ]:


np.shape(arr)


# 5. Print the type of the previous array in question 3

# In[ ]:


arr.dtype


# 6. Print the numpy version and the configuration
# 

# In[4]:


np.__version__


# In[ ]:


np.show_config()


# 7. Print the dimension of the array in question 3
# 

# In[ ]:


arr.ndim


# 8. Create a boolean array with all the True values

# In[ ]:


np.ones(5, dtype=bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[ ]:


np.arange(10).reshape(2,5)


# 10. Create a three dimensional array
# 
# 

# In[4]:


np.arange(18).reshape((3,2,3))


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[ ]:





# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[4]:


a=np.zeros(10)
a[4]=1
print(a)


# 13. Create a 3x3 identity matrix

# In[ ]:


np.ones((3,3))


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[ ]:


np.float(arr)


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[6]:


arr1 = np.array([[1., 2., 3.],

            [4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],

           [7., 2., 12.]])
arr1*arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[ ]:


np.append(arr1,arr2)


# 17. Extract all odd numbers from arr with values(0-9)

# In[1]:


a=np.arange(10)
a[a%2==1]


# 18. Replace all odd numbers to -1 from previous array

# In[7]:


a[a%2==1]=-1


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[6]:


arr[5:9]=12


# 20. Create a 2d array with 1 on the border and 0 inside

# In[ ]:


b=np.ones((3,3))
b[1,1]=0


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[ ]:


arr2d[1,1]=12


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[ ]:


arr3d[0]=64


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[8]:


a=np.arange(10).reshape((2,5))
a[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[ ]:


a=np.arange(10).reshape((2,5))
a[1,1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[12]:


a=np.arange(9).reshape((3,3))
a[:,2]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[13]:


a=np.random.randn(10,10)
print(np.max(a))
print(np.min(a))


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[ ]:


np.intersect1d(a,b)


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[ ]:


c=[a==b]


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[14]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[names!="Will"]


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[16]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data[names!="Will"])
print(data[names!="Joe"])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[23]:


np.arange(1,16, dtype=float).reshape(5,3)


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[22]:


np.arange(1,17, dtype=float).reshape(2,2,4)


# 33. Swap axes of the array you created in Question 32

# In[24]:


a=np.arange(1,17, dtype=float).reshape(2,2,4)
np.swapaxes(a,1,2)


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[46]:


arr=np.arange(10)
a=np.sqrt(arr)
np.where(a<0.5,0,arr)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[48]:


x=np.random.randn(12)
y=np.random.randn(12)
np.maximum(x,y)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[49]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[52]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
c=np.setdiff1d(a,b)
c


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[59]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
sampleArray[2:]=([[10,10,10]])
sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[60]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[69]:


a=np.random.randint(20, size=(4,4))
np.cumsum(a)

