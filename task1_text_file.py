nazev = input("Zadej nazev souboru s příponou:")
text = input(" Zadej text do souboru:")
try:
    with open(nazev, "w", encoding="utf-8") as soubor:
        soubor.write(text)
    print(f"Text byl uložen do souboru {nazev}")

except Exception as e:
<<<<<<< Updated upstream
    print("Chyba při zápisu")
    print()

=======
    print("Chyba při zápisu")
>>>>>>> Stashed changes
