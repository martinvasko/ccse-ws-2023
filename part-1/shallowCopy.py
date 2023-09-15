import copy

animals = ["dog", "cat", "fish"]
copyAnimals = animals[:]
print(copyAnimals)

cleanerCopyAnimals = copy.copy(animals)
print(cleanerCopyAnimals)
