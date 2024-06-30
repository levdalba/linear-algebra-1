#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[12]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    A_shape = numpy.random.randint(1, 10, size=[2])
    B_shape = numpy.random.randint(1, 10, size=[2])
    
    A_shape[1] = A_shape[0]
    B_shape[0] = A_shape[1]
    B_shape[1] = 1

    A = numpy.random.randint(-5, 5, size=A_shape)
    B = numpy.random.randint(-5, 5, size=B_shape)

    A_low = numpy.tril(A)
    numpy.fill_diagonal(A_low, 1)
    A_up = numpy.triu(A)
    numpy.fill_diagonal(A_up, 1)
    A = A_low @ A_up

    debug_cases.append({'A': A, 'b': A @ B})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(100):
    A_shape = numpy.random.randint(1, 100, size=[2])
    B_shape = numpy.random.randint(1, 100, size=[2])
    
    A_shape[1] = A_shape[0]
    B_shape[0] = A_shape[1]
    B_shape[1] = 1

    A = numpy.random.randint(-5, 5, size=A_shape)
    B = numpy.random.randint(-5, 5, size=B_shape)

    A_low = numpy.tril(A)
    numpy.fill_diagonal(A_low, 1)
    A_up = numpy.triu(A)
    numpy.fill_diagonal(A_up, 1)
    A = A_low @ A_up

    public_cases.append({'A': A, 'b': A @ B})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


# In[8]:


from find_solution import find_solution
import numpy as np



# In[9]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/3. Solving Square SLE')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[10]:


import time

start = time.time()

debug_result = [find_solution(**x) for x in debug_cases]
answer = [find_solution(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[11]:


print("Checking misfits |Ax - b|:")
print("Misfit should be < 1.0e-8")
print()
print('=' * 5 + ' DEBUG CASES ' + '='*5)
for index in range(len(debug_result)):
    case = debug_cases[index]
    x = debug_result[index]

    A = case['A']
    b = case['b']

    print(
        'Case #' + str(index),
        np.abs(A.astype(float) @ x.astype(float) - b.astype(float)).sum())
    

print()
print('=' * 5 + ' TEST CASES ' + '=' * 5)
for index in range(len(answer)):
    case = public_cases[index]
    x = answer[index]

    A = case['A']
    b = case['b']

    print(
        'Case #' + str(index),
        np.abs(A.astype(float) @ x.astype(float) - b.astype(float)).sum())
print('=' * 5 + ' END ' + '=' * 5)


# In[ ]:




