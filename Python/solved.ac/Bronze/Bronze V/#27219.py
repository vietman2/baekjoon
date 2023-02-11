num = int(input())

Vs = num//5
Is = num%5

line = ""

for i in range(Vs):
    line += "V"

for i in range(Is):
    line += "I"

print(line)