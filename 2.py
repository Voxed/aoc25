import re
b='*range('
l=eval(f"[{b}{open(0).read().replace(',','+1),'+b).replace('-',',')}+1)]")
[print(sum([e for e in l if re.match("^(\\d+)\\1"+r,str(e))]))for r in["$","+$"]]