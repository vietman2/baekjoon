l = int(input())

five = l//5
l = l%5
four = l//4
l = l%4
three = l//3
l = l%3
two = l//2
l = l%2

print(five + four + three + two + l)