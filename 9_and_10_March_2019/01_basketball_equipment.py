n = int(input())

k = n * 0.4
ka = n - k
e = ka * 0.2
ea = ka - e
t = ea / 4
a = t / 5

all_tot = ka + ea + t + a +n
print(f"{all_tot:.2f}")