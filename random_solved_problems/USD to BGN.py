nailon = 1.50
boq = 14.50
raz = 5.00


nailon2 = int(input())
boq2 = int(input())
raz2 = int(input())
maistor = int(input())

x = (nailon2 + 2) * 1.50
y = boq2 * 14.50 + (boq2 * 14.50)*0.10
z = raz2 * 5
material_all = x + y + z + 0.40

maistor_rabota = (material_all * 0.3) * maistor
total = maistor_rabota + material_all
print(total)



