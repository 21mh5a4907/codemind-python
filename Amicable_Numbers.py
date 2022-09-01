n = int(input())
m = int(input())
c = 0
c1 = 0
for i in range(1,n):
    if n%i==0:
        c +=i
        i +=1
    else:
        i +=1
for a in range(1,m):
    if m%a==0:
        c1 +=a
        a +=1
if(c == m and c1 == n):
    print("Amicable")
else:
    print("Not Amicable")
        