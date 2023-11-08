name = input()
grade_count = 1
false_count = 0
score_count = 0
passed_clas = False
while grade_count < 13:
    score = float(input())
    if score >= 4.00:
        grade_count += 1
        score_count += score
    else:
        false_count += 1
    if false_count > 1:
        passed_clas = True
        break
average_sum = score_count / 12
if not passed_clas:
    print(f"{name} graduated. Average grade: {average_sum:.2f}")
else:
    print(f"{name} has been excluded at {grade_count} grade")

