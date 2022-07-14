n = int(input())


def gcd(a,b):
    while b !=0:
        r = a%b
        a=b
        b=r
    return a


def lcm(a,b):
    lcm = (a*b) // gcd(a,b)
    return lcm

for i in range(n):
    a,b = map(int,input().split())

    print(lcm(a,b))

# import math 
# a, b = map(int, input().split())
# print(math.gcd(a, b))
# print(math.lcm(a, b))
 