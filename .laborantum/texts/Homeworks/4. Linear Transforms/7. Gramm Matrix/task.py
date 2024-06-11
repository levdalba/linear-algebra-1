#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    B_shape = numpy.random.randint(1, 10, size=[2])
    B_shape[1] = B_shape[0]

    B_L = numpy.tril(numpy.random.randint(-5, 5, size=B_shape))
    B_U = numpy.triu(numpy.random.randint(-5, 5, size=B_shape))

    numpy.fill_diagonal(B_L, 1)
    numpy.fill_diagonal(B_U, 1)

    B = B_L @ B_U

    x = numpy.random.randint(-5, 5, size=[B_shape[0]])
    debug_cases.append({'B': B, 'x': x})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    B_shape = numpy.random.randint(1, 10, size=[2])
    B_shape[1] = B_shape[0]

    B_L = numpy.tril(numpy.random.randn(*B_shape))
    B_U = numpy.triu(numpy.random.randn(*B_shape))

    numpy.fill_diagonal(B_L, 1)
    numpy.fill_diagonal(B_U, 1)

    B = B_L @ B_U

    x = numpy.random.randint(-5, 5, size=[B_shape[0]])
    public_cases.append({'B': B, 'x': x})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/7. Gramm Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[3]:


import numpy as np

def contra_to_co(B, x):
    G = B @ B.T
    return G @ x


# In[4]:


import time

start = time.time()

debug_result = [contra_to_co(**x) for x in debug_cases]
answer = [contra_to_co(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:





# In[ ]:




