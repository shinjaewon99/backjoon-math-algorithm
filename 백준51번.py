# 2292번

n =int(input())

nums =1
count =1

while n >nums:
    nums += 6 * count
    count +=1
print(count)