#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[14]:


from find_solution import find_solution
import numpy as np


# In[15]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/3. Solving Square SLE')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[16]:


import time

start = time.time()

debug_result = [find_solution(**x) for x in debug_cases]
answer = [find_solution(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[17]:


print("Checking misfits |Ax - b|:")
print("Misfit should be < 1.0e-8")
print()
print('=' * 5 + ' DEBUG CASES ' + '='*5)
for index in range(len(debug_result)):
    case = debug_cases[index]
    x = debug_result[index]

    A = case['A']
    b = case['b']

    print(
        'Case #' + str(index),
        np.abs(A.astype(float) @ x.astype(float) - b.astype(float)).sum())
    

print()
print('=' * 5 + ' TEST CASES ' + '=' * 5)
for index in range(len(answer)):
    case = public_cases[index]
    x = answer[index]

    A = case['A']
    b = case['b']

    print(
        'Case #' + str(index),
        np.abs(A.astype(float) @ x.astype(float) - b.astype(float)).sum())
print('=' * 5 + ' END ' + '=' * 5)


# In[ ]:




