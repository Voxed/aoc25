import numpy as npagt

l = [list(e.strip()) for e in open(0)]
sum = 0
while(True):
    for y, r in enumerate(l):
        for x, e in enumerate(r):
            s = 0
            if y > 0:
                if l[y-1][x] == '@':
                    s+=1
                if x < len(r)-1:
                    if l[y-1][x+1] == '@':
                        s+=1
                if x > 0:
                    if l[y-1][x-1] == '@':
                        s+=1
            if y < len(l)-1:
                if l[y+1][x] == '@':
                    s+=1
                if x < len(r)-1:
                    if l[y+1][x+1] == '@':
                        s+=1
                if x > 0:
                    if l[y+1][x-1] == '@':
                        s+=1
            if x > 0:
                if l[y][x-1] == '@':
                    s+=1
            if x < len(r)-1:
                if l[y][x+1] == '@':
                    s+=1
            if s < 4 and e == '@':
                l[y][x] = '.'
                sum += 1
    print(sum)