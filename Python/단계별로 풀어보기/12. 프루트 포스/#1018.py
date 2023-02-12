N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

min_count = 64
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] == 'B':
                        count += 1
                else:
                    if board[k][l] == 'W':
                        count += 1
        min_count = min(min_count, count, 64-count)

print(min_count)