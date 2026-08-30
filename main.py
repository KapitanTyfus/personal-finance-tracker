import json

# --- wczytanie danych na starcie ---
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []          # jeśli plik nie istnieje, zaczynamy od pustej listy


while True:
    print("=== PERSONAL FINANCE TRACKER ===")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What did you buy? ")
        amount = float(input("How much did it cost? "))
        category = input("Category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Added!")

    elif choice == "2":
        print("Your expenses:")
        for e in expenses:
            print(e)

    elif choice == "3":
        total = 0
        for e in expenses:
            total += e["amount"]
        print("Total:", total)

    elif choice == "4":
        # --- zapisanie danych przed wyjściem ---
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        print("Bye!")
        break

    else:
        print("Wrong option")