import numpy as np
from itertools import product
import math
import networkx as nx

l = [list(map(int,e.strip().split(','))) for e in open(0)]

smallest_pairs = []
for i, (x1,y1,z1) in enumerate(l):
    for j, (x2,y2,z2) in enumerate(l):
        if i != j:
            di = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2,2) + math.pow(z1-z2,2))
            smallest_pairs.append((di, i, j))
smallest_pairs.sort()

G = nx.Graph()

units = {}
nunits = 0
connections = 0
for i, j in enumerate(l):
    G.add_node(i)
for (d, p1, p2) in smallest_pairs:
    if p2 not in nx.neighbors(G, p1):
        G.add_edge(p1, p2)
        connections += 1
        if sorted(map(len, nx.connected_components(G)), reverse=True)[0] == 1000:
            print(l[p1][0]* l[p2][0])
            break

sizes = list(map(len, list(nx.connected_components(G))))
sizes.sort()
sizes = list(reversed(sizes))
print(sizes)
print(sizes[0] * sizes[1] * sizes[2])