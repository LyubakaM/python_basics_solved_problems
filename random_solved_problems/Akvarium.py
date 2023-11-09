d = int(input())
w = int(input())
h = int(input())
p = int(input())

obem = d * w * h
obeml = obem / 1000
z = p / 100
all = obeml * (1-z)
print(all)