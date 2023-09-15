season = input("Which season? ")

# First version
if season == "Winter":
    holiday = "New Year's day"
elif season == "Spring":
    holiday = "May Day"
elif season == "Summer":
    holiday = "Juneteenth"
elif season == "Fall":
    holiday = "Halloween"
else:
    holiday = "Personal day off"


# Second version
holiday = {
    "Winter": "New Year's day",
    "Spring": "May Day",
    "Summer": "Juneteenth",
    "Fall": "Halloween",
}.get(season, "Personal day off")

print(f"Happy {holiday}")
