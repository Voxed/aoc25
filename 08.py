import numpy as np
from itertools import combinations
import math
import networkx as nx
from networkx.utils import UnionFind

l = [list(map(int,e.strip().split(','))) for e in open(0)]

p1_connections = 10 if len(l) < 1000 else 1000

nodes = range(0, len(l))
indices = combinations(nodes, 2)
distances = map(lambda p: math.dist(*p), combinations(l, 2))

pairs = list(zip(distances, indices))
pairs.sort()

U = UnionFind(nodes)
G = nx.Graph()
num_components = len(nodes)
for n in nodes:
    G.add_node(n)
for (d, (p1, p2)) in pairs:
    if p2 not in nx.neighbors(G, p1):
        G.add_edge(p1, p2)
        if len(G.edges) == p1_connections:
            components = sorted(map(len, U.to_sets()), reverse=True)
            print(np.prod(components[0:3]))
        if U[p1] != U[p2]:
            num_components -= 1
            U.union(p1, p2)
            if num_components == 1:
                print(l[p1][0] * l[p2][0])
                break