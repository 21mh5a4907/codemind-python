n = int(input())
l = list(map(int,input().strip().split()))
res = int("".join(str(x) for x in l), 2)
print(res)