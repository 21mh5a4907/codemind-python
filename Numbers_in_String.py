str=input()
sum=0
for i in str:
    if i.isdigit():
        sum=sum+int(i)
print(sum)