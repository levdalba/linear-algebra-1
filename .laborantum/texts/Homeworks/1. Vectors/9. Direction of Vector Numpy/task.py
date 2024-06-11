#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[5]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/1. Vectors/9. Direction of Vector Numpy')


# In[6]:


debug_cases = json_tricks.load(str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(str(path / 'testcases' / 'public_cases.json'))


# In[1]:


import numpy as np
import numpy.typing as npt

def vector_direction(x):
    y = x.copy()
    length = np.linalg.norm(y)
    ans = y / length
    return ans


# In[8]:


import time

start = time.time()

debug_result = [vector_direction(**x) for x in debug_cases]
answer = [vector_direction(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

