#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[3]:


# import numpy
# import json_tricks
# import os

# numpy.random.seed(42)

# debug_cases = []
# for index in range(20):
#     A_shape = numpy.random.randint(1, 10, size=[2])
#     B_shape = numpy.random.randint(1, 10, size=[2])
    
#     A_shape[1] = A_shape[0]
#     B_shape = A_shape

#     A = numpy.random.randint(-5, 5, size=A_shape)
#     B = numpy.random.randint(-5, 5, size=B_shape)

#     debug_cases.append({'A': A, 'B': B})

# os.makedirs('testcases', exist_ok=True)
# with open('testcases/debug_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(debug_cases))

# public_cases = []
# for index in range(20):
#     A_shape = numpy.random.randint(1, 30, size=[2])
#     B_shape = numpy.random.randint(1, 30, size=[2])
    
#     A_shape[1] = A_shape[0]
#     B_shape = A_shape

#     A = numpy.random.randint(-10, 10, size=A_shape)
#     B = numpy.random.randint(-10, 10, size=B_shape)

#     public_cases.append({'A': A, 'B': B})

# with open('testcases/public_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(public_cases))


# In[1]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

print(path, '<- Path', file=sys.stderr)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/1. Gauss Elimination Step 1')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[8]:


import sys
sys.path.append('../../../../../code/')
sys.path.append('code/')

from gauss_elimination_1 import gauss_elimination_1
# import numpy as np

# A = np.array([
#     [1, 2, 3, 4],
#     [2, 1, 2, 3],
#     [3, 2, 1, 2],
#     [4, 3, 2, 1]
# ]).astype(float)

# P, A, B = gauss_elimination_1(A, np.eye(*A.shape))

# print(np.eye(*A.shape))
# print(P @ A @ B)

# print(P)
# print(A)
# print(B)


# In[6]:


import time

start = time.time()

debug_result = [gauss_elimination_1(**x) for x in debug_cases]
answer = [gauss_elimination_1(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

