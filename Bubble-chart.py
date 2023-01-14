#!/usr/bin/env python
# coding: utf-8

# In[34]:


import dash
import dash_core_components as dcc
from dash import html
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


# In[35]:


df = pd.read_csv('data\human_development.csv')
df.head()


# In[43]:


def main():

                app = dash.Dash(__name__)
                fig = px.scatter(df, x="GNI per Capita Rank Minus HDI Rank", y="Life Expectancy at Birth", title="3D Distribution of countries by the 3 HDI factors",
                 size="Human Development Index (HDI)", color="Expected Years of Education", hover_name="Country",
                 log_x=True, size_max=10)
            
                fig.show()

                app.layout = html.Div([
                dcc.Graph(id='life-exp-vs-gdp',figure=fig)
])

if __name__ == '__main__':
    main()


# In[ ]:




