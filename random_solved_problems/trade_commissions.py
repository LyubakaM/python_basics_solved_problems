city = input()
sales_volume = float(input())
result = 0
FALSE_DATA = False



if city == "Sofia":
    if 0 <= sales_volume <= 500:
        result = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        result = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        result = sales_volume * 0.08
    elif sales_volume > 10000:
        result = sales_volume * 0.12
    else:
        FALSE_DATA = True
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        result = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        result = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        result = sales_volume * 0.1
    elif sales_volume > 10000:
        result = sales_volume * 0.13
    else:
        FALSE_DATA = True

elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        result = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        result = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        result = sales_volume * 0.12
    elif sales_volume > 10000:
        result = sales_volume * 0.145
    else:
        FALSE_DATA = True
else:
    FALSE_DATA = True

if not FALSE_DATA:
    print(f"{result:.2f}")
else:
    print("error")








