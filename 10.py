from collections import namedtuple
from functools import cache
import sympy as sp
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

Machine = namedtuple('Machine', ('indicators', 'buttons', 'joltage'))
machines = []

l = [e.strip() for e in open(0)]
for m in l:
    wiring_index = m.index('(') - 1
    joltage_index = m.index('{') - 1
    indicator = tuple(m == '#' for m in list(m[1:wiring_index-1]))
    wiring = eval(m[wiring_index+1:joltage_index].replace(' ', ',').replace(')', ',)'))
    joltage = eval(m[joltage_index:].replace('{', '(').replace('}', ')'))
    machines.append(Machine(indicator, wiring, joltage))
    
ss = 0
for m in machines:
   
    N = len(m.joltage)
    V = len(m.buttons)
    eqs = []
    for i, jolt in enumerate(m.joltage):
        coefficients = []
        for j, b in enumerate(m.buttons):
            coefficients.append(1 if i in b else 0)
        eqs.append(coefficients)

    num_variables = len(m.buttons)
    result = milp(c=np.ones(num_variables), 
                constraints=LinearConstraint(eqs, m.joltage, m.joltage), # m.joltage <= coefficients * variables <= m.joltage
                bounds=Bounds(0, np.inf), 
                integrality=np.ones(num_variables, dtype=int))

    ss += result.fun

print(int(ss))
