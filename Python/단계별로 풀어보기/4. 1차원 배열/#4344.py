C = int(input())
for i in range(C):
    score = list(map(int, input().split()))
    N = score[0]
    avg = sum(score[1:])/N
    count = 0
    for j in score[1:]:
        if j > avg:
            count += 1
    print("%.3f%%" % (count/N*100))