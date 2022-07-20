

arr =[]

for i in range(10):
    

    arr.append(int(input()))
print(int(sum(arr)/10))


x = list(set(arr))
arry = []

for i in range(len(x)):
    arry.append(arr.count(x[i]))

print(x[arry.index(max(arry))])



    



