cond = [(list(map(int, a.split('x'))), list(map(int, b.split())))
        for a, b in [e.split(': ') for e in open(0).read().split('\n\n')[-1].strip().split('\n')]]
print(sum([sum(c) * 9 <= x * y for (x, y), c in cond]))
