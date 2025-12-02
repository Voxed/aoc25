import numpy as np

l = [np.array(e.split('-'), dtype=int) for e in open(0).read().split(',')]

sum = 0

for r in l:
    for i in range(r[0], r[1]+1):
        id = str(i)
        for p in range(1, len(id)+1):
            if len(id) % p == 0:
                reps = len(id) // p
                if reps >= 2:
                    prefix = id[:p]
                    if id == prefix * reps:
                        sum += i
                        break

print(sum)
