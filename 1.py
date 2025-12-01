import numpy as np

i = [50] + [int(l[1:]) * (-1 if l[0] == 'L' else 1) for l in open("input.txt").readlines()]

# 1
print(np.count_nonzero(np.cumsum(i) % 100 == 0))

# 2
print(np.count_nonzero(np.cumsum(np.concat([[np.sign(l)] * abs(l) for l in i])) % 100 == 0))
