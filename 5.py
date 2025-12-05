import numpy as np

lines = [e.strip() for e in open(0)]
ranges=[[*map(int,e.split('-'))] for e in lines[:lines.index('')]]
ranges.sort()

# Part 1
a = 0
for ingredient in [int(e) for e in lines[lines.index('')+1:]]:
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            a += 1
            break
print(a)

# Part 2
a = 0
cursor = 0
for r in ranges:
    if cursor < r[0]:
        cursor = r[0]
    if cursor > r[1]:
        continue
    a += r[1]+1 - cursor
    cursor = r[1]+1
print(a)