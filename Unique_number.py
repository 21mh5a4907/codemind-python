my_int = int(input())
my_list = [int(x) for x in str(my_int)]
l=[]
for i in(my_list):
    if i not in(l):
        l.append(i)
if len(l)==len(my_list):
    print("Unique Number")
else:
    print("Not Unique Number")
    