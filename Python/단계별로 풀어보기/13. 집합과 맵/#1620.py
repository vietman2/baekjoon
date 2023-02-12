import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for i in range(N):
    name = input().rstrip()
    dic[name] = i+1
    dic[str(i+1)] = name

for _ in range(M):
    print(dic[input().rstrip()])