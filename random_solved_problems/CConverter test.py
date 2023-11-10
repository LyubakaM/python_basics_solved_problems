Sum = int(input())
x = input()
y = input()

BGN = 1
USD = (1.79549) * BGN
EUR = (1.95583) * BGN
GBP = (2.53405) * BGN

end = 0

e_p = EUR / GBP
u_e = USD / EUR


if x == "USD":
    end = (Sum * USD)
elif x == "BGN":
    end = (Sum / EUR)
elif x == "EUR":
    end = (Sum * e_p)
elif x == "USD":
    end = (Sum * u_e)
if x == "USD":
    end = (Sum * USD)
elif y == "BGN":
    end = (Sum * USD)
elif y == "GBP":
    end = (Sum * e_p)
elif y == "EUR":
    end = (Sum * u_e)



print(f"{end:.2f}")
