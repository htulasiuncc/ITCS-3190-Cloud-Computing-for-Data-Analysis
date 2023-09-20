#!/usr/bin/env python
# coding: utf-8

# # Configuring pandas

# ### Documentation - https://pandas.pydata.org/docs/reference/index.html

# In[73]:


# import numpy and pandas
import numpy as np
import pandas as pd
import csv as csv
# used for dates
import datetime
from datetime import datetime, date

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # The pandas Series
# #### A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type. Read the documentation and create a series that contains 4 items. After that finish the following given cells.

# In[74]:


# create a four item Series
seriesWithFourItems = pd.Series([1,2,3,4])


# In[75]:


# get value at label 1
seriesWithFourItems[1]


# In[76]:


# Write a snippet of code that will return a Series with the row with labels 1 and 3
seriesWithFourItems[[1,3]]


# In[77]:


# create the same series but this time using an explicit index
seriesWithFourItems = pd.Series(data = [5,6,7,8], index = [1,2,3,4])


# In[78]:


# look up items the series having index at first and index at last position
seriesWithFourItems[[1,4]]


# In[79]:


# get only the index of the Series
seriesWithFourItems.index


# In[80]:


# create a Series who's index is a series of dates
# https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
# between the two specified dates (inclusive)
# Dates: September 5, 2022 to September 11, 2022
dateSeries = pd.date_range('2022-09-05', '2022-09-11')
dateSeries


# In[81]:


# create a Series with values (representing temperatures) for each date in the index
# You can give them hardcoded values for now [80, 82, 85, 90, 83, 87, 80, 78]
# You can call this series clt_temp
clt_temp = pd.Series([80, 82, 85, 90, 83, 87, 80], index = dateSeries)


# In[82]:


# what's the temperation for September 9?
clt_temp['2022-09-09']


# In[83]:


# create a second series of values using the same index
# You can give them hardcoded values for now [70, 75, 69, 83, 79, 77, 74, 79]
# You can call this series nycTemp
nycTemp = pd.Series([70, 75, 69, 83, 79, 77, 74], index = dateSeries)


# In[84]:


# the series clt_temp and nyc_temp are aligned by their index values
# calculates the difference by those matching labels


# In[85]:


# Write the code to find the temperature difference on September 8?
clt_temp['2022-09-08']-nycTemp['2022-09-08']


# In[86]:


# Write code to find an average difference of temperature between the 2 cities?
tempAvg = (sum(clt_temp-nycTemp)/(len(clt_temp)))
tempAvg


# # The pandas DataFrame

# In[87]:


# create a DataFrame from the two series objects clt_temp and nyc_temp
# and give them column names
temps_df = pd.DataFrame(
    {'Charlotte': clt_temp, 
     'NYC': nycTemp})
temps_df


# In[88]:


# get the column with the name Charlotte
temps_df['Charlotte']


# In[89]:


# likewise we can get just the NYC column
temps_df['NYC']


# In[90]:


# return both columns in a different order
temps_df[['NYC', 'Charlotte']]


# In[91]:


# retrieve the Charlotte column through PROPERTY SYNTAX
temps_df.Charlotte


# In[92]:


# calculate the temperature difference between the two cities using the dataframe
temps_df.Charlotte - temps_df.NYC


# In[93]:


# add a column to temp_df which contains the difference in temps you can call the column Difference
temps_df['Difference'] = temps_df['Charlotte'] - temps_df['NYC']


# In[94]:


# get the columns of the dataframe, which is also an Index object
temps_df.iloc[0]


# In[95]:


# slice the temp differences column for the rows at 
# location 1 through 4 (as though it is an array)
temps_df['Difference'][1:5]


# In[96]:


# get the row at array position 1
temps_df.iloc[0]


# In[97]:


# the names of the columns have become the index
# they have been 'pivoted'


# In[98]:


# retrieve a random row of your choice by index label using .loc
temps_df.loc['2022-09-05']


# In[99]:


# get the values in the Differences column in tows 1, 3 and 5
# using 0-based location
temps_df.iloc[[1,3,5]].Difference


# In[100]:


# which values in the Missoula column are > 82?
temps_df.Charlotte >82


# In[101]:


# return the rows where the temps for Missoula > 82
temps_df[temps_df.Charlotte >82]


# # Loading data from a CSV file into a DataFrame

# In[102]:


# read the contents of the file activity3_0.csv into a DataFrame. Call the dataframe df
df = pd.read_csv('/Users/himat/Documents/UNCC/Fall 2022/ITCS 3190/activity3_0.csv')


# In[103]:


# Print the contents of the date column
df['Date']


# In[104]:


# Get the first value in the date column
df['Date'][0]


# In[105]:


# Write the code to get the type of the Date
df.dtypes['Date']


# In[106]:


# read the data and tell pandas the date column should be a date in the resulting DataFrame
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
df2 = pd.read_csv('/Users/himat/Documents/UNCC/Fall 2022/ITCS 3190/activity3_0.csv', parse_dates=['Date'])


# In[107]:


# verify the type now is date
# in pandas, this is actually a Timestamp
df2.dtypes


# In[108]:


# unfortunately the index is numeric which makes accessing data by date more complicated
# read in again, now specity the data column as being the index of the resulting DataFrame
df3 = pd.read_csv('/Users/himat/Documents/UNCC/Fall 2022/ITCS 3190/activity3_0.csv', parse_dates=['Date'], index_col='Date')


# In[109]:


# Verify that the index is now a DatetimeIndex by calling df.index
df3.index


# # Visualization

# In[110]:


# plots the values in the Close column
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
df3.plot('Close')


# # Thats it for today :D Good job!!!!
# 
# #### Submit this notebook on canvas and you will be graded for correctness. Make sure that you are not cutting corners or shortcuts 

# In[ ]:




