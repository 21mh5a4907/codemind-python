n = int(input())
i = 1
count = 0
while i<n:
    if(n%i==0):
         count +=i
         i +=1
    else:
        i = i+1
if count==n:
    print("True")
else:
    print("False")