number_one_max = int(input())
number_two_max = int(input())
number_three_max = int(input())

for num1 in range(1, number_one_max + 1):
    for num2 in range(1, number_two_max + 1):
        for num3 in range(1, number_three_max + 1):
            if num1 % 2 == 0 and num3 % 2 == 0 and num2 in [2, 3, 5, 7]:
                print(f"{num1} {num2} {num3}")
