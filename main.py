expenses = []

while True:
    print("=== PERSONAL FINANCE TRACKER ===")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter expense: "))
        expenses.append(amount)
        print("Added!")

    elif choice == "2":
        print("Your expenses:")
        for e in expenses:
            print(e)

    elif choice == "3":
        total = sum(expenses)
        print("Total:", total)

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Wrong option")