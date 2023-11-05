starting_num = int(input())
ending_num = int(input())

for i in range(starting_num, ending_num + 1):
    curr_num_str = str(i)
    even_count = 0
    odd_count = 0
    for j in range(0, len(curr_num_str)):
        digit = int(curr_num_str[j])
        if j % 2 == 0:
            even_count += digit
        else:
            odd_count += digit

    if even_count == odd_count:
        print(curr_num_str, end=" ")


