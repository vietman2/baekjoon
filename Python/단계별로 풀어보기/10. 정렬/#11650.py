import sys

N = int(sys.stdin.readline())

coordinates = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))

coordinates.sort()

for i in range(N):
    print(coordinates[i][0], coordinates[i][1])
