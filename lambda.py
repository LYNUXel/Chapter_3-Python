
people = [
    {"name":"David", "house":"White"},
    {"name":"Arian", "house":"Red"},
    {"name":"Cristian","house":"Black"},
]

# def f(person):
#     return person["house"]

# Sorting the peoples with the function f
# people.sort(key=f)

# => OR.. with lambda function <=
people.sort(key=lambda person: person["name"])


print(people)