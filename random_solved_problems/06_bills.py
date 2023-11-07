k_num = int(input())
l_num = int(input())
m_num = int(input())
n_num = int(input())

counter = 0
counter2 = 0
for x in range(k_num, 8 + 1):
    if x % 2 == 0:
        for y in range(9, l_num - 1, -1):
            if y % 2 != 0:
                for z in range(m_num, 8 + 1):
                    if z % 2 == 0:
                        for i in range(9, n_num - 1, -1):
                            if i % 2 != 0:
                                first_number = x * 10 + y
                                second_number = z * 10 + i
                                if first_number != second_number:
                                    print(f"{x}{y} - {z}{i}")
                                    counter += 1
                                if first_number == second_number:
                                    print("Cannot change the same player.")
