import sys
from collections import deque

queue=deque([])
N=int(sys.stdin.readline())

for i in range(N):
    queue.append(i+1)

while len(queue)>1:
    queue.popleft()
    if (len(queue)>1):
        queue.append(queue.popleft())
    else:
        break
print(queue.popleft())