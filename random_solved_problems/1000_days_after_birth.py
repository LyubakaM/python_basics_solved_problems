import datetime

dob = input()
dob2 = datetime.datetime.strptime(dob, "%d-%m-%Y")
dob3 = dob2 + datetime.timedelta(days=1000)
p = datetime.datetime.strftime(dob3, "%d-%m-%Y")

print(p)