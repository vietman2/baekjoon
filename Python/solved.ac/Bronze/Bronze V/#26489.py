numLines = 0

while True:
    try:
        input()
        numLines += 1
    except EOFError:
        break

print(numLines)
