men_number = int(input())
women_number = int(input())
max_tables = int(input())
seats = max_tables * 2

for male_clients in range(1, men_number + 1):
    for female_clients in range(1, women_number + 1):
        if seats > 0:
            seats -= 2
            print(f"({male_clients} <-> {female_clients})", end=" ")
        else:
            break