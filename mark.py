date = input("Enter date: ")

present = int(input("How many students are present: "))

for i in range(present):
    roll = input("Roll no: ")

print("-----Report-----")

print("Present: ", present/10 * 100, "%")

print("Absent: ", (10-present)/10 * 100, "%")