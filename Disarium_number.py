n=int(input())
l=len(str(n))
temp=n
c=0
i=0
while temp>0:
    a=temp%10
    c +=int(a**l)
    temp=temp//10
    l=l-1
if c==n:
    print("True")
else:
    print("False")