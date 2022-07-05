a = int(input())
total = 0


while a >= 0:
    if a % 5 == 0:
        total +=a//5
        print(total)
        break
    a -=3
    total+=1
 

else:
    print(-1)



