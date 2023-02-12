A, B = map(int, input().split())
a = input()
b = input()

A_set = set(a.split())
B_set = set(b.split())

print(len(A_set ^ B_set))