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


# In[3]:


# import numpy
# import json_tricks
# import os

# numpy.random.seed(42)

# debug_cases = []
# for index in range(20):
#     A_shape = numpy.random.randint(1, 10, size=[2])
#     A = numpy.random.randint(-5, 5, size=A_shape)
#     if numpy.random.randn(1) < 0:
#         A[:, -1] = A[:, :-1] @ numpy.random.randint(-5, 5, size=[A.shape[-1] - 1])
#     debug_cases.append({'A': A.T})

# os.makedirs('testcases', exist_ok=True)
# with open('testcases/debug_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(debug_cases))

# public_cases = []
# for index in range(100):
#     A_shape = numpy.random.randint(1, 10, size=[2])
#     A = numpy.random.randn(*A_shape)
#     if numpy.random.randn(1) < 0:
#         A[:, -1] = A[:, :-1] @ numpy.random.randint(-5, 5, size=[A.shape[-1] - 1])
#     public_cases.append({'A': A.T})

# with open('testcases/public_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(public_cases))


# In[4]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/2. Vector Spaces/6. Linear Independency Task')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[7]:


import numpy as np


def is_independent(A):

    orthonormals = []
    for x in A:
        for y in orthonormals:
            dot_xy = (x * y).sum()
            len_y = np.sqrt((y * y).sum())

            x = x - dot_xy / len_y * y / len_y

        len_x = np.sqrt((x * x).sum())

        if len_x < 1.0e-4:
            return False
        
        orthonormals.append(x)
    
    return True


# In[8]:


import time

start = time.time()

debug_result = [is_independent(**x) for x in debug_cases]
answer = [is_independent(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[10]:


print(debug_result)
print(answer)


# In[ ]:




