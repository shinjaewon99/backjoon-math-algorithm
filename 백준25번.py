arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)

arr = set(arr) #중복을 제거

print(len(arr))

