max = 0
maxIndex = 0
for i in range(9):
    number = int(input())
    if number > max:
        max = number
        maxIndex = i + 1

print(max)
print(maxIndex)