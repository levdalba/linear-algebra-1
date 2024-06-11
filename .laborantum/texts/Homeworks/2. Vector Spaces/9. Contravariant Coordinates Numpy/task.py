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

path = Path(
    ".laborantum/texts/Homeworks/2. Vector Spaces/9. Contravariant Coordinates Numpy"
)

debug_cases = json_tricks.load(str(path / "testcases" / "debug_cases.json"))
public_cases = json_tricks.load(str(path / "testcases" / "public_cases.json"))


# In[3]:


import numpy as np


def vectors_from_contravariant_coords(B, C):
    B = np.array(B)
    C = np.array(C)

    if B.shape[1] != C.shape[1]:
        raise ValueError("Shapes are not aligned for matrix multiplication")

    # Compute the result using element-wise multiplication and summation
    V = np.einsum("ij,ik->kj", C, B)

    return V


# In[5]:


import time

start = time.time()

debug_result = [vectors_from_contravariant_coords(**x) for x in debug_cases]
answer = [vectors_from_contravariant_coords(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")

