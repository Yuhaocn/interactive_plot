#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df1 = pd.read_csv('data\human_development.csv')
df2 = pd.read_csv('data\inequality_adjusted.csv')
df = pd.merge(df1,df2,how="outer",on=['Country'])
df = df.rename(columns={'Human Development Index (HDI)_x':'Human Development Index (HDI)'})
df = df.dropna()
df = df.drop(['HDI Rank','IHDI Rank','Country','HDI Rank','Human Development Index (HDI)_y',
             'Inequality-adjusted HDI (IHDI)','IHDI Loss Percent','IHDI Rank Difference',
             'Inequality-Adjusted Life Expectancy Index','Inequality-Adjusted Education Index',
             'Inequality in Income','Income Inequality (Quintile Ratio)','Income Inequality (Palma Rati)',
             'Income Inequality (Gini Coefficient)'], axis=1)

df.head()


# In[7]:


df=df.replace(',','',regex=True)
df=df.replace('..','',regex=True)
df = df.apply(pd.to_numeric)
df.head()


# In[8]:


df_coor=df.corr()
df_coor.head()


# In[16]:


plt.subplots(figsize=(9,9))
plt.title('Distribution of HDI and IHDI factors', loc='left', fontsize=20)

fig=sns.heatmap(df_coor,vmin=0,annot=True, vmax=1, square=True, cmap="Blues")
fig


# In[ ]:




