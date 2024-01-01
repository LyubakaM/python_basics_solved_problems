groups_counter = int(input())
musala = 0
monblan = 0
kiliman = 0
k2 = 0
everest = 0
climbers_count = 0
for climbers in range(1, groups_counter + 1):
    people_in_group = int(input())
    climbers_count += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kiliman += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group
dat_musala = (musala / climbers_count) * 100
dat_monblan = (monblan / climbers_count) * 100
dat_kiliman = (kiliman / climbers_count) * 100
dat_k2 = (k2 / climbers_count) * 100
dat_everest = (everest / climbers_count) * 100

print(f"{dat_musala:.2f}%")
print(f"{dat_monblan:.2f}%")
print(f"{dat_kiliman:.2f}%")
print(f"{dat_k2:.2f}%")
print(f"{dat_everest:.2f}%")
