starting_letter = input()
end_letter = input()
skip_letter = input()

starting_letter_ascii = ord(starting_letter)
end_letter_ascii = ord(end_letter) + 1
skip_letter_ascii = ord(skip_letter)

counter = 0

for first in range(starting_letter_ascii, end_letter_ascii):
    for second in range(starting_letter_ascii, end_letter_ascii):
        for third in range(starting_letter_ascii, end_letter_ascii):
            if first != skip_letter_ascii and second != skip_letter_ascii and third != skip_letter_ascii:
                counter += 1
                print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")

print(counter)