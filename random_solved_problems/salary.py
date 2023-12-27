tabs_n = int(input())
salary = int(input())


for tabs in range(1, tabs_n + 1):
    current_tab = input()
    if current_tab == "Facebook":
        salary -= 150
    elif current_tab == "Instagram":
        salary -= 100
    elif current_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        print(f"You have lost your salary.")
        break

if salary > 0:
    print(salary)