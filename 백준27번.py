a = int(input())

result = 1

if a > 0:
    for i in range(1,a+1):
        result *= i

print(result)

# import math 활용

import math

print(math.factorial(int(input())))