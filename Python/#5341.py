def numBlocks(n):
    if n == 1:
        return 1
    else:
        return numBlocks(n-1) + n

while True:
    n = int(input())
    if n == 0:
        break
    print(numBlocks(n))
