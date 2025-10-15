#!/usr/bin/python3

def find_the_redheads(dupont_family):
    redheads = []
    items = list(dupont_family.items())
    i = 0
    while (i < len(items)):
        if (items[i][1] == "red"):
            redheads.append(items[i][0])
        i += 1
    return (redheads)


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))