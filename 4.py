import numpy as np
f = 1
l = np.pad(np.array([[1 if u == '@' else 0 for u in e.strip()] for e in open(0)]), ((1,1),(1,1)))
a = 0
while True:
    s = np.roll(l, 1, 0) + l + np.roll(l, -1, 0)
    t = np.roll(s, 1, 1) + s + np.roll(s, -1, 1)
    r = (l==1) & (t<5)
    a += r.sum()
    if f:
        f = 0
        print(a)
    if r.sum() == 0:
        break
    l = l & ~r
print(a)