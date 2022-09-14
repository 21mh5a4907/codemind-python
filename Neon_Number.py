n = int(input())
a=n*n
o=[int(x) for x in str(a)]
if sum(o)==n:
    print("Neon Number")
else:
    print("Not Neon Number")