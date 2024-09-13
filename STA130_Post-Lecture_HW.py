#!/usr/bin/env python
# coding: utf-8

# In[1]:


#count: Count refers to the frequency of the occurence of a particular item in a dataset.
#mean: Mean is the average of data points.
#std: Standard deviation refers to a measure of the variation of the data points from the mean.
#min: This refers to the minimum or the smallest value in the data.
#25%: The 25th percentile refers to the value which 25% of the data falls under, also known as Q1.
#50%: The 50th percentile is the median, which is the middle value in the dataset.
#75%: The 75th percentile refers to the value which 75% of the data falls under, also known as Q3.
#max: This refers to the maximum or largest value in the data.


# In[2]:


#We use df.dropna() when we need to remove rows with missing data and retain the remaining columns for analysis, and use del df['col'] when we want to permanently remove a column from the DataFrame.


# In[3]:


#Example of where df.dropna() might be preferred over del df['col']: There's a DataFrame containing information about customers, including their age, income, and whether they’ve made a purchase. However, some records have missing values in one or more columns. If the goal is to remove rows where any data is missing, df.dropna() should be used to prevent an entire column from the DataFrame being deleted.


# In[4]:


#An opposite example would be: There is a DataFrame with customer feedback data, including columns for customer ID, feedback score, and comments. Some columns, like comments, might have a lot of missing values because not all customers leave comments. If the Comments column has many missing values, it's better to delete the entire column so that unimportant information won't be included in the data analysis.


# In[ ]:


#It is useful to apply del df['col'] before df.dropna() as it will make the process more efficient by reducing the number of columns that dropna() has to process, keep dropna() from affecting anything but relevant columns, and avoid accidentally losing good data. By deleting the columns you don't need upfront, you make the cleaning process go much smoother and keep the quality of your dataset on track with the most valuable information.

