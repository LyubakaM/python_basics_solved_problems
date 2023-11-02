
first = int(input())
second = int(input())

first_str = str(first)
second_str = str(second)

for x in range(int(first_str[0]), int(second_str[0]) + 1):
    for y in range(int(first_str[1]), int(second_str[1]) + 1):
        for z in range(int(first_str[2]), int(second_str[2]) + 1):
            for q in range(int(first_str[3]), int(second_str[3]) + 1):
                if x % 2 != 0 and y % 2 != 0 and z % 2 != 0 and q % 2 != 0:
                    print(f"{x}{y}{z}{q}", end=" ")