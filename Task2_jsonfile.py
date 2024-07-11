import json

def nacti_data(nazev_souboru):
    with open(nazev_souboru, "r") as soubor:
        data = json.load(soubor)
    return data
def uloz_data(nazev_souboru, data):
    with open(nazev_souboru, "w") as soubor:
        json.dump(data, soubor)
def pridej_data(data):
    nove_data = int(input("Zadejte celé číslo k přidání: "))
    data.append(nove_data)
    print("Data byla úspěšně přidána.")
def odstran_data(data):
    del_data = int(input("Zadejte celé číslo k odstranění: "))
    if del_data in data:
        data.remove(del_data)
        print("Data byla úspěšně odstraněna.")
    else:
        print("Zadané číslo není v seznamu.")

def menu():
    nazev_souboru = "Task2.json"
    data = nacti_data(nazev_souboru)
    data = []
    uloz_data(nazev_souboru, data)
    print("Soubor nenalezen, vytvořen prázdný seznam.")

    while True:
        print("\nMenu:")
        print("1. Načíst data")
        print("2. Uložit data")
        print("3. Přidat data")
        print("4. Odstranit data")
        print("5. Konec")

        volba = input("Vyber (1-5): ")

        if volba == "1":
            data = nacti_data(nazev_souboru)
            print("Data byla úspěšně načtena ze souboru.")
        elif volba == "2":
            uloz_data(nazev_souboru, data)
            print("Data byla úspěšně uložena do souboru.")
        elif volba == "3":
            pridej_data(data)
        elif volba == "4":
            odstran_data(data)
        elif volba == "5":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    menu()