import copy
from functools import cache

l = [list(e.strip()) for e in open(0)]

@cache
def tl(x, y):
    if y+1 < len(l):
        match l[y+1][x]:
            case '.':
                return tl(x,y+1)
            case '^':
                return tl(x+1,y+1) + tl(x-1,y+1) + 1
    return 0

for y, r in enumerate(l):
    for x, e in enumerate(r):
        if e == 'S':
            print("S at ", x, y)
            print(tl(x,y)+1, x, y)