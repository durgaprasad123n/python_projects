#!/usr/bin/env python
# coding: utf-8

# #### Importing important libraries

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as pe
import warnings
warnings.filterwarnings("ignore")


# #### Importing Dataset

# In[3]:


df1=pd.read_csv("product details.csv")
df1.head()


# In[4]:


df2=pd.read_csv("products catalog.csv")
df2.head()


# In[5]:


df1.info()


# In[6]:


df2.info()


# In[7]:


df1.describe()


# In[8]:


df2.describe()


# In[9]:


df1.shape


# In[10]:


df2.shape


# In[11]:


df2.rename(columns = {'ID':'ProductID'}, inplace = True)
df2.columns


# ### Merging Two Datasets

# In[12]:


df=pd.concat([df1, df2], axis=0)
df = pd.merge(df1, df2, on=["ProductID"])
df.head()


# In[13]:


df.shape


# In[14]:


df.isnull().sum()


# In[15]:


# removing spaces 
df['ProductName'].str.rstrip()
df['ProductBrand'].str.rstrip()
df['Gender'].str.rstrip()
df['Description'].str.rstrip()


# In[16]:


df_obj = df.select_dtypes(['object'])
df_obj.head()


# In[17]:


df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
df.head()


# In[18]:


df['ProductName'] = df['ProductName'].str.lstrip()
df['ProductBrand'] = df['ProductBrand'].str.lstrip()
df['Gender'] = df['Gender'].str.lstrip()
df['Description'] = df['Description'].str.lstrip()
df['PrimaryColor'] = df['PrimaryColor'].str.lstrip()
df.head(10)


# In[19]:


df = df.fillna(value = 'Others')


# In[20]:


df.isnull().sum()


# In[21]:


df.rename(columns = {'Price (INR)':'Price'}, inplace = True)
df.columns


# In[22]:


#distribution of variables
df.hist(bins=10,figsize= (10,10))


# In[23]:


sns.histplot(df['Price'],kde=True)


# In[24]:


sns.histplot(df['NumImages'],kde=True)


# ### Exploratory Data Analysis

# In[25]:


# Checking for Correlation between variables
plt.tick_params(labelsize=13)
sns.heatmap(df.corr(),annot=True)


# Here no any variable is highly correlated with other variables.

# In[26]:


df["PrimaryColor"] = df["PrimaryColor"].apply(lambda x : str(x).strip())
vc = df['PrimaryColor'].value_counts().to_frame().reset_index().head(25)

fig = pe.bar(x=list(vc['PrimaryColor'])[::-1], y=list(vc['index'])[::-1])
fig.update_layout(plot_bgcolor="#FFEBCD", title="Most Popular Colors", yaxis_title="Colors", xaxis_title="Counts")
fig.show()


# In[27]:


vc = df["Gender"].value_counts().reset_index()
fig = pe.pie(vc, values='Gender', names='index', title='Gender Distribution')
fig.show()


# In[28]:


fig = pe.pie(df, names='Gender', height=300, width=600, hole=0.7, title='Gender Overview',
                   color_discrete_sequence=['#4c78a8', '#72b7b2', '#6b92bc'])
fig.update_traces(hovertemplate=None, textinfo='percent+label', rotation=40)


# In[29]:


df["ProductBrand"] = df["ProductBrand"].apply(lambda x : str(x).strip())
vc = df['ProductBrand'].value_counts().reset_index().head(15)

fig = pe.bar(x=list(vc['ProductBrand'])[::-1], y=list(vc['index'])[::-1])
fig.update_layout(plot_bgcolor="#FFEBCD", title="Most Popular Brands", yaxis_title="Brands", xaxis_title="Counts")
fig.show()


# ### Univariate Analysis

# In[30]:


df['ProductName'].value_counts()


# In[31]:


df['ProductBrand'].value_counts()


# In[32]:


sns.countplot(df['Gender'])


# In[33]:


df.boxplot(column=['Price'], grid=False, color='black')


# In[34]:


df.hist(column='Price', grid=False, edgecolor='black')


# In[35]:


sns.kdeplot(df['Price'])


# In[36]:


g = sns.pairplot(df, diag_kind="kde")


# In[37]:


g = sns.PairGrid(df)
g = g.map_upper(sns.scatterplot)
g = g.map_lower(sns.kdeplot, colors="C0")
g = g.map_diag(sns.kdeplot, lw=2)


# In[38]:


df[['Price','NumImages']].corr()


# In[39]:


df.groupby(by='NumImages').agg('mean')[['Price']]


# In[40]:


plt.figure(figsize=(12,8))
sns.kdeplot(data=df,x='Price',hue='NumImages',fill=True)


# In[41]:


sns.countplot(data=df,x='NumImages',hue='Gender')


# In[42]:


pd.crosstab(df.Gender,df.NumImages,margins=True)


# In[43]:


all=pd.crosstab(df.Gender,df.NumImages,margins=True)['All']
pd.crosstab(df.Gender,df.NumImages).divide(all,axis=0).dropna()


# In[44]:


sns.pairplot(data=df[['Price','NumImages']])


# In[45]:


sns.pairplot(data=df[['Price','NumImages']],hue='NumImages')


# In[46]:


df = df.replace({'Boys':'Men', 'Girls':'Women','Unisex Kids':'Unisex'})


# In[47]:


df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




