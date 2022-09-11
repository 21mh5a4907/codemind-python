n = int(input())
l = list(map(int,input().strip().split()))
b = sum(l)//len(l)
c=0
for i in(l):
    if i<=b:
        c +=1
    else:
        i +=1
print(c)