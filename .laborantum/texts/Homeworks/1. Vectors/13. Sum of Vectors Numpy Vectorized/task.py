#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

get_ipython().system('{sys.executable} -m pip -q install --user numpy json-tricks torch jupyter nbconvert')


# In[2]:


import json_tricks

path = Path(
    ".laborantum/texts/Homeworks/1. Vectors/13. Sum of Vectors Numpy Vectorized"
)


# In[3]:


debug_cases = json_tricks.load(str(path / "testcases" / "debug_cases.json"))
public_cases = json_tricks.load(str(path / "testcases" / "public_cases.json"))


# In[4]:


import numpy as np


def vector_sum(x, y):
    ## YOUR CODE HERE
    return x + y


# In[5]:


import time

start = time.time()

debug_result = [vector_sum(**x) for x in debug_cases]
answer = [vector_sum(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")

