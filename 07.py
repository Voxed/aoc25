from functools import cache

# Simple parser today!
world = [list(e.strip()) for e in open(0)]

# Global variable for tracking unique splitters 
# (only for Part 1, memoize is done through functools.cache)
# Might be able to deduce this through the function
# cache but this is not code golf
hit_splitters = set()

# Function is cached (memoized)
@cache
def tl(x, y):
    if y+1 >= len(world):
        # We reached the bottom :)
        return 0
    else:
        match world[y+1][x]:
            case '.':
                # Continue on original timeline
                return tl(x, y+1)
            case '^':
                # Keep track of all the unique splitters for Part 1
                hit_splitters.add((x, y+1))
                # Split into two new timelines
                return tl(x+1, y+1) + tl(x-1, y+1) + 1


# Execute the original timeline with beam start at 'S'
for y, r in enumerate(world):
    for x, e in enumerate(r):
        if e == 'S':
            num_timelines = tl(x, y)+1

# Part 1
print(num_timelines)

# Part 2
print(len(hit_splitters))
