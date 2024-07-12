#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/6. Change of basis")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[4]:


import numpy as np

def change_of_basis(B, x):
    return np.linalg.inv(B.T) @ x


# In[5]:


import time

start = time.time()

debug_result = [change_of_basis(**x) for x in debug_cases]
answer = [change_of_basis(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:





# In[ ]:




