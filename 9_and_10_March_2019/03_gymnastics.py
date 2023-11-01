country = input()
tool = input()

score = 0

if country == "Bulgaria":
    if tool == "ribbon":
        score = 9.600 + 9.400
    elif tool == "hoop":
        score = 9.550 + 9.750
    elif tool == "rope":
        score = 9.500 + 9.400
elif country == "Russia":
    if tool == "ribbon":
        score = 9.100 + 9.400
    elif tool == "hoop":
        score = 9.300 + 9.800
    elif tool == "rope":
        score = 9.600 + 9.000
elif country == "Italy":
    if tool == "ribbon":
        score = 9.200 + 9.500
    elif tool == "hoop":
        score = 9.450 + 9.350
    elif tool == "rope":
        score = 9.700 + 9.150
print(f"The team of {country} get {score:.3f} on {tool}.")
total = 20 - score
tot_perc = (total / 20) * 100
print(f"{tot_perc:.2f}%")