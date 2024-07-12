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

path = Path('.laborantum/texts/Homeworks/3. Matrices/11. Numpy Matrix Expression')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[21]:


import numpy as np
from scipy.linalg import expm

import numpy as np


def formula(A, B, C, x):
    I = np.eye(A.shape[1], B.shape[1])

    return np.exp(A.T @ (B + 2 * C) + 3 * I) @ x


# In[7]:


# In[22]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")


# In[ ]:




