import json

data = "Text"

with open("ukazka.json", "w") as soubor:
    json.dump(data, soubor)

