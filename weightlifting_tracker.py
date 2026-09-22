snatch = 0
cj = 0
total = 0

print("========================\n WEIGHTLIFTING TRACKER \n========================")

print(f"""Current records:
1. Snatch: {snatch} kg
2. Clean & Jerk: {cj} kg
3. Total: {total} kg
""")

choice = input("1. Enter new results\n2. Show history\n3. Exit\n\n")

if choice == "1":
    snatch = float(input("Snatch: "))
    cj = float(input("Clean & Jerk: "))

    total = snatch + cj

    print("Today's total:", total)

    file = open("results.txt", "w")

    file.write(f"Snatch: {snatch}\n")
    file.write(f"Clean & Jerk: {cj}\n")
    file.write(f"Total: {total}\n")

    file.close()

elif choice == "2":
    print(f"""Current records:
Snatch: {snatch} kg
Clean & Jerk: {cj} kg
Total: {total} kg""")

elif choice == "3":
    print("Good luck")