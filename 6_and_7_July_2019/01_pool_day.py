import math

hora = int(input())
vhod = float(input())
slong = float(input())
umb = float(input())
a = hora * vhod
b = math.ceil(hora * 0.75) * slong
c = math.ceil(hora * 0.50) * umb
total = (a + b + c)
print("%.2f" %(total) + " lv.")