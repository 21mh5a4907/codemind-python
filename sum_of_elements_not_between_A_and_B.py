n = int(input())
l = list(map(int,input().strip().split()))
a,b = map(int,input().split())
c=0
for i in(l):
    if i>=a and i<=b:
        i +=1
    else:
        c +=i
print(c)
    