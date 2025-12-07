from functools import cache

l = [list(e.strip()) for e in open(0)]
reached = set()

@cache
def tl(x, y):
    if y+1 < len(l):
        match l[y+1][x]:
            case '.':
                return tl(x,y+1)
            case '^':
                reached.add((x,y+1))
                return tl(x+1,y+1) + tl(x-1,y+1) + 1
    return 0

for y, r in enumerate(l):
    for x, e in enumerate(r):
        if e == 'S':
            timelines = tl(x,y)+1

print(timelines)
print(len(reached))