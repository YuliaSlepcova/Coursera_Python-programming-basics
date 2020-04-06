distance_24_hours = int(input())
distance_total = int(input())
count_day = (((distance_total * 24 // distance_24_hours) + 23)) // 24
print(count_day)
