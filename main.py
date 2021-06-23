# lidt items are enclosed into square brackets
# lists are ordered
# lists are mutable
# list elements don't need to be unique
# lists can be made up of different data types

# list = []
# list = [2,4,6]
# list = ["KD", "MJ", "Drose", "AJ"]
# list = ["Kobe", 10, 7.5, (1,2,3), 1j + 1]
# print(list)
# print(type(list))
# print(id(list))




'''
List indexing 
'''
# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# print(FamousAthletes[0])
# print(FamousAthletes[1])
# print(FamousAthletes[3])
# print(FamousAthletes[-1])
# print(FamousAthletes[-4])

# FamousAthletes = ["KD", "MJ", ["Drose", "AJ"]]
# print(FamousAthletes[0])
# print(FamousAthletes[2])
# print(FamousAthletes[2][1])


'''
How to slice lists in python
'''
# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# print(FamousAthletes[:])
# print(FamousAthletes[:])
# print(FamousAthletes[:])
# print(FamousAthletes[0:3])
# print(FamousAthletes[:-2])
# print(FamousAthletes[:2])
# print(FamousAthletes[::3])
# print(FamousAthletes[::-1])
# print(FamousAthletes[:-2])
# print(FamousAthletes[:-3])

'''
Add elements to a list
'''

# modifing a list

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes[2] = "Mike Tyson"
# print(FamousAthletes)

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes[1:4] = "Kobe", "Conor McGregor", "Lebron"
# print(FamousAthletes)

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.append("John Cena")
# print(FamousAthletes)

'''
Remove or delete list items
'''

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# del FamousAthletes[0]
# print(FamousAthletes)

# del FamousAthletes[1:4]
# print(FamousAthletes)

# del FamousAthletes
# print(FamousAthletes)

'''
python list methods
'''

# print(help(dir))
# print(dir(list))
# print(help(list.count))
# print(help(list.copy))
# print(help(list.index))
# print(dir(set))
# print(dir(range))

# ====================================

# .append() is method used to add more items to a list.

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.append("Khabib")
# print(FamousAthletes)

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.append("Jorge Masvidol")
# print(FamousAthletes)


# print(help(list.append))

# ===================================

# .insert() method is uded to add items to list using a index position.

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.insert(0, "Muhammmed Ali")
# print(FamousAthletes)

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.insert(3, "Rounda Rousey")
# print(FamousAthletes)

# print(help(list.insert))

# ======================================

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.clear()
# print(FamousAthletes)

# print(help(list.clear))

# =======================================

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.pop(1)
# print(FamousAthletes)

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# FamousAthletes.pop(-1)
# print(FamousAthletes)

# print(help(list.pop))


# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# print(FamousAthletes.index("KD"))
# print(FamousAthletes.index("MJ"))
# print(FamousAthletes.index("Drose"))
# print(FamousAthletes.index("AJ"))
# print(FamousAthletes)

# FamousAthletes = ["KD", "MJ", "Drose", "AJ"]
# x = FamousAthletes.index("Drose")
# FamousAthletes.pop(x)
# print(FamousAthletes)

# =============================================


# FamousAthletes = ["KD", "MJ", "Drose", "Drose", "Drose", "AJ","KD"]
# print(FamousAthletes.count("KD"))
# print(FamousAthletes.count("Drose"))

# print(id(FamousAthletes))

# Athletes = {}
# for x in FamousAthletes:
#   Athletes[x] = FamousAthletes.count(x)
#   print(x)
# print(Athletes)

# ==========================================


# from collections import Counter
# print(Counter(FamousAthletes))

# ==============================================

"""
List Membership test
"""


# FamousAthletes = ["KD", "MJ", "Drose", "Drose", "Drose", "AJ","KD"]
# print("KD" in FamousAthletes)
# print("Shaq" in FamousAthletes)
# print("KD" not in FamousAthletes)
# print("Shaq" not in FamousAthletes)


























