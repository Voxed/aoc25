from functools import cache

world = [list(e.strip()) for e in open(0)]
hit_splitters = set()

@cache
def tl(x, y):
    if y+1 < len(world):
        match world[y+1][x]:
            case '.':
                return tl(x,y+1)
            case '^':
                # We keep track of all the unique splitters for Part 1
                hit_splitters.add((x,y+1))
                return tl(x+1,y+1) + tl(x-1,y+1) + 1
    return 0

for y, r in enumerate(world):
    for x, e in enumerate(r):
        if e == 'S':
            num_timelines = tl(x,y)+1

print(num_timelines)
print(len(hit_splitters))