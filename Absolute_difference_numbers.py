n,x=map(int,input().split())
m=list(map(int,str(n)))
a=m[-x:]
b=m[:x]
s = [str(i) for i in a]
res=int("".join(s))
t = [str(i) for i in b]
r=int("".join(t))
print(abs(r-res))
