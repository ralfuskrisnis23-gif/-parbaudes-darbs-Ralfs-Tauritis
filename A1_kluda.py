skaits= 0

with open("zurnals.log", encoding="utf-8") as f:
    for rinda in f:
        skaits = skaits +1

print("Atrasts:", skaits)
