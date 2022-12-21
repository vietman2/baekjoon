hour, minute = input().split()

if int(minute) < 45:
    hour = int(hour) - 1
    minute = int(minute) + 60 - 45
    if hour < 0:
        hour = 23
else:
    minute = int(minute) - 45

print(hour, minute)