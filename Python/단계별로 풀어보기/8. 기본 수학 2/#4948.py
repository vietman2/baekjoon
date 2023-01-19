def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primeList = [i for i in range(1, 123456*2+1) if isPrime(i)]

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in primeList:
        if n < i <= 2*n:
            count += 1
    print(count)

