# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for i in humans:
    if i.name[0] == 'D':
        a.append(i.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
# print("Ends with e:")
# b = []
# for i in humans:
#     lastchar = len(i - 1)
#     if i.name[lastchar] == "e":
#         b.append(i.name)
# print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for i in humans:
    if  i.name[0] == "C" or i.name[0] == "D" or i.name[0] == "E" or i.name[0] == "F" or i.name[0] == "G": 
        c.append(i.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for i in humans:
    d.append(i.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for i in humans:
    e.append(i.name + " - " + str(i.age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for x in humans:
    if 27 < x.age < 32:
        f.append(x.name + ", " + str(x.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for i in humans:
    uppercase = i.name.upper()
    g.append(uppercase)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for i in humans:
    h.append(i.age**2)
print(h)
