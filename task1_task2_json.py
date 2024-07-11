import json

class Letadlo:
    def __init__(self, model, vyrobce, kapacita_sedadla, dolet_km):
        self.model = model
        self.vyrobce = vyrobce
        self.kapacita_sedadla = kapacita_sedadla
        self.dolet_km = dolet_km
    def zobraz_info(self):
        print(f"Model: {self.model}")
        print(f"Výrobce: {self.vyrobce}")
        print(f"Kapacita sedadel: {self.kapacita_sedadla}")
        print(f"Dolet: {self.dolet_km} km")
    def let(self):
        print(f"Letadlo {self.model} letí.")
    def to_dict(self):
        return self.__dict__

def uloz_letadlo(letadlo, nazev_souboru):
    with open(nazev_souboru, "w") as soubor:
        json.dump(letadlo, soubor)
    print(f"Letadlo bylo uložen do souboru: {nazev_souboru}.")

def nacti_letadlo(nazev_souboru):
    with open(nazev_souboru, "rb") as soubor:
        letadlo = json.load(soubor)
    print(f"Letadlo bylo načteno ze souboru: {nazev_souboru}.")
    return letadlo

if __name__ == "__main__":

    letadlo = Letadlo("Boeing 886", "Boeing", 525, 6378)

    letadlo.zobraz_info()
    letadlo.let()
    uloz_letadlo(letadlo, "Task1_T2_json_letadlo.json")
    nactene_letadlo = nacti_letadlo("Task1_T2_json_letadlo.json")
    nactene_letadlo.zobraz_info()
