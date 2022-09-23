n=int(input())
c=0
c1=0
while n>0:
    a=n%10
    if a%2==0:
        c +=1
    else:
        c1 +=1
    n=n//10
if c!=0 and c1!=0:
    print("Mixed")
elif c==0:
    print("Odd")
else:
    print("Even")
    