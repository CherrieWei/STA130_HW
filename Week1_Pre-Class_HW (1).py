#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

url = 'https://storage.googleapis.com/kaggle-data-sets/235062/413420/compressed/Funny_Names.csv'
df = pd.read_csv(url)
print(df.head())


# In[2]:


import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())


# In[3]:


missing_values = df.isnull().sum()
print(missing_values)


# In[4]:


num_rows, num_columns = df.shape

print(f'Number of rows: {num_rows}')
print(f'Number of columns: {num_columns}')


# In[5]:


#Observations are the individual units that are being measured in a dataset and each observation can correspond to a set of data.
#In terms of my dataset, each observation would refer to the data of each passenger aboard Titanic.
#Variables are the types of information or characteristics that are being collected for each observation.
#In this case, the variables of the dataset include PassengerID, Name, Sex, and Age. 


# In[6]:


summary = df.describe(include='all')
print(summary)


# In[7]:


#When you call df.describe(), it provides summaries of statistics analysis for numeric columns only. If you have many columns, but some are non-numeric, they won't be included in this summary. To get a summary for categorical data, df.describe(include='all') need to be used, but the statistical summaries would be different from what’s given for numeric data.


# In[8]:


#With respect to the value it reports in the "count" column, the discrepancies occur because df.describe() only counts non-null values, while df.shape reflects the total dataset size regardless of missing values.


# In[9]:


#Attributes are used to store information about an object or class. Methods are functions and they determine the actions that should be performed on the object or class.


# In[ ]:


#ChatBot histories link: https://chatgpt.com/share/66e3b32c-4568-8003-ab07-5348d21c40ac
#Summary of Interactions
#Dataset Dimensions:

#Question: How to find the number of rows and columns in the Titanic dataset.
#Response: Provided a Python script using pandas to load the dataset and print the number of rows and columns using df.shape.
#Definitions of Observations and Variables:

#Observations: Individual units of data; in the Titanic dataset, each observation corresponds to a single passenger.
#Variables: Attributes or features recorded for each observation; in the Titanic dataset, these include PassengerId, Pclass, Name, Sex, Age, etc.
#Summarizing Columns in the Dataset:

#Question: How to provide simple summaries of columns in a dataset.
#Response: Suggested using df.describe(include='all') for a summary of all columns, including categorical ones, and df.info() for basic DataFrame structure and types.
#Explaining Discrepancies Between Dataset Size and Summary Statistics:

#Issue: Discrepancies between dataset size reported by df.shape and counts in df.describe().
#Explanation: Discrepancies are often due to missing values. df.describe() shows non-null counts, so columns with missing data will have counts less than the total number of rows.
#Attributes vs. Methods:

#Definition of Attributes: Variables that hold data or state about an object or class, accessed without parentheses.
#Definition of Methods: Functions that define behaviors or actions for an object or class, called with parentheses.

