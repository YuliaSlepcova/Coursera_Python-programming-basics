import sys

user_string = sys.argv[1]
sum = 0
for i in range(0, len(user_string)):
   
    sum = int(user_string[i]) + sum
    i += 1
print(sum)