#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[3]:


from plu_decomposition import plu_decomposition
import numpy as np



# In[4]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/5. PLU Decomposition')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[5]:


import time

start = time.time()

debug_result = [plu_decomposition(**x) for x in debug_cases]
answer = [plu_decomposition(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[6]:


print("Checking misfits |Ax - b|:")
print("Misfit should be < 1.0e-8")
print()
print('=' * 5 + ' DEBUG CASES ' + '='*5)
for index in range(len(debug_result)):
    case = debug_cases[index]
    P, L, U = debug_result[index]

    A = case['A']
    
    print(
        'Case #' + str(index),
        np.abs(A.astype(float) - P @ L @ U).sum())
    

print()
print('=' * 5 + ' TEST CASES ' + '=' * 5)
for index in range(len(answer)):
    case = public_cases[index]
    P, L, U = answer[index]

    A = case['A']
    # b = case['b']

    # print(A)
    # print(numpy.linalg.inv(A))
    # print(numpy.linalg.det(A))

    # print(A.shape, A_inv.shape)
    print(
        'Case #' + str(index),
        np.abs(A.astype(float) - P @ L @ U).sum())
print('=' * 5 + ' END ' + '=' * 5)

