
colors = ["red", "black", "pink", "beige", "dark green", "azure", "amber", "light yellow"]
warm_count = 0
cool_count = 0
neutral_count = 0
misc_count = 0

for color in colors:
    if color in warm:
        warm_count += 1
    elif color in cool:
        cool_count += 1
    elif color in neutral:
        neutral_count += 1
    else:
        misc_count += 1

print("The total # of colors is ", len(colors))
print("There are ", warm_count, " warm colors")
print("There are ", cool_count, " cool colors")
print("There are ", neutral_count, " neutral colors")
print("There are ", misc_count, " miscellaneous colors")
