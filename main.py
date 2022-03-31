from colors import c
from pokemon import *
from person import *


def choose_initial_pokemon(initial_player):
    print(f"Hello {initial_player}! Choose your first pokemon:")
    pikachu = Pokemon(pokemon_type='Electric', pokemon_name='Pikachu', pokemon_level=1)
    charmander = Pokemon(pokemon_type='Fire', pokemon_name='Charmander', pokemon_level=1)
    squirtle = Pokemon(pokemon_type='Water', pokemon_name='Squirtle', pokemon_level=1)
    print(f"1 - {pikachu}")
    print(f"2 - {charmander}")
    print(f"3 - {squirtle}")
    while True:
        choice = input('Choose one: ')
        if choice == '1':
            initial_player.capture(pikachu)
            break
        elif choice == '2':
            initial_player.capture(charmander)
            break
        elif choice == '3':
            initial_player.capture(squirtle)
            break
        else:
            print('Invalid choice!')


if __name__ == '__main__':
    pass
