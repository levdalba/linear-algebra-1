#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[2]:


# import numpy
# import json_tricks
# import os

# numpy.random.seed(42)

# debug_cases = []
# for index in range(20):
#     A_shape = numpy.random.randint(1, 10, size=[2])
    
#     # A_shape[1] = A_shape[0]
#     if A_shape[0] > A_shape[1]:
#         A_shape[[0, 1]] = A_shape[[1, 0]]

#     A = numpy.random.randint(-4, 4, size=A_shape).astype(float)

#     debug_cases.append({'A': A})

# os.makedirs('testcases', exist_ok=True)
# with open('testcases/debug_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(debug_cases))

# public_cases = []
# for index in range(100):
#     A_shape = numpy.random.randint(1, 10, size=[2])
    
#     # A_shape[1] = A_shape[0]
#     if A_shape[0] > A_shape[1]:
#         A_shape[[0, 1]] = A_shape[[1, 0]]

#     A = numpy.random.randint(-5, 5, size=A_shape).astype(float)

#     # print(A)

#     # print(numpy.linalg.det(A_low), numpy.linalg.det(A_up))
#     # print(numpy.linalg.det(A))

#     public_cases.append({'A': A})

# with open('testcases/public_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(public_cases))


# In[3]:


from find_kernel import find_kernel
import numpy as np


# In[4]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/6. Nonsquare SLE/2. Matrix Null-Space')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[5]:


import time

start = time.time()

print("Debug")
debug_result = [find_kernel(**x) for x in debug_cases]

print("Public")
answer = [find_kernel(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[6]:


print("Checking misfits |Ax - b|:")
print("Misfit should be < 1.0e-8")
print()
print('=' * 5 + ' DEBUG CASES ' + '='*5)
for index in range(len(debug_result)):
    case = debug_cases[index]
    NS = debug_result[index]

    A = case['A']
    
    print(
        'Case #' + str(index),
        np.abs(A @ NS).sum())
    

print()
print('=' * 5 + ' TEST CASES ' + '=' * 5)
for index in range(len(answer)):
    case = public_cases[index]
    NS = answer[index]

    A = case['A']
    # b = case['b']

    # print(A)
    # print(numpy.linalg.inv(A))
    # print(numpy.linalg.det(A))

    # print(A.shape, A_inv.shape)
    print(
        'Case #' + str(index),
        np.abs(A @ NS).sum())
print('=' * 5 + ' END ' + '=' * 5)


# In[ ]:




