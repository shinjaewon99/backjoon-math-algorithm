# 4153번
while True :
  a, b, c = map(int, input().split())
  
  if a==0 and b==0 and c==0 :
    break
  
  a *= a
  b *= b
  c *= c
  if a+b == c or a+c == b or b+c == a :
    print("right")
  else :
    print("wrong")


