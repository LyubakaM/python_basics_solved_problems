n = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others = 0

for names in range(n):
    name = input()
    if name == "Hearthstone":
        hearthstone_count += 1
    elif name == "Fornite":
        fornite_count += 1
    elif name == "Overwatch":
        overwatch_count += 1
    else:
        others += 1
hsp = hearthstone_count / n * 100
fp = fornite_count / n * 100
op = overwatch_count / n * 100
other_p = others / n * 100


print(f"Hearthstone - {hsp:.2f}%")
print(f"Fornite - {fp:.2f}%")
print(f"Overwatch - {op:.2f}%")
print(f"Others - {other_p:.2f}%")