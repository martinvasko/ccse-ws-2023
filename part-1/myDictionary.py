numberOfPets = {"dogs": 2}
if "cats" in numberOfPets:
    print("I have", numberOfPets["cats"], "cats")
else:
    print("I have no cats")

print("I have", numberOfPets.get("cats", "no"), "cats")
