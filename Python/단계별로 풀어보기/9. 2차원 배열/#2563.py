number = int(input())

matrix = []
for i in range(100):
    matrix.append([0] * 100)

for i in range(number):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            matrix[j][k] = 1

count = 0
for i in range(100):
    for j in range(100):
        count += matrix[i][j]

print(count)