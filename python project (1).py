#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_excel(r"C:\Users\vvign\OneDrive\Documents\excel\BlinkIT Grocery Data - Copy.xlsx")


# In[4]:


df.tail(10)


# In[5]:


df.head(10)


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


print(df['Item Fat Content'].unique())


# In[11]:


df["Item Fat Content"]=df["Item Fat Content"].replace({"low fat":"Low Fat",
                                                       "LF":"Low Fat",
                                                       "reg":"Regular"})
df


# In[12]:


print(df['Item Fat Content'].unique())


# In[13]:


df.fillna(0,inplace=True)
df


# In[14]:


df.drop_duplicates(inplace=True)
df.head(40)


# In[15]:


df["Sales"] = df["Sales"].round(2)
df.tail(30)


# In[16]:


df['Item Visibility'] = df['Item Visibility'].round(2)
df


# In[17]:


df['Rating']=df['Rating'].astype(int)
df.tail(40)


# In[18]:


total_sales=df['Sales'].sum()
print("Total Sales:", total_sales)
total_average=df['Sales'].mean().round(3)
print("Total Average:",total_average)
total_sold=df['Sales'].count()
print("Total Sold:",total_sold)
average_rating=df['Rating'].mean().astype(int)
print("Total Average rating:",average_rating)


# In[19]:


print(df['Item Type'].unique())


# In[20]:


df['Item Type'].value_counts()


# In[21]:


df.sort_values(by='Outlet Establishment Year', ascending=True).head(50)


# In[22]:


df.head(50)


# In[23]:


sns.barplot(x='Item Type', y='Sales',color='gray', data=df)
plt.xticks(rotation=90)
plt.title('Sales by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Sales')
plt.show()


# In[24]:


plt.figure(figsize=(12,10))
df['Item Type'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Item Type Distribution')
plt.ylabel('')
plt.show()


# In[25]:


plt.figure()
plt.hist(df['Sales'], bins=20, color='skyblue', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()


# In[26]:


plt.figure()
sns.scatterplot(x='Item Weight', y='Sales',color='brown', data=df)
plt.title('Item Weight vs Sales')
plt.xlabel('Item Weight')
plt.ylabel('Sales')
plt.show()


# In[32]:


grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum()

grouped.unstack().plot(kind='bar',color='kg')

plt.title('Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.show()


# In[29]:


sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize=(12,10))
plt.plot(sales_by_year.index, sales_by_year.values, color='k', marker='o')

plt.title('Outlet Establishment Year vs Total Sales')
plt.xlabel('Year')
plt.ylabel('Total Sales')

# value show panna
for x, y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x, y, y, ha='center', color='g', va='bottom')

plt.show()


# In[ ]:


df.to_excel(
    r"C:\Users\vvign\OneDrive\Documents\excel\BlinkIT_Output.xlsx",
    index=False
)

print("File Saved Successfully")


# In[ ]:




