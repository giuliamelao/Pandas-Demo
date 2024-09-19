#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#READING THE csv FILES, CHANGING THEIR IDS TO DESIRED COLUMN#

df = pd.read_csv('data/survey_results_public.csv', index_col='ResponseId')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='qname')


# In[29]:


#SETTING ALL COLUMNS VISIBLE#

pd.set_option('display.max_columns', 79)
pd.set_option('display.max_rows', 79)


# In[4]:


#df JUST SHOW THE COMPLETE DATAFRAME, FIRST 5 ROWS AND LAST 5 ROWS BY DEFAULT#

df


# In[5]:


#FUNCTION TO FIND HOW MANY DEVELOPERS PER LANGUAGE IN BRAZIL#
#You can search by calling the function and putting the desired language in second parameter#
#You may also change the country by changing the cntry variable

cntry = 'Brazil'

def qtdePorLing(country, ling):
    num = df.loc[df['Country']==country]['LanguageHaveWorkedWith'].str.contains(ling, na=False).sum()
    if len(ling) > 5: #simple conditional just to print a better table#
        print(ling,':\t',num)
    else:
        print(ling,':\t\t',num)
    
qtdePorLing(cntry,'Java')
qtdePorLing(cntry,'Python')
qtdePorLing(cntry,'JavaScript')
qtdePorLing(cntry,'HTML')
qtdePorLing(cntry,'C#')
qtdePorLing(cntry,'C')
qtdePorLing(cntry,'CSS')
qtdePorLing(cntry,'Shell')


# In[6]:


#TOP 10 COUNTRIES WITH MOST RESPONSES IN THE SURVEY, CONSEQUENTLY COUNTRIES WITH MOST DEVELOPERS#
df['Country'].value_counts().head(10)


# In[7]:


#CREATING A GROUPBY (by countries) TO ENHANCE THE SEARCH FOR DATA AND VALUES#
country_grp = df.groupby(['Country'])


# In[8]:


#THE 10 MOST COMMON SALARIES OF BRAZILIAN DEVELOPERS IN USD PER YEAR#

country_grp['CompTotal'].value_counts().loc['Brazil'].head(10)


# In[9]:


df['Gender'].value_counts()


# In[10]:


country_grp['Gender'].value_counts().loc['Brazil'].head(5)


# In[13]:


comp_grp = df.groupby(['CompTotal'])


# In[28]:


#comp_grp['Country'].value_counts().loc[CompTotal>=70000]   #df['CompTotal']>70000]


# In[ ]:




