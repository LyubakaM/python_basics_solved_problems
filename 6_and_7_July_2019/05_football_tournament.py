club = input()
games = int(input())
points = 0
w_count = 0
d_count = 0
l_count = 0

if games == 0:
    print(f"{club} hasn't played any games during this season.")
else:
    for game in range(games):
        result = input()
        if result == "W":
            w_count += 1
            points += 3
        elif result == "D":
            d_count += 1
            points += 1
        elif result == "L":
            l_count += 1
    else:
        ave = (w_count / games) * 100
        print(f"{club} has won {points} points during this season.")
        print(f"Total stats:")
        print(f"## W: {w_count}")
        print(f"## D: {d_count}")
        print(f"## L: {l_count}")
        print(f"Win rate: {ave:.2f}%")

