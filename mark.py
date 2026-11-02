date = input("Enter date: ")

total = int(input("Total strngth of class: "))
present = int(input("How many students are present: "))

for i in range(present):
    roll = input("Roll no: ")

print()
print("-----Report-----")

print("Present: ", present/total * 100, "%")

print("Absent: ", (total-present)/total * 100, "%")