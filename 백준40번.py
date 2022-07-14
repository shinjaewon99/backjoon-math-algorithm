n = int(input())
arr = [64,32,16,8,4,2,1]
count = 0

for i in arr:
    while n -i>= 0:
        n -= i
        count += 1
print(count)