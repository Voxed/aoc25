import numpy as np
import re

l = np.concat([range(int((f := e.split('-'))[0]), int(f[1])+1) for e in open(0).read().split(',')])
print(np.sum([e for e in l if re.match("^(\\d+)\\1$", str(e))]))
print(np.sum([e for e in l if re.match("^(\\d+)\\1+$", str(e))]))
