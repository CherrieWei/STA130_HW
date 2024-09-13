#!/usr/bin/env python
# coding: utf-8

# In[3]:


url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())


# In[2]:


#For this error, I think both chatbot and google search are easy to work with. They both provided direct and solution to the error without using a lot of difficult terminologies.


# In[6]:


import pandas as pd
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())


# In[5]:


#For this error, chatbot is easier to work it. Chatbot not only provided brief explanations for why the error occured but also the correct code, this is something that cannot be done by google search.


# In[7]:


DF.groupby("col1")["col2"].describe()


# In[8]:


#It's easier to work with chatbot with regard to this error. Chatbot can provide personalized information regarding the error i provided, but google search can only give me a general explanation about the error.


# In[9]:


url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
pd.read_csv(url
print(df.head())


# In[10]:


#It is easier to work with chatbot for this error since a lot of irrevelant information not related to the specific error i encountered popped out when i used google search, while chatbox just provided a very concise solution. 


# In[11]:


df.group_by("pclass")["age"].describe()


# In[12]:


#Both chatbot and google search work well for this error since both directly indicated that it should be groupby not group_by.


# In[14]:


df.groupby("Sex")["Age"].describe()


# In[15]:


#Chatbot is easier to work with for this error because it provided step-by-step explanations about how to resolve the error.


# In[16]:


df.groupby(sex)["age"].describe()


# In[17]:


#chatbox worked a lot better for this error than google search since could not provide me with explanations about this error in the context of my dataset, but chatbot can.


# In[18]:


#I can understand the majority of the materials, but there are still quite a few things that I am not very sure and will seek for further clarifications sometime.


# In[ ]:


#Chatbot link: https://chatgpt.com/share/66e42ae4-8fe8-8003-9da6-c8fcbc1c24e5
#Error with Pandas Library:

#Issue: Encountered a NameError because pd was not defined.
#Solution: Added import pandas as pd to import the Pandas library.
#HTTPError:

#Issue: Received an HTTPError 404: Not Found when trying to load data from an incorrect URL.
#Solution: Corrected the URL to https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv.
#SyntaxError:

#Issue: Faced a SyntaxError due to an unclosed parenthesis in pd.read_csv(url.
#Solution: Fixed the parentheses by correcting the code to df = pd.read_csv(url).
#AttributeError:

#Issue: Got an AttributeError for using group_by instead of groupby.
#Solution: Corrected the method to df.groupby("pclass")["age"].describe().
#NameError:

#Issue: Encountered NameError because titanic_df was not defined.
#Solution: Ensured the DataFrame variable was correctly defined and used.
#KeyError:

#Issue: Received KeyError because the column name 'Sex' did not exist in the DataFrame.
#Solution: Verified and corrected column names using print(df.columns) and adjusted the code accordingly.
#NameError with Column Names:

#Issue: Got NameError due to using column names without quotes.
#Solution: Corrected column names to be enclosed in quotes, e.g., df.groupby("Sex")["Age"].describe().

