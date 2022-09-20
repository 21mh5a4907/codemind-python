def gcd(a, b):
  
  result = min(a, b)
   
  while result:
    if a % result == 0 and b % result == 0:
      break
    result -= 1
  return result
a,b=map(int,input().split())
 
print(gcd(a, b))