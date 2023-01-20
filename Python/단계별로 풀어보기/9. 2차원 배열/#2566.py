for i in range(9):
    if i == 0:
        matrix = [list(map(int, input().split()))]
    else:
        matrix.append(list(map(int, input().split())))

max_num = 0
max_i = 0
max_j = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]
            max_i = i
            max_j = j
            
print(max_num)
print(max_i + 1, max_j + 1)