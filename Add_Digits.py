n=int(input())
c=0
c1=0
while n>0:
    a=n%10
    c +=a
    n =n//10
    if n==0 and c>9:
        n=c
        c=0
print(c)
    