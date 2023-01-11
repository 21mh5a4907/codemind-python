def vc(s):
    c=0
    for i in s:
        if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
            c+=1
    return c
s=input()
k=s.split()
v=[]
for i in k:
    v.append(vc(i))
print(min(v))