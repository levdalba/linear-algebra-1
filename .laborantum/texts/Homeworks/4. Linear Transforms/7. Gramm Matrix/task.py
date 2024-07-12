#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/7. Gramm Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[3]:


import numpy as np

def contra_to_co(B, x):
    G = B @ B.T
    return G @ x


# In[4]:


import time

start = time.time()

debug_result = [contra_to_co(**x) for x in debug_cases]
answer = [contra_to_co(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:





# In[ ]:




