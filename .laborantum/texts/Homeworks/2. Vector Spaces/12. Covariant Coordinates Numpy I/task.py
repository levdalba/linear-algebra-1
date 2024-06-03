#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

get_ipython().system('{sys.executable} -m pip -q install --user numpy json-tricks torch jupyter nbconvert')


# In[8]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    B_shape = numpy.random.randint(1, 10, size=[2])
    B_shape.sort(axis=0)
    B_shape = B_shape[::-1]
    B = numpy.random.randint(-5, 5, size=B_shape)
    x_shape = B_shape[-1:]
    x = numpy.random.randint(-5, 5, size=x_shape)
    # if numpy.random.randn(1) < 0:
        # A[:, -1] = A[:, :-1] @ numpy.random.randint(-5, 5, size=[A.shape[-1] - 1])
    debug_cases.append({'B': B, 'x': x})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(100):
    B_shape = numpy.random.randint(1, 10, size=[2])
    B_shape.sort(axis=0)
    B_shape = B_shape[::-1]
    B = numpy.random.randint(-5, 5, size=B_shape)
    x_shape = B_shape[-1:]
    x = numpy.random.randint(x_shape)
    
    public_cases.append({'B': B, 'x': x})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


# In[10]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/2. Vector Spaces/12. Covariant Coordinates Numpy I')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[11]:


import numpy as np

def get_covariant_coordinates(B, x):
    return (B * x.reshape([1, -1])).sum(axis=1)


# In[12]:


import time

start = time.time()

debug_result = [get_covariant_coordinates(**x) for x in debug_cases]
answer = [get_covariant_coordinates(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




