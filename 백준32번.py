arr = 0

for i in list(map(int,input().split())):
    arr += i**2

print(arr%10)
