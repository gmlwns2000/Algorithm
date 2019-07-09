#!/usr/bin/env python
# coding: utf-8

# In[8]:


import util
import sys
import time


# In[9]:


def getInput():
    pass


# In[10]:


def algorithm(stdin):
    pass


# In[17]:


if __name__ == "__main__":
    util.algo_start()
    stdin = getInput()
    algorithm(stdin)
    util.algo_end()


# In[5]:


if __name__ == "__main__" and util.in_notebook():
    get_ipython().system('ipython nbconvert --to python main.ipynb')

