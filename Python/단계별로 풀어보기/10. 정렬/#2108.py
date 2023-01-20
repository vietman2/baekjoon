import sys

N = int(sys.stdin.readline())

arr = []
app = [0] * 8001

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    app[arr[i] + 4000] += 1

arr.sort()

print(round(sum(arr) / N))
print(arr[N // 2])
print(app.index(max(app)) - 4000 if app.count(max(app)) == 1 else app[app.index(max(app)) + 1:].index(max(app[app.index(max(app)) + 1:])) + app.index(max(app)) + 1 - 4000)
print(arr[-1] - arr[0])