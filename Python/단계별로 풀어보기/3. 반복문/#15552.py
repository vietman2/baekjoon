import sys

T = int(input())

for i in range(0,T):
    A, B = sys.stdin.readline().split()
    print(int(A) + int(B))