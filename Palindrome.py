n=int(input())
temp=n
rev=0
while n>0:
    a=n%10
    rev = rev*10+a
    n=n//10
if temp==rev:
    print("True")
else:
    print("False")