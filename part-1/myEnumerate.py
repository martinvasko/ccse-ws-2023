animals = ["cat", "dog", "fish"]
for i in range(len(animals)):
    print(i, animals[i])

for i, animal in enumerate(animals):
    print(i, animal)

for animal in animals:
    print(animal)
