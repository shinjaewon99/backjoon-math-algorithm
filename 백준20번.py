import sys

a = int(input())


for _ in range(a):
    n,m= map(int,sys.stdin.readline().split())
    print(n+m)