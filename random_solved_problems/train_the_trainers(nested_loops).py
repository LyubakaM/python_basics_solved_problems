number_of_jury = int(input())
command = input()
final_grade_counter = 0
final_counter = 0
while command != "Finish":
    grade_count = 0
    counter = 0

    for i in range(number_of_jury):
        current_grade = float(input())
        grade_count += current_grade
        counter += 1
        final_counter += 1
        final_grade_counter += current_grade

    average_grade = grade_count / counter

    print(f"{command} - {average_grade:.2f}.")
    command = input()
average_final = final_grade_counter / final_counter

print(f"Student's final assessment is {average_final:.2f}.")

