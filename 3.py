import numpy as np

b = [np.array(list(e.strip()), dtype=int) for e in open(0)]

def largest(b, n):
    if n == -1:
        return 0
    i = np.argmax(b[:-n or None])
    return b[i]*10**n + largest(b[i+1:], n-1)

[print(sum([largest(b, i) for b in b])) for i in [1,11]]