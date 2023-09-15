def removeLastCatFromList(petSpecies):
    if len(petSpecies) > 0 and petSpecies[-1] == "cat":
        petSpecies.pop()
