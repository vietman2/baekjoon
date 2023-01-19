T = int(input())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    if n == 4:
        return '2 2'
    if n % 2 == 0:
        for i in range(n//2, n):
            if isPrime(n-i) and isPrime(i):
                return f'{n-i} {i}'
    return 'Goldbach\'s conjecture is wrong.'

for _ in range(T):
    n = int(input())
    print(goldbach(n))