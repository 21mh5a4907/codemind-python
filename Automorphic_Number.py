n=int(input())
l=len(str(n))
s=n**2
last=s%pow(10,l)
if last==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")