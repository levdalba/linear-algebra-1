#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    theta = numpy.random.uniform(1)
    debug_cases.append({'theta': theta})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    theta = numpy.random.uniform(1)
    public_cases.append({'theta': theta})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


# In[3]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/14. 2D Rotation Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[4]:


import numpy as np

def rotation_matrix(theta):
    res = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return res


# In[ ]:


import time

start = time.time()

debug_result = [rotation_matrix(**x) for x in debug_cases]
answer = [rotation_matrix(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




