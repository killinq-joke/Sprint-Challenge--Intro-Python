# The following list comprehension exercises will make use of the
# defined Human class.
import math
import string


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
for D in humans:
    if D.name.startswith("D"):
        a.append(D.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for e in humans:
    if e.name.endswith("e"):
        b.append(e.name)


print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for CG in humans:
    for letter in list(string.ascii_uppercase)[2:-19]:
        if CG.name.startswith(letter):
            c.append(CG.name)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for age_plus_10 in humans:
    d.append(age_plus_10.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for name_age in humans:
    e.append(f"{name_age.name}-{name_age.age}")
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for btw27_32 in humans:
    if btw27_32.age >= 27 and btw27_32.age <= 32:
        f.append((btw27_32.name, btw27_32.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
up_humans = humans[:]
for x in up_humans:
    g.append(Human(x.name.upper(), x.age + 5))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = []

for sqr in humans:
    h.append(math.sqrt(sqr.age))
print(h)
