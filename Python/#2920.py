list = list(map(int, input().split()))

state = ""

for i in range (1, list.__len__()):
    if i == 1:
        if list[i] > list[i-1]:
            state = "ascending"
        elif list[i] < list[i-1]:
            state = "descending"
        else:
            state = "mixed"
            break
    else:
        if list[i] > list[i-1] and state == "ascending":
            continue
        elif list[i] < list[i-1] and state == "descending":
            continue
        else:
            state = "mixed"
            break

print(state)