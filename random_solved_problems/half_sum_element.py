import sys
n = int(input())
max_number = - sys.maxsize
sum_numbers = 0
for number in range(n):
    numbers = int(input())
    if numbers > max_number:
        max_number = numbers
    sum_numbers += numbers
sum_numbers -= max_number
diff = abs(max_number - sum_numbers)
if max_number == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {diff}")

