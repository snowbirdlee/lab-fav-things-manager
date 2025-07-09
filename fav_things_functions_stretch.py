import time
import json
import os

favorites_json = "favorites.json"

# ChatGPT helped me a lot with functions :)
# ChatGPT recommended to remove .keys() for simplicity

def load_favorites():
    if os.path.exists(favorites_json):
        with open(favorites_json, "r") as file:
            favorites = json.load(file) or {'color': 'blue', 'food': 'mac and cheese', 'place': 'grand canyon'}
    else:
        favorites = {'color': 'blue', 'food': 'mac and cheese', 'place': 'grand canyon'}
    return favorites
def save_favorites(favorites):
    with open(favorites_json, "w") as file:
        json.dump(favorites, file, indent=2)

def clean_input(prompt_message):
    return input(prompt_message).lower().strip() # from ChatGPT. cleanup purposes

def lookup_favorite(favorites, view_category):
    if view_category in favorites:
        if view_category == 'place':
            print("My favorite place is Grand Canyon!") 
        else:
            print(f"My favorite {view_category} is {favorites[view_category]}!")
    else:
        print("Category not found.")
    time.sleep(1)

def add_favorite(favorites, category, value): # from ChatGPT. while True deleted
    new_favorites = favorites.copy()  # Create a new dictionary to modify
    new_favorites[category] = value
    print("Category added!")
    time.sleep(1)
    save_favorites(new_favorites)
    return new_favorites

def display_favorite(favorites):
    print("\nHere are all your favorites:")
    for category, favorite in favorites.items():
        print(f"{category}: {favorite}")
    time.sleep(1)
        
def update_favorite(favorites, category, value):
    if category in favorites:
        favorites[category] = value
        print(f"Your favorite {category} is now {value}!")
        save_favorites(favorites) 
    else:
        print("Category not found. Please try again.")
    time.sleep(1)
    return favorites
            

def del_favorite(favorites, category):
    if category in favorites:
        del favorites[category]
        print("Category deleted!")
        time.sleep(1)
        save_favorites(favorites)
    else:
        print("Category not found. Please try again.")
    time.sleep(1)
    return favorites


def main():
    favorites = load_favorites()
    print(f"Available categories: {', '.join(favorites)}") # ', ' makes them into one string. ChatGPT help
    while True:
        action = clean_input("\n\nWhat would you like to do? (lookup/add/update/display/delete/quit) ")
        
        if action == 'lookup':
            view_category = clean_input("\nWhich category would you like to see? ")
            lookup_favorite(favorites, view_category)      
            
        elif action == 'add': # ChatGPT
            add_category = clean_input("What category would you like to add? ")
            add_value = clean_input(f"What is your favorite {add_category}? ")
            result = add_favorite(favorites, add_category, add_value)
            if result is not None:
                favorites = result
                display_favorite(favorites) 
                   
        elif action == 'display':
            display_favorite(favorites)
            
        elif action == 'update':
            user_update = clean_input("\nWhat category would you like to update: ")
            new_value = clean_input(f"What is your favorite {user_update}? ")
            favorites = update_favorite(favorites, user_update, new_value)
            
        elif action == 'delete':
            user_del = clean_input("\nWhat category would you like to delete? ")
            favorites = del_favorite(favorites, user_del)
            
        elif action == 'quit':
            print("Goodbye!")
            save_favorites(favorites)
            time.sleep(1)
            break
        
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()