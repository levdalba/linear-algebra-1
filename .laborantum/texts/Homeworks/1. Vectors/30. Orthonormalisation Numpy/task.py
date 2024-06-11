#!/usr/bin/env python
# coding: utf-8

# In[8]:


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


# In[9]:


import json_tricks

path = Path(".laborantum/texts/Homeworks/1. Vectors/30. Orthonormalisation Numpy")


# In[10]:


debug_cases = json_tricks.load(str(path / "testcases" / "debug_cases.json"))
public_cases = json_tricks.load(str(path / "testcases" / "public_cases.json"))


# In[11]:


import numpy as np


def orthonormalisation(vecs):
    ## YOUR CODE HERE
    res = []
    for v in vecs:
        w = v - sum(np.dot(v, u) * u for u in res)
        if np.linalg.norm(w) > 1e-4:
            res.append(w / np.linalg.norm(w))
    return np.array(res)


# In[12]:


# import numpy
# import json_tricks

# numpy.random.seed(42)

# debug_cases = []
# for index in range(20):
#     vecs = []
#     n = numpy.random.randint(1, 10)
#     shape = numpy.random.randint(1, 10)
#     for index in range(n):
#         x = numpy.random.randint(-10, 10, size=shape)
#         vecs.append(x)
#     debug_cases.append({'vecs': vecs})

# with open('testcases/debug_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(debug_cases))

# public_cases = []
# for index in range(100):
#     vecs = []
#     n = numpy.random.randint(1, 100)
#     shape = numpy.random.randint(1, 100)
#     for index in range(n):
#         x = numpy.random.randn(shape)
#         vecs.append(x)
#     public_cases.append({'vecs': vecs})

# with open('testcases/public_cases.json', 'w+') as fin:
#     fin.write(json_tricks.dumps(public_cases))


# In[13]:


import time

start = time.time()

debug_result = [orthonormalisation(**x) for x in debug_cases]
answer = [orthonormalisation(**x) for x in public_cases]

print(time.time() - start, "<- Elapsed time")


# In[16]:


json_tricks.dump(answer, "test.json")


# In[ ]:




