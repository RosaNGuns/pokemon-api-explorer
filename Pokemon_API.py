import requests
from pathlib import Path

print()
print("----------------------------------------------")
print("                    PokeDex                   ")
print("----------------------------------------------")
print()


def start():
    while True:
        uinput = input("give a pokemon name you want some info on!: ")
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{uinput.lower()}")
        
        if response.status_code == 200:
            data = response.json()
            return data
        
        print("unknown pokemon!")
    
def basic_info(pokemon):
    print("abilities: ", end="")
    abilities = pokemon["abilities"]
    for i in abilities:
        ability = i["ability"]
        print(ability["name"], end=", ")
    print()
    print(f"height: {pokemon["height"] / 10} m")
    print(f"weight: {pokemon["weight"] /10} kg")
    
def poketypes(pokemon):
    types = pokemon["types"]
    for pokemon_type in types:
        type = pokemon_type["type"]
        types_name = type["name"]
        types_url = type["url"]
        type_url = requests.get(types_url)
        type_url_data = type_url.json()      
        damage_relations = type_url_data["damage_relations"]
        weaknesses = damage_relations["double_damage_from"]
        strenghts = damage_relations["double_damage_to"]
        print(f"type: {types_name}")
        print(f"{types_name} is weak against: ", end="")
        for weakness in weaknesses:
            print(weakness["name"], end=", ")
        print()
        print(f"{types_name} is strong against: ", end="")
        for strenght in strenghts:
            print(strenght["name"], end=", ")
        print()
        
def save_sprite(pokemon):
    types = pokemon["types"]
    sprite = pokemon["sprites"]["front_default"]
    surl = requests.get(sprite).content
    folder = Path(__file__).parent
    pokemon_folder = folder / "pokemon"
    pokemon_folder.mkdir(exist_ok=True) 
    for pokemon_type in types:
        type = pokemon_type["type"]
        types_name = type["name"]
        types_folder = pokemon_folder / types_name
        types_folder.mkdir(exist_ok = True)        
        destination = types_folder / f"{pokemon["name"]}.png"
                
        with open(destination, "wb") as file:
            file.write(surl)
        print()

def stats(pokemon):
    all_stats = pokemon["stats"]
    for stats in all_stats:
        stat = stats["stat"]
        sname = stat["name"]
        amount = stats["base_stat"]
        print(f"{sname}: {amount}")
    print()
  
pokemon = start()
  
while True:
    print()
    print(f"Pokemon name: {pokemon["name"]}")
    print()
    print("what would you like?")
    print("1. basic info \n2. pokemon type \n3. pokemon stats \n4. save pokemon sprite \n5. change pokemon \n6. exit ")
    option = input("type only the number of the option. ")
    
    if option == "1":
        print()
        basic_info(pokemon)
    elif option == "2":
        print()
        poketypes(pokemon)
    elif option == "3":
        print()
        stats(pokemon)
    elif option == "4":
        print()
        save_sprite(pokemon)
    elif option == "5":
        print()
        pokemon = start()
    elif option == "6":
        print("bye byee!")
        break
    else:
        print()
        print("what?")
        