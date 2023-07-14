#!/usr/bin/env python
# coding: utf-8

# ## Web scraping data from wikipedia using pandas and BeautifulSoup

# Following code scrapes data from the wikipedia page of Largest companies in the us based on revenue with url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# # step1
# 
# -> import the libraries Beautiful Soup(used to scrape information from webpage)  and requests(makes HTTP requests that makes it easy to send and recieve information  from websites providing a uniform interface)

# In[2]:


from bs4 import BeautifulSoup

import requests


# # step2
# 
# -> retrieve the data from a resource using .get() method.
# 
# -> print out the page to get a response to make sure the command is working prefferably 200.

# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[4]:


page= requests.get(url)


# In[5]:


print(page)


# # step3
# -> use BeautifulSoup to parse the page 
# 
# -> find the html tags associated with the table we want to extract using the inspect in the given url [.find('table')] 

# In[6]:


soup = BeautifulSoup(page.text,'html')


# In[7]:


soup.find('table')


# In[8]:


Table=soup.find_all('table')[1]


# # step 4
# -> find all 'th' tags (for the heading of the table)
# 
# -> use.strip() to remove the spaces and /n from the output 

# In[12]:


world_titles=Table.find_all('th')


# In[10]:


world_table_titles= [title.text.strip() for title in world_titles]
print(world_table_titles)


# # step 5
# -> import the pandas library
# 
# ->put the extracted column names into a dataframe

# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame(columns=world_table_titles)

df


# # step 6
# 
# -> find all the 'tr' tags which gives the row data 
# 
# -> start from the second row as the first row has no data 
# 
# -> find all 'td' which gives out the individual row data
# 
# -> insert all the individual data into the dataframe

# In[15]:


column_data=Table.find_all('tr')


# In[16]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length=len(df)
    df.loc[length]=individual_row_data


# In[17]:


df


# # step7
# 
# -> save the scraped data in a csv  file using df.to_csv(r'path')

# In[ ]:


df.to_csv(r'E:\python')


# In[ ]:




