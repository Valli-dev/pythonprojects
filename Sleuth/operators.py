import math
a=5
b=-5
c=10
d=8.87
n=int(input("Enter number"))
print("d=", round(d))
print("d=", math.ceil(d))
print("d=", math.floor(d))
print(pow(a,3))
print(abs(b))
print(max(a,b,c))
print(c**5)
print(math.factorial(9))
print(math.gcd(121,143))
print("log=",math.log2(n))
print("cos=",math.cos(n))
print("exp=",math.e**n)
if a >=b :
    print("a is big")
elif a>=c:
    print("a is big than c")
else:
    print("a is smaller than b and c")