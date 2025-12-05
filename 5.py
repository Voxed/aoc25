import numpy as np

i = [e.strip() for e in open(0)]
r=eval('['+','.join(['(' + e.replace('-',',') + "+1)" for e in i[:i.index('')]])+']')
j=[int(e) for e in i[i.index('')+1:]]
r.sort()
print(r)

s = 0
p = 0
for ra in r:
    if p < ra[0]:
        p = ra[0]
    if p >= ra[1]:
        continue
    s += ra[1] - p
    p = ra[1]
print(s)