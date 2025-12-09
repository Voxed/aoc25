import numpy as np
from itertools import combinations
from shapely import Polygon
from shapely.geometry import box

l = [(*map(int, e.strip().split(',')),) for e in open(0)]
boxes = [
    box(
        min(s1[0], s2[0]),
        min(s1[1], s2[1]),
        max(s1[0], s2[0]),
        max(s1[1], s2[1])
    ).buffer(0.5, join_style=2) for s1, s2 in combinations(l, 2)]
print(int(np.max([p.area for p in boxes])))

print(int(
    sorted([b.area for b in filter(
        Polygon(l).buffer(0.5, join_style=2).contains, boxes)
    ])[-1]))
