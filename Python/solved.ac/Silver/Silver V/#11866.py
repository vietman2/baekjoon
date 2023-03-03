N, K = map(int, input().split())

queue = [i for i in range(1, N + 1)]
answer = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.pop(0))
    answer.append(queue.pop(0))

print('<' + ', '.join(map(str, answer)) + '>')
