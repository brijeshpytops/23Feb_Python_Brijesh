"""
dict - mutable, duplicate keys are not allowed, unindexed

syntax :
dict = {key1 : value1, key2 : value2, ...}
dict = dict([(key1, value1), (key2, value2), ...])
"""

contacts = {
    "A" : [
        {
            "name" : "Amit",
            "mobile": ["4675686646", "54786753756"]
        },
        {
            "name" : "Ajay",
            "mobile": ["4675686644676"]
        }
    ],
    "B" : [
        {
            "name" : "Bhavesh",
            "mobile": ["46753333344676"]
        }
    ],
    "C" : [
        {
            "name" : "Chetan",
            "mobile": ["4675667544676"]
        }
    ]
}

# print(dir(contacts))

# print(contacts)

# print(contacts["B"])

# print(contacts["A"][-1]['mobile'][0])

# x = 10
# x = 20
# print(x)


new_contacts = {
    'D': {
        'name': 'Dhaval',   
        'mobile': ['4675667231216']
    }
}

# contacts.pop('A')
# contacts.popitem()

# print(contacts.get('A'))

# contacts.update(new_contacts)

# print(contacts.keys(), len(contacts.keys()))
# print(contacts.values(), len(contacts.values()))
# print(contacts.items(), len(contacts.items()))

# for key in contacts.keys():
#     print(key)

# for value in contacts.values():
#     print(value)

# for key, value in contacts.items():
#     print(key, value)

# vegs_dict['tomato'] = 20
# vegs_dict['chilli'] = 20
# vegs_dict['ghisodu'] = 20

# print(dict().fromkeys(['tomato', "chilli", "ghisodu"], 20))


# car = {
#     'make': 'Audi',
#     'model': 'A4',
#     'year': 2018,
#     # 'color': 'white',
#     'engine': {
#         'cc': 2000,
#         'type': 'diesel',
#         }
# }
# car.setdefault("color", "blue")
# print(car)
