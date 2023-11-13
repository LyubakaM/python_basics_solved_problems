input_line = input()
total_count = 0
student_count = 0
standard_count = 0
kid_count = 0

while input_line != "Finish":
    curr_movie = input_line
    capacity = int(input())

    current_ticket_count = 0
    command_line = input()
    while command_line != "End":
        type_ticket = command_line
        current_ticket_count += 1

        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        elif type_ticket == "kid":
            kid_count += 1
        if current_ticket_count == capacity:
            break
        command_line = input()
    total_count += current_ticket_count
    percentage_current = current_ticket_count / capacity * 100
    print(f"{curr_movie} - {percentage_current:.2f}% full.")
    input_line = input()

standard_tickets = (standard_count / total_count) * 100
student_tickets = (student_count / total_count) * 100
kid_tickets = (kid_count / total_count) * 100

print(f"Total tickets: {total_count}")
print(f"{student_tickets:.2f}% student tickets.")
print(f"{standard_tickets:.2f}% standard tickets.")
print(f"{kid_tickets:.2f}% kids tickets.")










