from re import*
[i]=open(0)
[print(sum(e for e in eval(f"[{sub(r"(\d+)-(\d+)",r"*range(\1,\2+1)",i)}]") if match(r"(\d+)\1"+r,str(e))))for r in["$","+$"]]