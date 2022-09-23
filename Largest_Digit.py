n=int(input())
v=[]
while n>0:
    a=n%10
    v.append(a)
    n=n//10
print(max(v))