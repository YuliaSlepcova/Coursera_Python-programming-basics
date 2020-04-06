rubl = int(input())
kopeck = int(input())
count = int(input())
count_rubl = rubl * count
count_kopeck = (kopeck % 100) * count
final_kopeck = count_kopeck % 100
count_kopeck_rubl = count_kopeck // 100
final_rubl = count_rubl + count_kopeck_rubl
print(final_rubl, final_kopeck)
