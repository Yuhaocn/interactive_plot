#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import pandas as pd
import datetime
import numpy as np

from ipywidgets import widgets


# In[8]:


df = pd.read_csv('data\human_development.csv')

df.head()


# In[9]:


country = widgets.Dropdown(
    options=list(df['Country']),
    value='World',
    description='By Country:',
)


# In[10]:



g = go.FigureWidget(data=go.Splom(
                dimensions=[dict(label='HDI',
                                 values=df.loc[188:194,'Human Development Index (HDI)']),
                            dict(label='LEB',
                                 values=df.loc[188:194,'Life Expectancy at Birth']),
                            dict(label='EYE',
                                 values=df.loc[188:194,'Expected Years of Education']),
                            dict(label='MYE',
                                 values=df.loc[188:194,'Mean Years of Education'])],
                diagonal_visible=False, # remove plots on diagonal
                text=df.loc[188:194,'Country'],
                marker=dict(color=df.loc[188:194,'Country'].astype('category').cat.codes,
                            showscale=False, # colors encode categorical variables
                            line_color='white', line_width=0.5)
                ))



# In[11]:


def response(change):
    filter_list = [ i for i in
                           df['Country'] == country.value]
    a = df.loc[188:194]
    b = df[filter_list]
    temp_df = pd.concat([b,a])
    with g.batch_update():
        g.data[0].dimensions[0].values=temp_df['Human Development Index (HDI)']
        g.data[0].dimensions[1].values=temp_df['Life Expectancy at Birth']
        g.data[0].dimensions[2].values=temp_df['Expected Years of Education']
        g.data[0].dimensions[3].values=temp_df['Mean Years of Education']
        

    
country.observe(response, names="value")


# In[14]:


g.update_layout(
    title='Scatter plot matrix showing selected factors per country',
    width=600,
    height=600,
)

container = widgets.HBox([country])
a = widgets.VBox([container,
              g])

display(a)


# In[ ]:





# In[ ]:




