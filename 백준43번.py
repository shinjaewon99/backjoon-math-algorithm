n , m = map(int,input().split())

people= list(map(int,input().split()))

total = n*m

for i in people:
    print(i-total)

    