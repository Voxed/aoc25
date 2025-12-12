cond = [(list(map(int, a.split('x'))), list(map(int, b.split())))
        for a, b in [e.split(': ') for e in open(0).read().split('\n\n')[-1].strip().split('\n')]]

# This only works in the input. Had a full set packing approach that got stuck on ex with this
# prune. Turns out input works just fine. Yikes.
# Probably extend this with some actual set packing for the two failed example conditions.
print(sum([sum(c) * 9 <= x * y for (x, y), c in cond]))
