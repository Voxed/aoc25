from collections import namedtuple
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

Machine = namedtuple('Machine', ('indicators', 'buttons', 'joltage'))
machines = []

l = [e.strip().split(' ') for e in open(0)]
for m in l:
    indicators = [e == '#' for e in m[0][1:-1]]
    buttons = [eval(e.replace(')', ',)')) for e in m[1:-1]]
    joltages = list(map(int, m[-1][1:-1].split(',')))
    machines.append(Machine(indicators, buttons, joltages))

ss = 0
for m in machines:
    eqs = [
        [1 if i in b else 0 for b in m.buttons]
        for i in range(len(m.joltage))
    ]
    num_variables = len(m.buttons)
    result = milp(c=np.ones(num_variables), 
                constraints=LinearConstraint(eqs, m.joltage, m.joltage), # m.joltage <= coefficients * variables <= m.joltage
                bounds=Bounds(0, np.inf), 
                integrality=np.ones(num_variables, dtype=int))

    ss += result.fun

print(int(ss))
