n = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                first_second = first + second
                third_fourth = third + fourth
                last_condition = n % first_second == 0
                if first_second == third_fourth and last_condition:
                    print(f"{first}{second}{third}{fourth}", end=" ")