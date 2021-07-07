#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as stats
import IPython as ip
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv(r"C:\Users\skhou\Downloads\US_Accidents_June20.csv (1).zip")


# In[3]:


# Convert object into real date time value

df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])


# In[4]:


# Creates new columns in df for each type based on the Start_Time
# which includes the date and time
# .dt.day is a pandas? file to convert data from dates into other forms
# originally in YYYY-MM-DD format, and weekday : Monday = "0"

df['day'] = df['Start_Time'].dt.day
df['weekday'] = df['Start_Time'].dt.weekday
df['hour'] = df['Start_Time'].dt.hour
df['month'] = df['Start_Time'].dt.month


# In[5]:


# Sort the values to make the bar graph look better
# Gives a matrix of the (columns of df)X(the elements of Weather_Condition)
# df.sort_values(by=['Brand'], inplace=True) : this gives ascending order
weather = df.groupby('Weather_Condition').count()
weather.sort_values(by=['ID'],inplace=True, ascending=False)
weather


# In[6]:


plt.figure(figsize=(30,10))
plt.title('Number of Accidents due to Weather Conditions')
plt.bar(weather.index, weather['ID'], color = 'r')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(weather.index, rotation='vertical', size=10)
plt.show()


# In[7]:


day = df.groupby('day').count()

plt.figure(figsize = (30,10))
plt.title('Number of Accidents per Day of the Month')
plt.bar(day.index, day.Number, color = 'b')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Accidents')
plt.xticks(day.index, rotation = 'vertical', size = 8)


# In[8]:


print('Day of the Month with the Most Accidents is : ',
      day.Number.idxmax())
day['Number'].sort_values(ascending=False)


# In[9]:


weekday = df.groupby('weekday').count()
weekday

#plt.figure(figsize=(30,10))
plt.title('Number of Accidents per day of the Week')
index = ["M","T","W","Th","F","S","Su"]
plt.bar(index, weekday.Number, color='g')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Accidents')
plt.xticks(weekday.index, size=8)
plt.show()


# In[10]:


hour = df.groupby('hour').count()
hour

#plt.figure(figsize=(30,10))
plt.title('Number of Accidents per Hour in the Day')
plt.bar(hour.index, hour.Number, color='g')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.xticks(hour.index, size=8)
plt.show()


# In[11]:


month = df.groupby('month').count()
month

plt.title('Number of Accidents per Month')
index = [6,7,8,9,10,11,12,1,2,3,4,5]
plt.bar(index, month.Number, color='r')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(month.index, size = 15)
plt.show()


# In[12]:


state = df.groupby('State').count()
state = state.sort_values(by = ['ID'], ascending=True)
state

plt.figure(figsize=(30,10))
plt.title('Number of Accidents per State')
plt.bar(state.index, state['ID'], color = 'g')
plt.xlabel(state.index)
plt.ylabel('Number of Accidents')
plt.xticks(state.index, size=50)

plt.show()


# In[13]:


states = df.State.unique()
severity_1_by_state = []
severity_2_by_state = []
severity_3_by_state = []
severity_4_by_state = []
for i in states:
    severity_1_by_state.append(df[(df['Severity']==1)&
                                  (df['State']==i)].count()['ID'])
    severity_2_by_state.append(df[(df['Severity']==2)&
                                  (df['State']==i)].count()['ID'])
    severity_3_by_state.append(df[(df['Severity']==3)&
                                  (df['State']==i)].count()['ID'])
    severity_4_by_state.append(df[(df['Severity']==4)&
                                  (df['State']==i)].count()['ID'])


# In[14]:


plt.figure(figsize=(20,15))

plt.bar(states, severity_2_by_state, label='Severity 2')
plt.bar(states, severity_3_by_state, label='Severity 3')
plt.bar(states, severity_4_by_state, label='Severity 4')
plt.bar(states, severity_1_by_state, label='Severity 1')


plt.legend()


# In[22]:


# weather being named this way gives us an .index that is the unique
# values and a .values column for the number of accidents in each case
weather = df.Weather_Condition.value_counts()

severity_1_by_weather = []
severity_2_by_weather = []
severity_3_by_weather = []
severity_4_by_weather = []
for i in weather.index:
    severity_1_by_weather.append(df[(df['Severity']==1)&
                                  (df['Weather_Conditon']==i)].count()['ID'])
    severity_2_by_weather.append(df[(df['Severity']==2)&
                                  (df['Weather_Conditon']==i)].count()['ID'])
    severity_3_by_weather.append(df[(df['Severity']==3)&
                                  (df['Weather_Conditon']==i)].count()['ID'])
    severity_4_by_weather.append(df[(df['Severity']==4)&
                                  (df['Weather_Conditon']==i)].count()['ID'])


# In[19]:




