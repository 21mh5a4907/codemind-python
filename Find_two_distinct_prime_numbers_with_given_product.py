def pr(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
v=[]
for i in range(2,n+1):
    for j in range(2,i+1):
        if pr(j)==True and pr(i)==True and j*i==n:
            v.append(j)
            v.append(i)
            break
if len(v)==0:
    print(-1)
else:
    print(*v)