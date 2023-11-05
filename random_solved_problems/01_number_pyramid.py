n = int(input())
flag = False
count = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if count > n:
            flag = True
            break
        print(count, end=" ")
        count += 1

    print()

    if flag:
        break

