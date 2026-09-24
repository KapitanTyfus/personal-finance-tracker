file = open("results.txt", "r")

data = file.readlines()

file.close()

snatch = float(data[0].split(":")[1])

cj = float(data[1].split(":")[1])

total = snatch + cj

print(snatch)
print(cj)
print(total)

# Otwieramy plik i odczytujemy zapisane rekordy
file = open("results.txt", "r")

data = file.readlines()

file.close()


# Wyciągamy Snatch i Clean & Jerk z pliku
snatch = float(data[0].split(":")[1])
cj = float(data[1].split(":")[1])

# Liczymy aktualny rekord Total
total = snatch + cj


# Pokazujemy aktualne rekordy
print(f"Snatch record: {snatch}")
print(f"Clean and Jerk record: {cj}")
print(f"Total record: {total}")


# Użytkownik wpisuje wynik Snatch z dzisiejszego treningu
new_snatch = float(input("Snatch: "))

if new_snatch > snatch:
    print(f"New snatch record! New record: {new_snatch} Previous record: {snatch}")
    snatch = new_snatch
else:
    print(f"No new record. Current record: {snatch}")


# Użytkownik wpisuje wynik Clean & Jerk z dzisiejszego treningu
new_cj = float(input("Clean and Jerk: "))

if new_cj > cj:
    print(f"New Clean and Jerk record! New record: {new_cj} Previous record: {cj}")
    cj = new_cj
else:
    print(f"No new record. Current record: {cj}")


# Po sprawdzeniu obu bojów liczymy nowy Total
total = snatch + cj

print(f"Total record: {total}")


# Zapisujemy aktualne rekordy do pliku
file = open("results.txt", "w")

file.write(f"Snatch: {snatch}\n")
file.write(f"Clean and Jerk: {cj}\n")
file.write(f"Total: {total}\n")

file.close()


# Dopisujemy dzisiejszy trening do historii
file = open("results.txt", "a")

file.write(f"Snatch: {new_snatch}, Clean and Jerk: {new_cj}\n")

file.close()