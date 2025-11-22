#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IMPORT ESSENTIAL LIBRIES FOR DATA ANAYSIS,ML,DL AND CAS

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
import openpyxl



# In[2]:


# LOAD PROJECT DATASET IN EXCEL FORMAT
df = pd.read_excel("superstore.xlsx")


# In[3]:


# LOAD THE FIRST 10 ROWS OF PROJECT DATASET
print(df.head(6))


# In[7]:


#title of dashboard
st.set_page_config(page_title="STATCAP SALES DASHBOARD", layout="wide")
st.title("STATCAP SALES DASHOBARD")

df = pd.read_excel("superstore.xlsx")

#total sales
total_sales = df['sales'].sum()
st.header("summary metrics")
st.metric(label="total sales",value=f"$ {total_sales:,.2f}")
#total profit
total_profit=df['profit'].sum()
st.metric(label="total profit", value = f"$ {total_profit:,.2f}")
#prepare counts

cat_counts = df['category'].value_counts().reset_index()
cat_counts.columns = ['category', 'count']

segment_counts = df.groupby(['category', 'segment']).size().reset_index(name='count')

#plot
#bar
bar_fig = px.bar(
    cat_counts,
    x="category",
    y="count",
    text="count",
    title="bar chart:category counts"
)
#stacked
stack_fig = px.bar(
    segment_counts,
    x='category',
    y='count',
    color="segment",
    title="stacked bar chart: segemnt by category(counts)"
)
#donut

donut_fig = px.pie(
    cat_counts,
    names="category",
    values="count",
    hole=0.5,
    title="donut chart:category distribution(counts)"
)

st.plotly_chart(bar_fig,use_container_width=True)
st.plotly_chart(stack_fig,use_container_width=True)
st.plotly_chart(donut_fig,use_container_width=True)


# In[8]:


df.to_excel("superstore.xlsx", index=False)


# In[ ]:




