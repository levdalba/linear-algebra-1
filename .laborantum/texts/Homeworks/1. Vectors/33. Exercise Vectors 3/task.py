#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[4]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/1. Vectors/33. Exercise Vectors 3')


# In[5]:


debug_cases = json_tricks.load(str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(str(path / 'testcases' / 'public_cases.json'))


# In[15]:


import numpy as np
import numpy.typing as npt
from typing import Dict

def vector_operations(x, y):

    a, b = x, y

    dot_ab = (a * b).sum()

    len_a = np.sqrt((a * a).sum())
    len_b = np.sqrt((b * b).sum())

    angle = np.arccos(dot_ab / len_a / len_b)

    dir_a = a / len_a
    dir_b = b / len_b

    a_proj_b = dot_ab / len_b ** 2
    b_proj_a = dot_ab / len_a ** 2

    a_orth_b = a - a_proj_b
    b_orth_a = b - b_proj_a

    answer = {
        'expression': 2 * a + b,
        'dot_prod': dot_ab,
        'length_a': len_a,
        'length_b': len_b,
        'angle': angle,
        'dir_a': dir_a,
        'dir_b': dir_b,
        'a_proj_b': a_proj_b,
        'b_proj_a': b_proj_a,
        'a_orth_b': a_orth_b,
        'b_orth_a': b_orth_a
    }

    return answer


# In[16]:


import time

start = time.time()

debug_result = [vector_operations(**x) for x in debug_cases]
answer = [vector_operations(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




