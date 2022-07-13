burger = []


for i in range(3):
    burger.append(int(input()))


drink = []

for j in range(2):
    drink.append(int(input()))


min = min(burger) + min(drink) -50

print (min)