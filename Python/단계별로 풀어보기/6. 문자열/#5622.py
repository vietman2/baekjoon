input = input()
time = 0
for i in range(len(input)):
    if input[i] in ['A', 'B', 'C']:
        time += 3
    elif input[i] in ['D', 'E', 'F']:
        time += 4
    elif input[i] in ['G', 'H', 'I']:
        time += 5
    elif input[i] in ['J', 'K', 'L']:
        time += 6
    elif input[i] in ['M', 'N', 'O']:
        time += 7
    elif input[i] in ['P', 'Q', 'R', 'S']:
        time += 8
    elif input[i] in ['T', 'U', 'V']:
        time += 9
    elif input[i] in ['W', 'X', 'Y', 'Z']:
        time += 10

print(time)