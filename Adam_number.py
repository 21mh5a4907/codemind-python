n=int(input())
rev=0
r1=0
a=n*n
while n>0:
    b=n%10
    rev=rev*10+b
    n=n//10
c=rev*rev
while c>0:
    d=c%10
    r1=r1*10+d
    c=c//10
if r1==a:
    print("True")
else:
    print("False")