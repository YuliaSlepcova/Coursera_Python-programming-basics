number = int(input())
n1 = number % 1440
hour = n1 // 60
minute = n1 % 60
print(hour, minute)
