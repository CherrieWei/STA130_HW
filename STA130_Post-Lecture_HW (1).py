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


# In[5]:


#It is useful to apply del df['col'] before df.dropna() as it will make the process more efficient by reducing the number of columns that dropna() has to process, keep dropna() from affecting anything but relevant columns, and avoid accidentally losing good data. By deleting the columns we don't need upfront, we make the cleaning process go much smoother and keep the quality of the dataset on track with the most valuable information.


# In[6]:


import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())


# In[7]:


missing_values = df.isnull().sum()
print(missing_values)


# In[9]:


del df['Cabin']


# In[10]:


del df['Age']


# In[11]:


df.dropna()


# In[12]:


#The majority of missing data is being removed using del df['col'] first. This is because by using missing_values = df.isnull().sum() to find the total number of missing values, it can be seen that the column 'Cabin' and 'Age' contains significant large number of missing values. Hence, it is better to remove these missing values first so that valuable data of a large number of passengers would not be removed if df.dropna() is applied


# In[13]:


#Since there are two more missing values in the column 'embarked', df.dropna() is used afterwards to remove all missing values.


# In[14]:


#ChatBot link: https://chatgpt.com/share/66e41d21-6824-8003-aad8-5e6fe96796e8
#Chatbot session summaries:
#Statistical Terms: We discussed the meanings of several statistical terms:

#Count: Refers to the number of occurrences of a particular item in a dataset.
#Std: Stands for standard deviation, which measures how spread out values are from the mean.
#Min: Represents the smallest value in a dataset.
#25% and 50%: These refer to percentiles; the 25th percentile is where 25% of data points fall below a certain value, while the 50th percentile is the median.
#Pandas Functions: We explored use cases involving df.dropna() and del df['col']:

#Use of df.dropna(): Preferred when removing rows with any missing values to ensure complete records are retained, particularly when all columns are important.
#Use of del df['col']: Preferred when an entire column with many missing values is irrelevant, so you can remove it and preserve the rest of the data.
#Combined Use: Deleting unnecessary columns with del df['col'] before using df.dropna() is beneficial because it improves efficiency, reduces the risk of accidentally deleting important rows, and focuses the data cleaning process on relevant columns.


# In[15]:


#When df.groupby("col1")["col2"].describe() is used, it would first group the dataset according to the values in the first column (col1). Then the method .describe() would be performed on the second column (col2), which statistical summaries of column 2 would be generated based on the grouped data.


# In[18]:


df.groupby("Ticket")["Fare"].describe()


# In[19]:


#For example, using the column 'Ticket' and 'Fare' from the titanic data set. The data is first grouped based on the values in the column 'Ticket', then data in the column 'Fare' is analyzed statistically (including count, meaning, std, min, 25%, 50%, 75%, max)


# In[20]:


#The values are different because the scope of missingness is different. df.describe() gives a comprehensive view of the missingness of each column for the whole dataset, while df.groupby("col1")["col2"].describe() provides a more detailed view of missingness within small subgroups.


# In[ ]:




