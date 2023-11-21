from pprint import pprint
import requests

def get_pokemon(name_pokemon="ditto"):

    request_url = f"https://pokeapi.co/api/v2/pokemon/{name_pokemon.lower()}"

    pokemon_data = requests.get(request_url).json()


    return pokemon_data

def get_moves(pokemon_data):
    pass

if __name__ == "__main__":
    
    print("********Prueba pokemon*********")

    pokemon_name = input("\nIntroduce a pokemon name: ")

    pokemon_data = get_pokemon(pokemon_name)

    print("\n")
    print(pokemon_data["name"])
    pprint(pokemon_data)
