n = int(input())

bonus = 0

if n <= 100:
    bonus += 5
elif n > 1000:
    bonus = n * 0.10
else:
    bonus = n * 0.20

if n % 2 == 0:
    bonus += 1
elif n % 10 == 5:
    bonus += 2

print(bonus)
print(n + bonus)