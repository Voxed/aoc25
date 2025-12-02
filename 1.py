import numpy as np

i = [int(l[1:]) * (-1 if l[0] == 'L' else 1) for l in open(0)]

# 1
print(np.sum(np.cumsum(i) % 100 == 50))

# 2
print(np.sum(np.cumsum(np.concat([[np.sign(l)] * abs(l) for l in i])) % 100 == 50))