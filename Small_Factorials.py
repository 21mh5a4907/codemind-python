for i in range(int(input())):
    n = int(input())
    count = 1
    for i in range(1,n+1):
        count = count*i
        i = i+1
    print(count,end ='
')
    