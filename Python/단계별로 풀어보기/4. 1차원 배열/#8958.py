num_testcases = int(input())
for i in range(num_testcases):
    score = input()
    total = 0
    count = 0
    for j in score:
        if j == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)