first_num = int(input())
second_num = int(input())
c = 0

for i in range(first_num, second_num + 1):
    curr_number = str(i)
    even_count = 0
    odd_count = 0
    for position in range(0, len(curr_number)):
        digit = int(curr_number[position])
        if position % 2 == 0:
            even_count += digit
        else:
            odd_count += digit

    if even_count == odd_count:
        print(curr_number, end=" ")

