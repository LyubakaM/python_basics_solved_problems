most_powerful_word = ""
mpword_ascii_count = 0


while True:
    word = input()
    if word == "End of words":
        break

    curr_counter_ascii_value = 0
    for letter in word:
        curr_counter_ascii_value += ord(letter)

    if word[0].lower() in "aeiouy":               # if letter in "aeiouyAEIOUYA":
        curr_counter_ascii_value *= len(word)
    else:
        curr_counter_ascii_value = int(curr_counter_ascii_value / len(word))

    if curr_counter_ascii_value > mpword_ascii_count:
        most_powerful_word = word
        mpword_ascii_count = curr_counter_ascii_value


print(f"The most powerful word is {most_powerful_word} - {mpword_ascii_count}")