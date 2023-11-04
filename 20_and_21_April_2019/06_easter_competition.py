n = int(input())
best_baker = ""
backer_score = 0
best_score = 0
best_backer_name = ""
for scores in range(n):
    baker_name = input()
    backer_score = 0
    while True:
        user_input = input()
        if user_input == "Stop":
            print(f"{baker_name} has {backer_score} points.")
            if backer_score > best_score:
                print(f"{baker_name} is the new number 1!")
                best_score = backer_score
                best_backer_name = baker_name
            break
        points = int(user_input)
        backer_score += points
print(f"{best_backer_name} won competition with {best_score} points!")