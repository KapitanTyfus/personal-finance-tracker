file = open("results.txt", "r")

data = file.readlines()

file.close()

snatch = float(data[0].split(":")[1])

cj = float(data[1].split(":")[1])

total = snatch + cj

print(snatch)
print(cj)
print(total)