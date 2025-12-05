import numpy as np

lines = [e.strip() for e in open(0)]
ranges = [tuple(np.array(e.split('-'), dtype=int)+(0, 1))
          for e in lines[:lines.index('')]]
ranges.sort()

# Part 1
a = 0
for ingredient in [int(e) for e in lines[lines.index('')+1:]]:
    for r in ranges:
        if r[0] <= ingredient < r[1]:
            a += 1
            break
print(a)

# Part 2
a = 0
cursor = 0
for r in ranges:
    if cursor >= r[1]:
        continue
    a += min(r[1]-cursor, r[1]-r[0])
    cursor = r[1]
print(a)
