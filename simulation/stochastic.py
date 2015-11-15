# stochastic.py
import random as randint
import numpy as np
## generate random 6x6 stochastic matrix
i = 0
m = []
while i < 6:
    t = 0
    a = []
    while t < 6:
        v = [np.random.randint(0,100)]
        a.extend(v)
        t += 1
    s = np.sum(a)
    a = a/s
    e = np.sum(a)
    print(e)
    m.append(a)
    i += 1
print(m)


## visualize the stochastic process from the generated transition matrix
