import numpy as np



l = [l[:-1] for l in open(0)]
am = len(l[-1].split())

t = np.array([list(e) for e in l[:-1]]).transpose()
#t = t[np.mod(np.arange(t.shape[0]),4)!=3]
nn=np.array([ 0 if ''.join(l).strip() == '' else int(''.join(l)) for l in t] + [0])

numsnew = []
x = []
for v in nn:
    if v == 0:
        numsnew.append(x)
        x = []
    else:
        x.append(int(v))

print(numsnew)


ops = []
nums = []
for li in l:
    if li.startswith('*') or li.startswith('+'):
        ops = li.split()
    else:
        for i, k in enumerate(li.split()):
            if i >= len(nums):
                nums.append([])
            nums[i].append(k)



'''
n2 = []
for i in nums:
    n2.append([])
for j,n in enumerate(nums):
    longest = max([len(n) for n in n])
    pn = [n.ljust(longest, '0') for n in n]
    for i, _ in enumerate(pn[0]):
        for n in reversed(pn):
            if len(n2[j]) <= i:
                n2[j].append("")
            n2[j][i] = n[i] + n2[j][i]

    print(pn)
print(n2)
'''
print(numsnew)
sum = 0
for i,n in enumerate(numsnew):
    if ops[i] == '*':
        sum += np.prod(np.array(n, dtype=int))
    else:
        sum += np.sum(np.array(n, dtype=int))
print(sum)