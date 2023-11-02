the_best_movie = ""
counter = 7
best_score = 0
previous_score = 0
while True:
    if counter == 0:
        print(f"The limit is reached.")
        break
    movie = input()
    counter -= 1
    if movie == "STOP":
        break

    curr_score = 0
    for letters in movie:
        add_sum = ord(letters)
        if letters.isupper():
            add_sum -= len(movie)
        elif letters.islower():
            add_sum -= (len(movie) * 2)
        curr_score += add_sum
    if curr_score > previous_score:
        previous_score = curr_score
        the_best_movie = movie

print(f"The best movie for you is {the_best_movie} with {previous_score} ASCII sum.")