num = int(input())

for _ in range(num):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    
    count = 0
    for i in score[1:]:
        if i > avg:
            count += 1
            
    per = (count/score[0])*100
    print('%.3f' %per + '%')