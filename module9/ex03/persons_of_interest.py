#!/usr/bin/python3

def famous_births(historical_figures):
    sorted_figures = sorted(historical_figures.values(), key=lambda x: int(x["date_of_birth"]))
    i = 0
    while (i < len(sorted_figures)):
        person = sorted_figures[i]
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")
        i += 1

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)