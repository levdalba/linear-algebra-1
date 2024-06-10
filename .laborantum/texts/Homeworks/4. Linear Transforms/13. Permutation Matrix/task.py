#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    N = numpy.random.randint(1, 20, size=[1])[0]
    perm = numpy.random.permutation(N)
    debug_cases.append({'perm': perm})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    N = numpy.random.randint(1, 20, size=[1])[0]
    perm = numpy.random.permutation(N)
    public_cases.append({'perm': perm})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


# In[7]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/13. Permutation Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[8]:


import numpy as np

def permutation_matrix(perm):
    N = len(perm)
    res = np.zeros([N, N])

    res[np.arange(N), perm] = 1
    
    return res


# In[9]:


import time

start = time.time()

debug_result = [permutation_matrix(**x) for x in debug_cases]
answer = [permutation_matrix(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




