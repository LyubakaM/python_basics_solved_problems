
best_player = ""
best_score = - 90000000

while True:
    command = input()
    if command == "Stop":
        break
    name = command
    counter = 0
    previous_score = 0
    score = 0

    for letters in name:
        input_score = int(input())
        if input_score == ord(letters):
            counter += 1
            score += 10
        else:
            score += 2
    if score >= best_score:
        best_score = score
        best_player = name

print(f"The winner is {best_player} with {best_score} points!")
