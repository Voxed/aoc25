# ==================================================================
#                    First Slow(ish) Solution
# ==================================================================
'''
boxes = [
    box(
        min(s1.x, s2.x),
        min(s1.y, s2.y),
        max(s1.x, s2.x),
        max(s1.y, s2.y)
    ).buffer(0.5, join_style=2) for s1, s2 in combinations(l, 2)]
print(len(boxes))
print(int(np.max([p.area for p in boxes])))

print(int(
    sorted([b.area for b in filter(
        Polygon(l).buffer(0.5, join_style=2).contains, boxes)
    ])[-1]))

#for p in filter(Polygon(l).buffer(0.5, join_style=2).contains, boxes):
#    pyplot.plot(*p.exterior.xy)
w = Polygon(l)
for r in w:
    pyplot.plot(r.xy)'''


import numpy as np
from shapely import Polygon, Point
from matplotlib import pyplot

l = [(*map(int, e.strip().split(',')),) for e in open(0)]

# ==================================================================
#                     Coordinate Compression
# ==================================================================

# These arrays are used to unmap from compressed space to
# uncompressed space.
xx = sorted(set(p[0] for p in l))
yy = sorted(set(p[1] for p in l))

# These dictionaries are used to map from uncompressed space to
# compressed space
xx_map = {val: index for index, val in enumerate(xx)}
yy_map = {val: index for index, val in enumerate(yy)}

# This array is used to quickly check available x coordinates on a
# row. This is important as we need to check whether our minimum
# bounding box corners two vertices.
xcoords_on_row = [
    [x for x in range(len(xx)) if (xx[x], yy[y]) in l]
    for y in range(len(yy))]

# ==================================================================
#                       Rasterize Container
# ==================================================================
polygon = Polygon([(xx_map[p[0]], yy_map[p[1]]) for p in l])
compressed_polygon = Polygon([(xx_map[p[0]], yy_map[p[1]]) for p in l])
world_shape = (len(yy), len(xx))
arr = np.array(
    [
        compressed_polygon.covers(Point(x,y))
        for y,x in np.ndindex(world_shape)
    ]).reshape(world_shape)

# ==================================================================
#                   Calculate Height Histogram
# ==================================================================

# In order to quickly check how large of a rectangle WWwill fit
# between two x coordinates we construct a 2D array where each cell
# correspondes to the amount of y-space available above the cell.
#
# Example on the test input:
# . . . . . . . . . . . .
# . . . . . . 0 0 0 0 0 .
# . . . . . . 1 1 1 1 1 .
# . 0 0 0 0 0 2 2 2 2 2 .
# . 1 1 1 1 1 3 3 3 3 3 .
# . 2 2 2 2 2 4 4 4 4 4 .
# . . . . . . . . 5 5 5 .
# . . . . . . . . 6 6 6 .
# . . . . . . . . . . . .

# Construction is trivial, we keep track of the current height
# available in each column and iterate down. Resetting if we step
# outside the shape.
height_hist = np.zeros(len(xx))
vertical_space = np.zeros(arr.shape)
for (y, x) in np.ndindex(arr.shape):
    if arr[y, x]:
        vertical_space[y, x] = height_hist[x]
        height_hist[x] += 1
    else:
        height_hist[x] = 0

# ==================================================================
#                 Find Max Internal Bounding Box
#                    (with corners in input)
# ==================================================================
area_max = 0
for y_max, r in enumerate(vertical_space):
    for x1 in xcoords_on_row[y_max]:
        for x2 in range(len(r)):
            y_min = int(y_max - min(r[x1], r[x2]))
            if x2 in xcoords_on_row[y_min]:
                x_min = min(x1, x2)
                x_max = max(x1, x2)
                height = yy[y_max] - yy[y_min] + 1
                width = xx[x_max] - xx[x_min] + 1
                area = width * height
                if area > area_max:
                    area_max = area

# ==================================================================
#                        Print Part 1
# ==================================================================
print(area_max)
pyplot.imshow(vertical_space)
pyplot.show()
