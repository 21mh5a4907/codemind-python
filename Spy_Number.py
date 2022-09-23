n=int(input())
c=0
c1=1
while n>0:
    a=n%10
    c +=a
    c1 = c1*a
    n=n//10
if c==c1:
    print("Spy Number")
else:
    print("Not Spy Number")