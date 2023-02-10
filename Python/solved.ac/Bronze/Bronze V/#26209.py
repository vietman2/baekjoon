values = []
N1, N2, N3, N4, N5, N6, N7, N8 = map(int, input().split())

values.append(N1)
values.append(N2)
values.append(N3)
values.append(N4)
values.append(N5)
values.append(N6)
values.append(N7)
values.append(N8)

for i in range(8):
    if values[i] == 9:
        print("F")
        break
    if i == 7:
        print("S")
