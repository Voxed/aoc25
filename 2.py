import re

r = "^(\\d+)\\1"
l = eval(f"[*range({open(0).read().replace(',','),*range(').replace('-',',')})]")

#1
print(sum([e for e in l if re.match(r+"$",str(e))]))

#2
print(sum([e for e in l if re.match(r+"+$",str(e))]))
