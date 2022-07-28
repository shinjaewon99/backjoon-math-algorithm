# 11651번

n = int(input())

arr = []

for i in range(n):
    xy = list(map(int,input().split()))
    arr.append([xy[1],xy[0]])

arr.sort()


for j in arr:
    print(j[1], j[0])