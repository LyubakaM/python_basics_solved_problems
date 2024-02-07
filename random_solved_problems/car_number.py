starting_num = int(input())
end_num = int(input())

for first in range(starting_num, end_num + 1):
    for second in range(starting_num, end_num + 1):
        for third in range(starting_num, end_num + 1):
            for fourth in range(starting_num, end_num + 1):
                if (first % 2 == 0 and fourth % 2 != 0) or (first % 2 != 0 and fourth % 2 == 0):
                    if first > fourth:
                        result = second + third
                        if result % 2 == 0:
                            print(f"{first}{second}{third}{fourth}", end=" ")