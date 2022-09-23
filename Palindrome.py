m=int(input())
temp=m
rev=0
while m>0:
    a=m%10
    rev = rev*10+a
    m=m//10
if rev==temp:
    print("True")
else:
    print("False")