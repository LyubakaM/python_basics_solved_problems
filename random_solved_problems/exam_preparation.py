bad_scores = int(input())
bad_score_count = 0
score = 0
problems_count = 0
last_prob_name = ""
failed = False
while bad_score_count < bad_scores:
    cur_problem = input()
    if cur_problem == "Enough":
        break
    grade = int(input())
    if grade <= 4:
        bad_score_count += 1
        problems_count += 1
        score += grade
        last_prob_name = cur_problem
        if bad_scores <= bad_score_count:
            failed = True
            break
    else:
        score += grade
        problems_count += 1
        last_prob_name = cur_problem
average_score = score / problems_count
if failed:
    print(f"You need a break, {bad_score_count} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_prob_name}")
