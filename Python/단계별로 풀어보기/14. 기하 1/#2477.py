K = int(input())

heights = []
widths = []
totals = []

for i in range(6):
    direction, length = map(int, input().split())
    totals.append(length)
    if direction == 1 or direction == 2:
        heights.append(length)
    else:
        widths.append(length)

area = max(heights) * max(widths)

heightIndex = totals.index(max(heights))
widthIndex = totals.index(max(widths))

small1 = abs(totals[heightIndex-1] - totals[((heightIndex+1) % 6)])
small2 = abs(totals[widthIndex-1] - totals[((widthIndex+1) % 6)])

print((area - small1 * small2) * K)