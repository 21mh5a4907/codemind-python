n = int(input())
l = list(map(int,input().strip().split()))
a,b=map(int,input().split())
c=0
for i in(l):
    if i>=a and i<=b:
        c +=i
    else:
        i +=1
print(c)