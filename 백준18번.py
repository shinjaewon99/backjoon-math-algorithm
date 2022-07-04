list = int(input())

for list in range(1, list+1):  
    A, B = map(int, input().split())
    print(f'Case #{list}: {A} + {B} = {A+B}')