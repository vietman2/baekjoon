def recursion(line, l, r):
    global numCalls
    numCalls += 1

    if(l >= r):
        return 1
    elif(line[l] == line[r]):
        return recursion(line, l+1, r-1)
    else:
        return 0

def isPalindrome(line):
    return recursion(line, 0, len(line)-1)

n = int(input())
for i in range(n):
    line = input()
    numCalls = 0
    print(isPalindrome(line), numCalls)
