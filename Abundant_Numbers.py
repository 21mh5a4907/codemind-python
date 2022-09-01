n = int(input())
count = 0
i = 1
while i<n:
    if n%i==0:
        count +=i
        i +=1
    else:
        i +=1
if count>n:
    print("True")
else:
    print("False")
        
    