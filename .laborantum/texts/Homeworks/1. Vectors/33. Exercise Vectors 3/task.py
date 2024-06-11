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

get_ipython().system('{sys.executable} -m pip -q install numpy json-tricks torch jupyter nbconvert')


# In[4]:


import json_tricks

path = Path(".laborantum/texts/Homeworks/1. Vectors/33. Exercise Vectors 3")


# In[5]:


debug_cases = json_tricks.load(str(path / "testcases" / "debug_cases.json"))
public_cases = json_tricks.load(str(path / "testcases" / "public_cases.json"))


# In[6]:


import numpy as np
import numpy.typing as npt
from typing import Dict


def vector_operations(a, b):
    ## YOUR CODE HERE

    expression = 2 * a + b

    # Calculate the dot product ⟨a, b⟩
    dot_prod = np.dot(a, b)

    # Calculate the magnitudes |a| and |b|
    length_a = np.linalg.norm(a)
    length_b = np.linalg.norm(b)

    # Calculate the angle between a and b in radians
    angle = np.arccos(dot_prod / (length_a * length_b))

    # Find directions of these vectors
    dir_a = a / length_a
    dir_b = b / length_b

    # Find collinear component (projection)
    a_proj_b = (dot_prod / np.dot(b, b)) * b
    b_proj_a = (dot_prod / np.dot(a, a)) * a

    # Find orthogonal component
    a_orth_b = a - a_proj_b
    b_orth_a = b - b_proj_a

    answer = {
        "expression": expression.tolist(),
        "dot_prod": dot_prod,
        "length_a": length_a,
        "length_b": length_b,
        "angle": angle,
        "dir_a": dir_a.tolist(),
        "dir_b": dir_b.tolist(),
        "a_proj_b": a_proj_b.tolist(),
        "b_proj_a": b_proj_a.tolist(),
        "a_orth_b": a_orth_b.tolist(),
        "b_orth_a": b_orth_a.tolist(),
    }

    return answer


# In[7]:


import time

start = time.time()

debug_result = [vector_operations(**x) for x in debug_cases]
answer = [vector_operations(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")

