budget_left = float(input())
actor_name = input()
actor_wage = 0

while actor_name != "ACTION":
    if len(actor_name) <= 15:
        actor_wage = float(input())
    else:
        actor_wage = budget_left * 20 / 100
    budget_left -= actor_wage
    if budget_left <= 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        break
    actor_name = input()
else:
    print(f"We are left with {budget_left:.2f} leva.")



#budget = float(input())
#curr_budget = budget


#while True:
    #command = input()
    #if command == "ACTION":
        #break
    #actor_name = command
    #if curr_budget <= 0:
        #break
    #else:
        #if len(actor_name) <= 15:
            #price = float(input())
            #curr_budget -= price
        #else:
            #curr_budget -= curr_budget * 0.2

#if curr_budget > 0:
    #print(f"We are left with {abs(curr_budget):.2f} leva.")

#else:
    #print(f"We need {abs(curr_budget):.2f} leva for our actors.")

