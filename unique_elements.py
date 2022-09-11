n = int(input())
l = list(map(int,input().strip().split()))
c=0
d=[]
for i in(l):
    if i not in d:
        d.append(i)
        print(i,end=' ')
    