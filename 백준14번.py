

n = int(input())

num = n
new_num = 0
temp = 0 
count = 0

while True:
   temp = num // 10 + num%10
   new_num =(num%10)*10 + temp%10
   count += 1
   if(num == n):
        break

print(count)
