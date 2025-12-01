import numpy as np

i = [50] + [int(l[1:]) * (-1 if l[0] == 'L' else 1) for l in open("input.txt")]

# 1
print(np.sum(np.cumsum(i) % 100 == 0))

# 2
print(np.sum(np.cumsum(np.concat([[np.sign(l)] * abs(l) for l in i])) % 100 == 0))
