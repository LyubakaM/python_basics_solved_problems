n = int(input())
count = 0
bus_count = 0
truck_count = 0
train_count = 0
price = 0
total_tons = 0
for loads in range(n):
    curr_price = 0
    curr_load = int(input())
    total_tons += curr_load
    if curr_load <= 3:
        curr_price = 200
        bus_count += curr_load
    elif 4 <= curr_load <= 11:
        curr_price = 175
        truck_count += curr_load
    elif curr_load >= 12:
        curr_price = 120
        train_count += curr_load
    price += curr_price * curr_load
average = price / total_tons
print(f"{average:.2f}")
print(f"{bus_count / total_tons * 100:.2f}%")
print(f"{truck_count / total_tons * 100:.2f}%")
print(f"{train_count / total_tons * 100:.2f}%")