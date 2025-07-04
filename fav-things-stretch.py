import time
import json
import os # from ChatGPT

if os.path.exists("favorites.txt"):
    with open("favorites.txt", "r") as file: # from ChatGPT
        favorites = json.load(file)
        print("Favorites loaded from file!")
        time.sleep(1)
else:
    favorites = {'color': 'blue', 'food': 'mac and cheese', 'place': 'grand canyon'}

def clean_input(prompt_message):
    return input(prompt_message).lower().strip() # from ChatGPT. cleanup purposes
    

print(f"Available categories: {', '.join(favorites)}") # ', ' makes them into one string. ChatGPT help

while True:
    action = clean_input("\n\nWhat would you like to do? (lookup/add/update/display/delete/quit) ")
    if action == 'lookup':
        while True:
            view_category = clean_input("\nWhich category would you like to see? ")   
            if view_category in favorites:
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
        
    elif action == 'add': # ChatGPT
        add_category = clean_input("What category would you like to add? ")
        add_value = clean_input(f"What is your favorite {add_category}? ")
        favorites[add_category] = add_value
        print("Category added!")
        time.sleep(1)
        
    elif action == 'display':
        print("\nHere are all your favorites:")
        for category, favorite in favorites.items():
            print(f"{category}: {favorite}")
        time.sleep(1)
        
    elif action == 'update':
            while True:
                user_update = clean_input("\nWhat category would you like to update: ")
                if user_update in favorites:
                    user_update_favorite = clean_input(f"What is your favorite {user_update}? ")
                    favorites[user_update] = user_update_favorite
                    print(f"Your favorite {user_update} is now {user_update_favorite}!")
                    time.sleep(1)
                    break
                else:
                    print("Category not found. Please try again.")
                    continue
                
    elif action == 'delete':
        while True:
            user_del = clean_input("\nWhat category would you like to delete?")
            if user_del in favorites:
                del favorites[user_del]
                print("Category deleted!")
                time.sleep(1)
                break
            else:
                print("Category not found. Please try again.")
                continue    
    
    elif action == 'quit':
        print("Goodbye!")
        with open("favorites.txt", "w") as file: # from ChatGPT
            json.dump(favorites, file)
        time.sleep(1)
        break
    
    else:
        print("Invalid option. Try again.")

    