#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import pandas as pd
import datetime
import numpy as np

from ipywidgets import widgets


# In[2]:


df1 = pd.read_csv('data\human_development.csv')
df2 = pd.read_csv('data\inequality_adjusted.csv')
df = pd.merge(df1,df2,how="outer",on=['Country'])
df = df.rename(columns={'HDI Rank_x':'HDI Rank','Human Development Index (HDI)_x':'Human Development Index (HDI)'})
df = df.dropna()
df.head()


# In[11]:


data = widgets.Dropdown(
    options=list(['HDI Rank','Human Development Index (HDI)','Coefficient of Human Inequality',
                  'Inequality in Life Expectancy','Inequality-Adjusted Life Expectancy Index',
                  'Inequality in Education','Inequality-Adjusted Education Index',
                  'Inequality-Adjusted Education Index','Income Inequality (Gini Coefficient)',
                 'Expected Years of Education','Mean Years of Education','GNI per Capita Rank Minus HDI Rank']),
    value='HDI Rank',
    description='By data:',
)


# In[12]:


g = go.FigureWidget(data= go.Choropleth(
    locations=df['Country'], # Spatial coordinates
    z = df['HDI Rank'], # Data to be color-coded
    locationmode = 'country names', # set of locations match entries in `locations`,
))


# In[13]:


def response(change):
    x=data.value
    temp_df = df[x]
    with g.batch_update():
        g.data[0].z = df[x]

data.observe(response, names="value")


# In[15]:


g.update_layout(
    title='Selected HDI and IHDI factors by country',
    width=600,
    height=600,
)

container = widgets.HBox([data])
a = widgets.VBox([container,
              g])

display(a)


# In[ ]:




