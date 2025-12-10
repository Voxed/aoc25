import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from itertools import product, count

# Parse the machines
machines = [
    (
        # Parse indicator requirements
        tuple(e == '#' for e in m[0][1:-1]),

        # Parse buttons
        [eval(e.replace(')', ',)')) for e in m[1:-1]],

        # Parse joltage requirements
        list(map(int, m[-1][1:-1].split(',')))
    )
    for m in [e.strip().split(' ') for e in open(0)]]

# Breadth first search
part1 = 0
for (req_indicators, buttons, _) in machines:
    states = set([tuple(False for _ in req_indicators)])
    for i in count(1):
        new_states = set()
        for state, button in product(states, buttons):
            new_state = tuple(
                indicator ^ (i in button)
                for i, indicator in enumerate(state)
            )
            new_states.add(new_state)
            if new_state == req_indicators:
                break
        else:
            states = new_states
            continue
        break
    part1 += i
print(part1)

# Mixed integer linear programming
part2 = 0
for (_, buttons, joltage_req) in machines:
    eqs = [
        [1 if i in b else 0 for b in buttons]
        for i in range(len(joltage_req))
    ]
    num_variables = len(buttons)
    result = milp(c=np.ones(num_variables),
                  constraints=LinearConstraint(eqs, joltage_req, joltage_req),
                  bounds=Bounds(0, np.inf),
                  integrality=np.ones(num_variables, dtype=int))
    part2 += result.fun
print(int(part2))
