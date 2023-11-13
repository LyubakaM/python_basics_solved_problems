screening_type = input()
rows = int(input())
cols = int(input())

tickets = rows * cols
profit = 0

if screening_type == "Premiere":
    profit += tickets * 12.00
elif screening_type == "Normal":
    profit += tickets * 7.50
elif screening_type == "Discount":
    profit += tickets * 5.00

print(f"{profit} leva")

