#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


import json_tricks

path = Path(".laborantum/texts/Homeworks/2. Vector Spaces/1. Span Numpy")

debug_cases = json_tricks.load(str(path / "testcases" / "debug_cases.json"))
public_cases = json_tricks.load(str(path / "testcases" / "public_cases.json"))


# In[5]:


import numpy as np
import numpy.typing as npt


def linear_combination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    ## YOUR CODE HERE
    weighted_A = A.T * b[:, np.newaxis]

    # Sum the weighted vectors along the columns to get the final result
    result = np.sum(weighted_A, axis=0)

    return result


# In[4]:


import time

start = time.time()

debug_result = [linear_combination(**x) for x in debug_cases]
answer = [linear_combination(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")

