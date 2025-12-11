from functools import cache

# Parse graph into dictionary of node -> [node]
G = {
    e[0]: e[1].split()
    for e in [e.split(': ') for e in open(0)]
}

# Number of paths from f -> t
def P(f, t):
    @cache
    def r(f):
        return 1 if f == t else sum(map(r, G.get(f, [])))
    return r(f)

# Part 1
print(P('you', 'out'))

# Part 2
print(
    # svr -> dac -> fft -> out
    P('svr', 'dac') *
    P('dac', 'fft') *
    P('fft', 'out') +
    # svr -> fft -> dac -> out
    P('svr', 'fft') *
    P('fft', 'dac') *
    P('dac', 'out')
)
