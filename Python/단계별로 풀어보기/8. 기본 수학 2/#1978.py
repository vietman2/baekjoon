N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
for i in map(int, input().split()):
    if is_prime(i):
        count += 1
print(count)
