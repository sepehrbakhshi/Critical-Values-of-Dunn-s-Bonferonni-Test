import numpy as np
from scipy.stats import studentized_range

initial_alpha = 0.1
initial_k = 8

alpha = initial_alpha/(initial_k-1)

k = 2 # number of groups
df = np.inf # degrees of freedom

q = studentized_range.isf(alpha, k, df)

cv = q/np.sqrt(2)
print(cv)