import numpy as np
from itertools import combinations
from shapely import Polygon
from shapely.geometry import box
import matplotlib.pyplot as plt


l = [(*map(int, e.strip().split(',')),) for e in open(0)]
c = list(combinations(l, 2))
s = 0
for (s1, s2) in c:
    size = (abs(s1[0] - s2[0])+1) * (abs(s1[1] - s2[1])+1)
    if size > s:
        print(s1, s2)
        s = size
print(s)

p = Polygon(l)
p = p.buffer(0.5, join_style=2)

x,y = p.exterior.xy
l = zip(x,y)
s = 0
f = None
for (s1, s2) in c:
    size = abs(s1[0] - s2[0]) * abs(s1[1] - s2[1])
    b = box(min(s1[0], s2[0]), min(s1[1], s2[1]), max(s1[0], s2[0]), max(s1[1], s2[1]))
    b = b.buffer(0.5, join_style=2)
    if b.area > s:
        if p.contains(b):
            print(s1, s2)
            f = b
            s = b.area
print(s)
plt.plot(x,y)
plt.plot(*f.exterior.xy)
plt.show()