list = []
for i in range(30):
    list.append(i+1)

for i in range(28):
    num = int(input())
    list.remove(num)

for i in list:
    print(i)