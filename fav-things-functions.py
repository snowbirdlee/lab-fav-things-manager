import time

favorites = {'color': 'blue', 'food': 'mac and cheese', 'place': 'grand canyon'}

# ChatGPT helped me a lot with functions :)
def clean_input(prompt_message):
    return input(prompt_message).lower().strip() # from ChatGPT. cleanup purposes

def lookup_favorite(favorites):
    while True:
        view_category = clean_input("\nWhich category would you like to see? ")   
        if view_category in favorites.keys():
            if view_category == 'place':
                print(f"My favorite {view_category} is {favorites[view_category].title()}!") 
                time.sleep(1)
            else:
                print(f"My favorite {view_category} is {favorites[view_category]}!")  
                time.sleep(1)
        else:
            view_category = clean_input("Category not found. Please try again: ")
            continue
        break

def add_favorite(favorites): # from ChatGPT
    while True:
        add_category = clean_input("What category would you like to add? ")
        add_value = clean_input(f"What is your favorite {add_category}? ")
        favorites[add_category] = add_value
        print("Category added!")
        time.sleep(1)
        return favorites # this updates

def display_favorite(favorites):
    print("\nHere are all your favorites:")
    for category, favorite in favorites.items():
        print(f"{category}: {favorite}")
    time.sleep(1)
        
def update_favorite(favorites):
    while True:
        user_update = clean_input("\nWhat category would you like to update: ")
        if user_update in favorites.keys():
            user_update_favorite = clean_input(f"What is your favorite {user_update}? ")
            favorites[user_update] = user_update_favorite
            print(f"Your favorite {user_update} is now {user_update_favorite}!")
            time.sleep(1)
            return favorites
        else:
            print("Category not found. Please try again.")
            continue

def del_favorite(favorites):
    while True:
        user_del = clean_input("\nWhat category would you like to delete?")
        if user_del in favorites.keys():
            del favorites[user_del]
            print("Category deleted!")
            time.sleep(1)
            return favorites
        else:
            print("Category not found. Please try again.")
            continue
            

print(f"Available categories: {', '.join(favorites.keys())}") # ', ' makes them into one string. ChatGPT help

while True:
    action = clean_input("\n\nWhat would you like to do? (lookup/add/update/display/delete/quit) ")
    if action == 'lookup':
        lookup_favorite(favorites)       
    elif action == 'add': # ChatGPT
        result = add_favorite(favorites)
        if result is not None:
            favorites = result
            display_favorite(favorites)    
    elif action == 'display':
        display_favorite(favorites)
    elif action == 'update':
        update_favorite(favorites)
    elif action == 'delete':
        del_favorite(favorites)
    elif action == 'quit':
        print("Goodbye!")
        time.sleep(1)
        break
    else:
        print("Invalid option. Try again.")

