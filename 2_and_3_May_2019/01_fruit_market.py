straw_price = float(input())
banana_kg = float(input())
oranges_kg = float(input())
rasp_kg = float(input())
straw_kg = float(input())

rasp_price = (straw_price * 0.5)
orange_price = (rasp_price * 0.6)
banana_price = (rasp_price * 0.2)

straw_sum = straw_kg * straw_price
rasp_sum = rasp_kg * rasp_price
orange_sum = oranges_kg * orange_price
banana_sum = banana_kg * banana_price
sum_all = straw_sum + rasp_sum + orange_sum + banana_sum
print(f"{sum_all:.2f}")
