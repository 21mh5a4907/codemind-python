n = int(input())
l = list(map(int,input().strip().split()))
b=[]
c=0
for i in(l):
    if i not in b and i%2!=0:
        c +=1
        b.append(i)
print(c)
