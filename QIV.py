# Question 4
import numpy as np
from numpy.random import normal
from numpy.random import seed


seed(1)

"""
Generate normal distro and find mean
"""
def genNorm(size):
    data = normal(loc=0, scale=1, size=size)
    mu = np.mean(data)
    return mu

mus = []

for i in range(100):
    mus.append(genNorm(5))

print(np.mean(mus))
print(np.var(mus))

mus = []

for i in range(5):
    mus.append(genNorm(100))

print(np.mean(mus))
print(np.var(mus))



