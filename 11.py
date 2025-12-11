import networkx as nx
from functools import cache

l = [
    e.strip()
    for e in open(0)
]

G = nx.DiGraph()
for r in l:
    G.add_node(r.split(':')[0])

for r in l:
    n = r.split(':')[0]
    others = r.split(':')[1][1:].split()
    for o in others:
        G.add_edge(n, o)

@cache
def num_paths(f, t):
    if f == t:
        return 1
    count = 0
    for v in G.neighbors(f):
        count += num_paths(v, t)
    return count

svr_to_dac = num_paths('svr', 'dac')
svr_to_fft = num_paths('svr', 'fft')
dac_to_fft = num_paths('dac', 'fft')
fft_to_dac = num_paths('fft', 'dac')
dac_to_out = num_paths('dac', 'out')
fft_to_out = num_paths('fft', 'out')

print(svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out)