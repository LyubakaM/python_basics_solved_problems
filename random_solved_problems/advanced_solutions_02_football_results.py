first_match = input()
second_match = input()
third_match = input()

win = 0
loss = 0
draw = 0

first_res = int(first_match[0])
first_res_2 = int(first_match[2])
second_res = int(second_match[0])
second_res_2 = int(second_match[2])
third_res = int(third_match[0])
third_res_2 = int(third_match[2])

if first_res > first_res_2:
    win += 1
elif first_res == first_res_2:
    draw += 1
else:
    loss += 1
if second_res > second_res_2:
    win += 1
elif second_res == second_res_2:
    draw += 1
else:
    loss += 1
if third_res > third_res_2:
    win += 1
elif third_res == third_res_2:
    draw += 1
else:
    loss += 1

print(f"Team won {win} games.")
print(f"Team lost {loss} games.")
print(f"Drawn games: {draw}")


# first_match = input()
# second_match = input()
# third_match = input()


# first_res, first_res_2 = (first_match[0]),  (first_match[2])
# second_res, second_res_2 = (second_match[0]), (second_match[2])
# third_res, third_res_2 = (third_match[0]), (third_match[2])

# win = int(first_res > first_res_2) + int(second_res > second_res_2) + int(third_res > third_res_2)
# loss = int(first_res < first_res_2) + int(second_res < second_res_2) + int(third_res < third_res_2)
# draw = int(first_res == first_res_2) + int(second_res == second_res_2) + int(third_res == third_res_2)
# print(f"Team won {win} games.")
# print(f"Team lost {loss} games.")
# print(f"Drawn games: {draw}")
