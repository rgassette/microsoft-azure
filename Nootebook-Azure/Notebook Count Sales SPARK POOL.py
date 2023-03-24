#!/usr/bin/env python
# coding: utf-8

# ## Notebook Count Sales SPARK POOL
# 
# USE A SPARK POOL TO ANALYZE DATA
# 

# In[2]:


get_ipython().run_cell_magic('pyspark', '', "df = spark.read.load('abfss://files@datalaketmp5i79.dfs.core.windows.net/sales_data/sales.csv', format='csv'\r\n## If\u202fheader\u202fexists\u202funcomment\u202fline\u202fbelow\r\n, header=True\r\n)\r\ndisplay(df.limit(10))\n")


# In[3]:


df_counts = df.groupby(df.Category).count()
display(df_counts)

