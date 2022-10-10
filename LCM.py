n,m=map(int,input().split())
i=max(n,m)
while True:
    if i%n==0 and i%m==0:
        print(i)
        break
    i+=1