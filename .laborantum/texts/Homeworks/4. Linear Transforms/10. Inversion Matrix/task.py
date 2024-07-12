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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/10. Inversion Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[3]:


import numpy as np


def inversion(N):
    res = np.zeros([N, N])
    for index in range(N):
        res[index, N - index - 1] = 1
    return res


# In[4]:


import time

start = time.time()

debug_result = [inversion(**x) for x in debug_cases]
answer = [inversion(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")


# In[ ]:




