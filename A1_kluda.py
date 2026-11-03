skaits = 0

with open("zurnals.log", encoding="utf-8") as f:
    for rinda in f:
        if "WARNING" in rinda:
            skaits = skaits + 1

print("Atrasts:", skaits)
