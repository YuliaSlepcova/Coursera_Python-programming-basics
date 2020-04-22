import random

number = []
number_size = random.randint(10, 15)

for _ in range(number_size):
    number.append(random.randint(10, 20))

number.sort()

half_saze = len(number) // 2
mediana = None

if number_size % 2 == 1:
    mediana = number[half_saze]
else:
    mediana = sum(number[half_saze - 1:half_saze + 1]) / 2
print(mediana)


import statistics

print(statistics.median(number))


