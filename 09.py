import numpy as np
from shapely import Polygon, Point
from collections import defaultdict
from itertools import combinations

l = [(*map(int, e.strip().split(',')),) for e in open(0)]

# =============================================================================
#                                   Part 1
# =============================================================================
print(
    np.max([
        (abs(x1 - x2) + 1)*(abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in combinations(l, 2)
    ]))

# =============================================================================
#                            Coordinate Compression
# =============================================================================

# These arrays are used to unmap from compressed space to uncompressed space.
xx = sorted(set(p[0] for p in l))
yy = sorted(set(p[1] for p in l))

# These dictionaries are used to map from uncompressed space to compressed space
xx_map = {val: index for index, val in enumerate(xx)}
yy_map = {val: index for index, val in enumerate(yy)}

# This array is used to quickly check available x coordinates on a row. This
# is important as we need to check whether our minimum bounding box corners
# two vertices.
xcoords_on_row = defaultdict(list)
ycoords_on_col = defaultdict(list)
for x, y in l:
    x_compressed = xx_map[x]
    y_compressed = yy_map[y]
    xcoords_on_row[y_compressed].append(x_compressed)
    ycoords_on_col[x_compressed].append(y_compressed)

# =============================================================================
#                            Rasterize Container
# =============================================================================
compressed_polygon = Polygon([(xx_map[p[0]], yy_map[p[1]]) for p in l])
world_shape = (len(yy), len(xx))
arr = np.array(
    [
        compressed_polygon.covers(Point(x, y))
        for y, x in np.ndindex(world_shape)
    ]).reshape(world_shape)

# =============================================================================
#                        Calculate Clearance Histogram
# =============================================================================
# In order to quickly check how large of a rectangle will fit between two x
# coordinates we construct a 2D array where each cell correspondes to the
# amount of y-space available above the cell.
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

# Construction is trivial, we keep track of the current height available in
# each column and iterate down. Resetting if we step outside the shape.
height_hist = np.zeros(len(xx))
vertical_clearance = np.zeros(arr.shape)
for (y, x) in np.ndindex(arr.shape):
    if arr[y, x]:
        vertical_clearance[y, x] = height_hist[x]
        height_hist[x] += 1
    else:
        height_hist[x] = 0

# =============================================================================
#                      Find Max Internal Bounding Box
#                          (with corners in input)
# =============================================================================
# This part is not very optimized, but the main bottleneck is rasterization
# anyway.
#
# We iterate over each x-vertex on a row. We then consider each other
# x-coordinate. For each of these other x-coordinates we fetch all the
# y-vertices that would fit within the clearence in of the vertical
# clearance array. These vertices, a long with the row we're on gives us a
# box that fits the shape.
#
# Then it's trivial to find the box with the maximum area.

area_max = 0
for y_max, r in enumerate(vertical_clearance):

    # Iterate all the x-vertices on this row
    for x1 in xcoords_on_row[y_max]:

        # For each one, try every other x-coordinate
        for x2 in range(len(r)):

            # Find the maximum available clearance between these x1 and x2.
            clearence = int(y_max - min(r[x1], r[x2]))

            # Iterate over all y-vertices that fits the clearence
            for y_min in (
                    y for y in ycoords_on_col[x2] if y >= clearence
            ):
                x_min = min(x1, x2)
                x_max = max(x1, x2)

                # Map back to uncompressed space and calculate the area :)
                height = yy[y_max] - yy[y_min] + 1
                width = xx[x_max] - xx[x_min] + 1
                area = width * height
                if area > area_max:
                    area_max = area

# =============================================================================
#                              Print Part 2
# =============================================================================
print(area_max)

# =============================================================================
#                         First Slow(ish) Solution
# =============================================================================
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