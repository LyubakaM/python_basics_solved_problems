students_number = int(input())
grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
grades_count = 0

for grade in range(students_number):
    curr_grade = float(input())
    grades_count += curr_grade
    if 2.00 <= curr_grade <= 2.99:
        grade1 += 1
    elif 3.00 <= curr_grade <= 3.99:
        grade2 += 1
    elif 4.00 <= curr_grade <= 4.99:
        grade3 += 1
    elif curr_grade >= 5.00:
        grade4 += 1
average = (grades_count / students_number)
print(f"Top students: {((grade4 / students_number) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((grade3 / students_number) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((grade2 / students_number) * 100):.2f}%")
print(f"Fail: {((grade1 / students_number) * 100):.2f}%")
print(f"Average: {average:.2f}")