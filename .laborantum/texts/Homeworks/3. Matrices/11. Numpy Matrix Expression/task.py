#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 10, size=[2])
    B_shape = numpy.random.randint(1, 10, size=[2])
    C_shape = numpy.random.randint(1, 10, size=[2])
    x_shape = numpy.random.randint(1, 10, size=[1])
    B_shape[0] = A_shape[0]
    C_shape[0] = A_shape[0]
    C_shape[1] = B_shape[1]
    x_shape[0] = B_shape[1]
    A = numpy.random.randint(-5, 5, size=A_shape)
    B = numpy.random.randint(-5, 5, size=B_shape)
    C = numpy.random.randint(-5, 5, size=C_shape)
    x = numpy.random.randint(-5, 5, size=x_shape)
    debug_cases.append({'A': A, 'B': B, 'C': C, 'x': x})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 30, size=[2])
    B_shape = numpy.random.randint(1, 30, size=[2])
    C_shape = numpy.random.randint(1, 30, size=[2])
    x_shape = numpy.random.randint(1, 30, size=[1])
    B_shape[0] = A_shape[0]
    C_shape[0] = A_shape[0]
    C_shape[1] = B_shape[1]
    x_shape[0] = B_shape[1]
    A = numpy.random.randn(*A_shape)
    B = numpy.random.randn(*B_shape)
    C = numpy.random.randn(*C_shape)
    x = numpy.random.randn(*x_shape)
    public_cases.append({'A': A, 'B': B, 'C': C, 'x': x})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


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


# In[6]:


import numpy as np

def formula(A, B, C, x):
    I = np.eye(A.shape[1], B.shape[1])
    return np.exp(A.T @ (B + 2 * C) + 3 * I) @ x


# In[7]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




