N = int(input())

common = ""

for i in range(N):
    fileName = input()
    if i == 0:
        common = fileName
    else:
        for j in range(len(common)):
            if common[j] != fileName[j]:
                common = common[:j] + "?" + common[j+1:]

print(common)