#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[1]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

print(path, '<- Path', file=sys.stderr)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/1. Gauss Elimination Step 1')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[8]:


import sys
sys.path.append('../../../../../code/')
sys.path.append('code/')

from gauss_elimination_1 import gauss_elimination_1


# In[6]:


import time

start = time.time()

debug_result = [gauss_elimination_1(**x) for x in debug_cases]
answer = [gauss_elimination_1(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

