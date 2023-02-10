N = int(input())

for _ in range(N):
    password = input()
    if(len(password) < 6 or len(password) > 9):
        print("no")
        continue
    else:
        print("yes")