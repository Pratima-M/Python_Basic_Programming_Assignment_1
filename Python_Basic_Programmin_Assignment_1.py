#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?

# In[1]:


print('Hello Python')


# 2.	Write a Python program to do arithmetical operations addition and division.?

# In[2]:


#Addition
a = int(input('Enter num1 = '))
b = int(input('Enter num2 = '))
a + b


# In[3]:


#Devision
a = int(input('Enter num1 = '))
b = int(input('Enter num2 = '))
a/b


# 3.	Write a Python program to find the area of a triangle?

# In[18]:


x = int(input('Len1 = '))
y = int(input('Len2 = '))
z = int(input('Len3 = ' ))
sp = (x+y+z)/2
Area = (sp*(sp-x)*(sp-y)*(sp-z))**0.5
print ('Area of triangle is', round(Area,3))


# 4.	Write a Python program to swap two variables?

# In[19]:


a = input('Enter num1 = ')
b = input('Enter num2 = ')
a,b = b,a
print ('Value of a after swapping', a)
print ('Value of b after swapping', b)


# In[ ]:




