from numpy import*
b,l=[[*map(int,e.strip())]for e in open(0)],lambda b,n:0 if n<0 else b[i:=argmax(b[:len(b)-n])]*10**n+l(b[i+1:],n-1)
[print(sum([l(b,i)for b in b]))for i in[1,11]]