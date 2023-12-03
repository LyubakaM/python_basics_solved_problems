t1 = int(input())
t2 = int(input())
t3 = int(input())

tot_seconds = t1 + t2 + t3
min = tot_seconds // 60
seconds = tot_seconds % 60
end = f"{min}:0{seconds}"
end2 = f"{min}:{seconds}"

if seconds < 10:
    print(end)
else:
    print(end2)

