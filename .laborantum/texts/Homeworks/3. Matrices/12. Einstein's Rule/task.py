#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 10, size=[2])
    B_shape = numpy.random.randint(1, 10, size=[2])
    C_shape = numpy.random.randint(1, 10, size=[2])
    D_shape = numpy.random.randint(1, 10, size=[2])
    A_shape[1] = B_shape[0]
    B_shape[1] = C_shape[0]
    D_shape[1] = A_shape[0]
    A = numpy.random.randint(-5, 5, size=A_shape)
    B = numpy.random.randint(-5, 5, size=B_shape)
    C = numpy.random.randint(-5, 5, size=C_shape)
    D = numpy.random.randint(-5, 5, size=D_shape)
    debug_cases.append({'A': A, 'B': B, 'C': C, 'D': D})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 10, size=[2])
    B_shape = numpy.random.randint(1, 10, size=[2])
    C_shape = numpy.random.randint(1, 10, size=[2])
    D_shape = numpy.random.randint(1, 10, size=[2])
    A_shape[1] = B_shape[0]
    B_shape[1] = C_shape[0]
    D_shape[1] = A_shape[0]
    A = numpy.random.randn(*A_shape)
    B = numpy.random.randn(*B_shape)
    C = numpy.random.randn(*C_shape)
    D = numpy.random.randn(*D_shape)
    public_cases.append({'A': A, 'B': B, 'C': C, 'D': D})

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

path = Path(".laborantum/texts/Homeworks/3. Matrices/12. Einstein's Rule")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[ ]:


import numpy as np

def formula(A, B, C, D):
    return D @ A @ B @ C


# In[ ]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

