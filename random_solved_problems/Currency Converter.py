Sum = float(input())
x = input()
y = input()

BGN = 1
USD = float(1.79549) * BGN
EUR = float(1.95583) * BGN
GBP = float(2.53405) * BGN

e_p = EUR / GBP
u_e = USD / EUR
pr1 = (Sum * USD)
pr2 = f"{pr1:.2f}"
pra1 = (Sum / EUR)
pra12 = f"{pra1:.2f}"
eg_1 = (Sum * e_p)
eg_2 = f"{eg_1:.2f}"
use = (Sum * u_e)
use_2 = f"{use:.2f}"

if x == "USD" and y == "BGN":
    print(f"{pr2} BGN")
elif x == "BGN" and y == "EUR":
    print(f"{pra12} EUR")
elif x == "EUR" and y == "GBP":
    print(f"{eg_2} GBP")
elif x == "USD" and y == "EUR":
    print(f"{use_2} GBP")
