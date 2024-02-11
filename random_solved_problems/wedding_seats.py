end_sector = input()
rows_in_sector_A = int(input())
odd_row_seats = int(input())

start_into_ascii = ord("A")
end_sector_into_ascii = ord(end_sector)
last_character = ord("a")
add_row_for_new_sector = 0
total_seats = 0

for sectors in range(start_into_ascii, end_sector_into_ascii + 1):
    add_row_for_new_sector += 1

    for rows in range(1, rows_in_sector_A + add_row_for_new_sector):

        if rows % 2 != 0:
            for last_letter in range(last_character, last_character + odd_row_seats):
                print(f"{chr(sectors)}{rows}{chr(last_letter)}")
                total_seats += 1
        else:
            for last_letter in range(last_character, last_character + odd_row_seats + 2):
                print(f"{chr(sectors)}{rows}{chr(last_letter)}")
                total_seats += 1

print(total_seats)
