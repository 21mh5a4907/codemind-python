a=int(input())
n=list(map(int, input().strip().split()))
avg = sum(n)//len(n)
c=0
for i in(n):
    if i>=avg:
        c +=1
    else:
        i +=1
print(c)
