import re
l=eval('['+re.sub(r"(\d+)-(\d+)",r"*range(\1,\2+1)",open(0).read())+']')
[print(sum([e for e in l if re.match(r"^(\d+)\1"+r,str(e))]))for r in["$","+$"]]