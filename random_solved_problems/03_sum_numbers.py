number = int(input())
count = 0

while True:
    data = int(input())
    count += data

    if count >= number:
        print(f"{count}")
        break



