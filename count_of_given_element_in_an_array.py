n = int(input())
a = list(map(int,input().strip().split()))
z = int(input())
c=0
for i in(a):
    if i==z:
        c +=1
    else:
        i +=1
print(c)