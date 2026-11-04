import csv

servisi = {}

with open("zurnals.log", encoding="utf-8") as f:
    for rinda in f:
        if "ERROR" in rinda:
            dalas = rinda.split()
            for i in range(len(dalas)):
                if "ERROR" in dalas[i] and i + 1 < len(dalas):
                    serviss = dalas[i + 1].strip(":")
                    if serviss in servisi:
                        servisi[serviss] = servisi[serviss] + 1
                    else:
                        servisi[serviss] = 1
                    break

with open("servisi.csv", "w", newline="", encoding="utf-8-sig") as g:
    rakstitajs = csv.writer(g, delimiter=";")
    rakstitajs.writerow(["serviss", "error_skaits"])
    for serviss in servisi:
        rakstitajs.writerow([serviss, servisi[serviss]])

print("Dati ierakstīti")
 
