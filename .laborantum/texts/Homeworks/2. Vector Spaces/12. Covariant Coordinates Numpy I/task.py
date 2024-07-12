#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# In[6]:


import json_tricks

path = Path(
    ".laborantum/texts/Homeworks/2. Vector Spaces/12. Covariant Coordinates Numpy I"
)

debug_cases = json_tricks.load(str(path / "testcases" / "debug_cases.json"))
public_cases = json_tricks.load(str(path / "testcases" / "public_cases.json"))


# In[1]:


import numpy as np


def get_covariant_coordinates(B, x):
    B = np.array(B)
    x = np.array(x)

    print(f"B shape: {B.shape}")
    print(f"x shape: {x.shape}")

    assert B.ndim == 2, "B must be a 2D numpy array"
    assert x.ndim == 1, "x must be a 1D numpy array"

    if B.shape[0] != x.size:
        raise ValueError(
            f"Incompatible dimensions: B has {B.shape[0]} rows but x has size {x.size}"
        )

    coords, residuals, rank, s = np.linalg.lstsq(B, x, rcond=None)

    return coords


# In[2]:


import time

start = time.time()

debug_result = [get_covariant_coordinates(**x) for x in debug_cases]
answer = [get_covariant_coordinates(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")

