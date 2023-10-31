standard_count = 0
kid_count = 0
student_count = 0
counter = 0
total_tickets = 0

while True:
    command = input()
    if command == "Finish":
        break
    capacity = int(input())
    capacity_decrease = capacity

    counter = 0
    while True:
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "kid":
            kid_count += 1
        elif ticket_type == "student":
            student_count += 1
        total_tickets += 1
        counter += 1
        capacity_decrease -= 1
        if capacity_decrease <= 0:
            break
    average = (counter / capacity) * 100
    print(f"{command} - {average:.2f}% full.")
s_ave = (student_count / total_tickets) * 100
kid_ave = (kid_count / total_tickets) * 100
std_ave = (standard_count / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{s_ave:.2f}% student tickets.")
print(f"{std_ave:.2f}% standard tickets.")
print(f"{kid_ave:.2f}% kids tickets.")
