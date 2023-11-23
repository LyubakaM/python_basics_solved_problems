n = int(input())
for numbers in range(1, n + 1):
    str_number = str(numbers)
    curr_letter = []
    for str_numbers_in_numbers in str_number:
        curr_letter.append(int(str_numbers_in_numbers))
    if sum(curr_letter) in (5, 7, 11):
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")

# n = int(input())
# for numbers in range(1, n + 1):
#     str_number = str(numbers)
#     digits_sum = sum(int(x) for x in str_number)#
#     if digits_sum in (5, 7, 11):
#         print(f"{numbers} -> True")
#     else:
#         print(f"{numbers} -> False")
