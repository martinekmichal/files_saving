import json

vstup = input("Zadej seznam celých čísel, oddělených čárkami: ")
data = [int(x) for x in vstup.split(",")]

with open("task1.json", "w") as soubor:
    json.dump(data, soubor)

with open("task1.json", "r") as r_soubor:
    seznam_n = json.load(r_soubor)
    print("Načtené data:", seznam_n)
