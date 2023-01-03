N = int(input())
count = 0

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                break
    else:
        count += 1

print(count)