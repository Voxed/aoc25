from itertools import combinations
from math import dist, prod
from networkx.utils import UnionFind

pos = [eval(e) for e in open(0)]

# I don't like questions where you have to do this
p1_connections = 10 if len(pos) < 1000 else 1000

nodes = range(0, len(pos))

# Sorted pairs of form [(dist, index1, index2)]
pairs = sorted(zip(
    map(lambda p: dist(*p), combinations(pos, 2)),
    combinations(nodes, 2)))

U = UnionFind(nodes)
# We start out with N disjunct sets
num_sets = len(nodes)

# Join edges
for edges, (d, p) in enumerate(pairs):
    # If the amount of edges reaches p1_connections,
    # we print the product of the length of the 3 largest sets.
    if edges == p1_connections:
        print(prod(sorted(map(len, U.to_sets()), reverse=True)[0:3]))

    # If the junctions are not in the same set, join them
    if U[p[0]] != U[p[1]]:
        num_sets -= 1
        U.union(*p)
        # When the number of sets reach 1, we have joined everything
        if num_sets == 1:
            print(pos[p[0]][0] * pos[p[1]][0])
            break
