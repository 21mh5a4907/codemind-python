n = int(input())
l = list(map(int,input().strip().split()))
k = int(input())
c=0
for i in(l):
    if i==k:
        c +=i
        break
    else:
        c +=i
print(c)