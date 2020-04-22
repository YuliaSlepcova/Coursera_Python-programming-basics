import sys

user_input = int(sys.argv[1])

for i in range(user_input):
    print(' ' * (user_input - i - 1), "#" * (i + 1), sep='')