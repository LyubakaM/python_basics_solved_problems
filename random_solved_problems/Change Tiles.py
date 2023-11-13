n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())

obshta_pl = n * n
plosht_peika = m * o
plosht_zapokrivane = obshta_pl - plosht_peika
plosht_plochki = w * l
neobhodimi_plochki = plosht_zapokrivane / plosht_plochki
neobhodimo_vreme = neobhodimi_plochki * 0.2

print(round(neobhodimi_plochki, 2))
print(round(neobhodimo_vreme, 2))