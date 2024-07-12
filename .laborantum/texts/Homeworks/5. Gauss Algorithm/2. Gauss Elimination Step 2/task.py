#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[9]:


from gauss_elimination_2 import gauss_elimination_2
import numpy as np


# In[10]:


import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/2. Gauss Elimination Step 2')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[11]:


import time

start = time.time()

debug_result = [gauss_elimination_2(**x) for x in debug_cases]
answer = [gauss_elimination_2(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

