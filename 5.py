import numpy as np

ranges, ingredients = open(0).read().split('\n\n')

# Parse ranges into tuples of (start(inclusive), end(exclusive)).
ranges = [tuple(np.array(e.split('-'), dtype=int)+(0, 1))
          for e in ranges.split()]
# Sort based on range start, this is the magic for Part 2
ranges.sort()

# Part 1: straightforward, add if ingredient is in any range.
a = 0
for ingredient in ingredients.split():
    for r in ranges:
        if r[0] <= int(ingredient) < r[1]:
            a += 1
            break
print(a)

# Part 2
a = 0
cursor = 0
for (start, end) in ranges:
    # If the cursor has passed the end of the range, it was contained
    # within some other range.
    if cursor >= end:
        continue
    # Since the cursor can be located before the range start, we need to
    # cap the size of the fresh range.
    a += min(end-cursor, end-start)
    # Since our ranges are sorted, we can move the cursor to the end
    # without skipping any earlier ranges.
    cursor = end
print(a)
