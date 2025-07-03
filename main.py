import time

favorites = {'color': 'blue', 'food': 'mac and cheese', 'place': 'grand canyon'}

while True:
    print(f"Your favorite categories are: {', '.join(favorites.keys())}") # ', ' makes them into one string. ChatGPT help
    view_category = input("Which category would you like to see? ")
    if view_category in favorites.keys():
        if view_category.lower().strip() == 'place':
            print(f"My favorite {view_category} is {favorites[view_category].title()}!")
            break
        else:
            print(f"My favorite {view_category} is {favorites[view_category]}!")
            break
    else:
        print("Category not found. Please try again.")
        continue

while True:
    continue_add = input("\nWould you like to add a new favorite category? (yes/no) ")
    
    if continue_add.lower().strip() == 'no':
        time.sleep(1)
        break
    elif continue_add.lower().strip() == 'yes':
        add_category = input("What category would you like to add? ")
        add_value = input(f"What is your favorite {add_category.lower().strip()}? ")
        favorites[add_category.lower().strip()] = add_value.lower().strip()
        print("Category added!")
        time.sleep(1)
        break
    else:
        print("Please put 'yes' or 'no.'")
        continue

print("\nHere are all your favorites:")
for category, favorite in favorites.items():
    print(f"{category}: {favorite}")

    