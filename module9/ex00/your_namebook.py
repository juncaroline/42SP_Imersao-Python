#!/usr/bin/python3

def array_of_names(persons):
    full_name = []
    first_name = list(persons.keys())
    last_name = list(persons.values())
    i = 0
    while i < len(first_name):
        full_name.append(f"{first_name[i].capitalize()} {last_name[i].capitalize()}")
        i += 1
    return (full_name)

persons = {
    'jean': 'valjean',
    'grace': 'hopper',
    'xavier': 'niel',
    'fifi': 'brindacier'
}

print(array_of_names(persons))