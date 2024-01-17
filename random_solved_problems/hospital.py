period = int(input())
doctors = 7
treated_count = 0
untreated_count = 0
day_count = 0
for days in range(period):
    patients = int(input())
    day_count += 1
    if day_count % 3 == 0 and treated_count < untreated_count:
        doctors += 1
    if patients <= doctors:
        treated_count += patients

    else:
        treated_count += doctors
        untreated_count += patients - doctors

print(f"Treated patients: {treated_count}.")
print(f"Untreated patients: {untreated_count}.")