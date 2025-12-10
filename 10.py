from collections import namedtuple
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from itertools import count

Machine = namedtuple('Machine', ('indicators', 'buttons', 'joltage'))
machines = []

l = [e.strip().split(' ') for e in open(0)]
for m in l:
    indicators = tuple(e == '#' for e in m[0][1:-1])
    buttons = [eval(e.replace(')', ',)')) for e in m[1:-1]]
    joltages = list(map(int, m[-1][1:-1].split(',')))
    machines.append(Machine(indicators, buttons, joltages))

# Breadth first search
part1 = 0
for m in machines:
    states = set([tuple(False for _ in m.indicators)])
    for i in count(1):
        found_solution = False
        new_states = set()
        for state in states:
            for button in m.buttons:
                new_state = tuple(indicator ^ (i in button) for i, indicator in enumerate(state))
                new_states.add(new_state)
                if new_state == m.indicators:
                    found_solution = True
        if found_solution:
            break
        states = new_states
    part1 += i
print(part1)

# Mixed integer linear programming
part2 = 0
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

    part2 += result.fun
print(int(part2))
