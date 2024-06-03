#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[1]:


# import numpy
# import json_tricks
# import os

# numpy.random.seed(42)

# debug_cases = []
# for index in range(20):
#     A_shape = numpy.random.randint(1, 10, size=[2])
#     b_shape = A_shape[-1:]
#     A = numpy.random.randint(-10, 10, size=A_shape)
#     b = numpy.random.randint(-10, 10, size=b_shape)
#     debug_cases.append({'A': A, 'b': b})

# os.makedirs('testcases', exist_ok=True)
# with open('testcases/debug_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(debug_cases))

# public_cases = []
# for index in range(100):
#     A_shape = numpy.random.randint(1, 10, size=[2])
#     b_shape = A_shape[-1:]
#     A = numpy.random.randn(*A_shape)
#     b = numpy.random.randn(*b_shape)
#     public_cases.append({'A': A, 'b': b})

# with open('testcases/public_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(public_cases))


# In[4]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/2. Vector Spaces/1. Span Numpy')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[3]:


import numpy as np
import numpy.typing as npt

def linear_combination(A, b):
    return (A * b.reshape([1, -1])).sum(axis=1)


# In[5]:


import time

start = time.time()

debug_result = [linear_combination(**x) for x in debug_cases]
answer = [linear_combination(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

