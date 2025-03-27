#!/usr/bin/env python
# coding: utf-8

# In[60]:


def plot_bar_x(prices,time,cityname):
    # this is for plotting purpose
    index = np.arange(len(time))
    plt.bar(index,prices)
    plt.xlabel('Year', fontsize=15)
    plt.ylabel('Price per square feet', fontsize=5)
    plt.xticks(index, time, fontsize=5)
    plt.title(cityname)
    plt.figure(figsize=(4000, 3000))
    plt.show()


# In[61]:


import matplotlib.pyplot as plt
import numpy as np


# In[62]:


import pandas as pd

xls = pd.ExcelFile("HPI@Assessment Prices_Prices.xls")

sheetX = xls.parse(0) #0 is the sheet number

uniquecitynames= sheetX['City'].unique()
df=sheetX
#print(var1)
print(sheetX.groupby(['City']).groups.keys())

#x=list(sheetX.groupby(['City']).groups.values())
    


# In[63]:


for city in uniquecitynames:
    prices=df.loc[df['City'] == city]
    #print(prices['Composite Price'])
    pricevalues=prices['Composite Price']
    time=prices['Quarter']
    plot_bar_x(pricevalues,time,city)
    #print(time)


# In[64]:


#plot_bar_x(pricevalues,time)
#print(time)


# In[65]:


#print(pricevalues)


# In[ ]:





# In[ ]:




