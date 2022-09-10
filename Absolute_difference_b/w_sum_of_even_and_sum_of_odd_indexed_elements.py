n = int(input())
l = list(map(int,input().strip().split()))
a=0
b=0
for index, i in enumerate(l):
    if index%2==0:
        a +=i
    else:
        b +=i
print(a-b)