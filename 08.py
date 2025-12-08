from itertools import combinations
import math
from networkx.utils import UnionFind

pos = [eval(e) for e in open(0)]
p1_connections = 10 if len(pos) < 1000 else 1000
nodes = range(0, len(pos))
pairs = sorted(zip(
    map(lambda p: math.dist(*p), combinations(pos, 2)),
    combinations(nodes, 2)))

U = UnionFind(nodes)
num_components = len(nodes)
for edges, (d, p) in enumerate(pairs):
    if edges == p1_connections:
        print(math.prod(sorted(map(len, U.to_sets()), reverse=True)[0:3]))
    if U[p[0]] != U[p[1]]:
        num_components -= 1
        U.union(*p)
        if num_components == 1:
            print(pos[p[0]][0] * pos[p[1]][0])
            break
