import json

data = {"jmeno": "Michal",
        "Vek": 40,
        "zaliby": ["kolo", "kemping"]}

class Uzivatel:
    def __init__(self, jmeno, vek, zaliby):
        self.jmeno = jmeno
        self.vek = vek
        self.zaliby = zaliby

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)

p = Uzivatel("Michal", 45, ["kemping", "kolo"])

print(p.to_json())

with open("ukazka.json", "w") as soubor:
    json.dump(p.to_dict(), soubor)


with open("ukazka.json", "r") as S:
    data2 = json.load(S)

print(f"data z souboru: {data2}")