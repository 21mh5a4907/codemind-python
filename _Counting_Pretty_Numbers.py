for i in range(int(input())):
    l,r=map(int,input().split())
    c=0
    for j in range(l,r+1):
        if j%10==2 or j%10==3 or j%10==9:
            c +=1
        else:
            j +=1
    print(c)