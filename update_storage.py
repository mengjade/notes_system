
# coding: utf-8

# In[47]:


import sqlite3
import pandas as pd
import numpy as np
import math
import xlwt
import time
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import warnings
warnings.filterwarnings("ignore")


con = sqlite3.connect('/home/peiying/notes_system/db.sqlite3')


# In[ ]:


con.execute("DELETE FROM food_storage");
con.commit()


# In[33]:


df = pd.read_excel(open("/home/peiying/Dropbox/Huiyi_Peiying/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "A:E",
                   sheetname='Food_Track',names=['cat','food_type','quant','unit','inputdate'],header=None)
df = df[1:]

today = time.strftime("%Y-%m-%d")

df['date_diff'] = df.inputdate.map(lambda x: (datetime.strptime(today, "%Y-%m-%d") - x).days)

# get exp map and merge
df1 = pd.read_excel(open("/home/peiying/Dropbox/Huiyi_Peiying/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "A:B",
                    sheetname='Expriation_Map',names=['food_type','days'],header=None)
df = pd.merge(df,df1,how = "outer")

# ok to store = 0 = nothing
df['exprie_flag'] = [0]*df.shape[0]
# two days before exp = 1 = suggested
df['exprie_flag'][((df.days - df.date_diff) <= 2)] = 1
# after exp = 2 = EAT NOW
df.exprie_flag[(df.days - df.date_diff) < 0 ] = 2

df.drop("inputdate", axis=1,inplace=True)
df.drop("days", axis=1,inplace=True)
df.drop("date_diff", axis=1,inplace=True)
df[["exprie_flag"]] = df[["exprie_flag"]].astype(int)
df[["exprie_flag"]] = df[["exprie_flag"]].astype(str)


# In[34]:


df1 = pd.read_excel(open("/home/peiying/Dropbox/Huiyi_Peiying/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "G:H",
                   sheetname='Food_Track',names=['cat','food_type'],header=None)
df1 = df1[1:]
df1 = df1.dropna()

# In[36]:

df = pd.concat([df,df1])
df = df.fillna(" ")
df = df[['cat','food_type','quant','unit','exprie_flag']]


def add_notes(df,con):

    data = df.values.tolist()
    
    i = 0
    for row in data:
        con.execute("INSERT INTO food_storage (cat, food_type, quant, unit, expire_flag)             VALUES ( '" + row[0] + "','" + row[1] + "','" +str(row[2]) + "','" + row[3] + "','" + str(row[4]) + "')")
        con.commit()
        


# In[38]:


add_notes(df,con)


# In[ ]:


# add planner 


# In[44]:


def add_notes(df,con):

    data = df.values.tolist()
    
    i = 0
    for row in data:
        con.execute("INSERT INTO food_planner (name, source, ing)         VALUES ( '" + row[0] + "','" + row[1] + "','" + row[2] + "')")        
        con.commit()
        


# In[ ]:


con.execute("DELETE FROM food_planner");
con.commit()


# In[45]:


df = pd.read_excel(open("/home/peiying/Dropbox/Huiyi_Peiying/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "L:N",
                   sheetname='Food_Track',names=['name','source','ing'],header=None)
df = df.dropna()


# In[46]:


add_notes(df,con)

