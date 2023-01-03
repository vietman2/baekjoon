num_testcases = int(input())
for i in range(num_testcases):
    num, string = input().split()
    for j in string:
        print(j * int(num), end='')
    print()
