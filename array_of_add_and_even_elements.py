n = int(input())
a = list(map(int,input().strip().split()))
b = []
c = []
for i in(a):
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
d = c+b
print(*d)