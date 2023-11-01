first_match_result = input()
second_match_result = input()
third_match_result = input()

res1 = int(first_match_result[0])
res2 = int(first_match_result[2])
w = 0
d = 0
loss = 0
if res1 > res2:
    w += 1
elif res1 == res2:
    d += 1
else:
    loss += 1
res21 = int(second_match_result[0])
res22 = int(second_match_result[2])
if res21 > res22:
    w += 1
elif res21 == res22:
    d += 1
else:
    loss += 1
res31 = int(third_match_result[0])
res32 = int(third_match_result[2])
if res31 > res32:
    w += 1
elif res31 == res32:
    d += 1
else:
    loss += 1
print(f"Team won {w} games.")
print(f"Team lost {loss} games.")
print(f" Drawn games: {d}")
