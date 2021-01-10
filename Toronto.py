#!/usr/bin/env python
# coding: utf-8

# # <b><center>Segmenting and Clustering Neighborhoods in Toronto</b></center>

# <b>#Importing various libaries</b>

# In[1]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

get_ipython().system("conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab")
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

get_ipython().system('pip install folium')
import folium # map rendering library

print('Libraries imported.')


# <b>"We would be importing data from https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M, in order to obtain the data that is in the table of postal codes and to transform the data into a pandas  dataframe"</b>

# In[6]:


toronto_df=pd.read_excel(r'C:\Users\HP\Desktop\toronto.xlsx',header=None)
toronto_df.head()


# <b>"The dataframe will consist of three columns: PostalCode, Borough, and Neighborhood. So,we would be labeling the DataFrame with headers-  Postal Code , Borough and Neighborhood"</b>
# 

# In[13]:


header=["PostalCode","Borough","Neighborhood"]
toronto_df.columns=header
toronto_df.head()


# <b>"We would be only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned."</b>

# In[14]:


toronto_df.drop(toronto_df.loc[toronto_df['Borough']=='Not assigned'].index,inplace=True)
toronto_df.reset_index(drop=True, inplace=True)
toronto_df.head()


# <b>"We use the .shape method to print the number of rows of your dataframe"</b>

# In[17]:


toronto_df.shape


# In[ ]:




