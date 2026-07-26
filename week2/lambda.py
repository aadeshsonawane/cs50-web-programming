people = [
    {"name":"sham", "house": "Dl"},
    {"name":"ram", "house": "MH"},
    {"name":"jay", "house": "GH"},

]
def f(person):
    return person["name"]

people.sort(key= lambda person: person["name"])

print(people)