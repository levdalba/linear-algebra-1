#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[8]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 10, size=[2])
    B_shape = numpy.random.randint(1, 10, size=[2])
    
    A_shape[1] = A_shape[0]
    B_shape = A_shape

    A = numpy.random.randint(-5, 5, size=A_shape)
    B = numpy.random.randint(-5, 5, size=B_shape)

    A = numpy.triu(A)
    numpy.fill_diagonal(A, 1)

    debug_cases.append({'A': A, 'B': B})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 30, size=[2])
    B_shape = numpy.random.randint(1, 30, size=[2])
    
    A_shape[1] = A_shape[0]
    B_shape = A_shape

    A = numpy.random.randint(-10, 10, size=A_shape)
    B = numpy.random.randint(-10, 10, size=B_shape)

    A = numpy.triu(A)
    numpy.fill_diagonal(A, 1)

    public_cases.append({'A': A, 'B': B})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


# In[9]:


from gauss_elimination_2 import gauss_elimination_2
import numpy as np



# In[10]:


import sys
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

