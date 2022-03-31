import random

from pokemon import Pokemon
from colors import c


class Person:
    names = ['Smith', 'John', 'William', 'Jones', 'Davis', 'Miller', 'Wilson', 'Moore', 'Daniel', 'Anderson',
             'Thomas', 'Jackson', 'Harris', 'Scott', 'Mitchell', 'Parker', 'Peter', 'Miles', 'Harry', 'Tobey'
             'Stephen', 'Tony', 'Anthony', 'Steve', 'Bruce', 'Wayne', 'Edward', 'Leonard', 'Arthur', 'Morgan',
             'Evans', 'Chris', 'Justin', 'Drew', 'Richard', 'Allen', 'Barry', 'Robinson', 'George', 'James',
             'Mark', 'Donald', 'Brian', 'Joseph', 'Michael', 'Charles', 'Robert', 'Jefferson', 'Paul', 'Tom']

    def __init__(self, name=None, pokemons=None):
        if name:
            self.name = name
        else:
            self.name = random.choice(self.names)

        if pokemons is None:
            pokemons = []
        self.pokemons = pokemons

    def __str__(self):
        return self.name

    def show_pokemons(self):
        if self.pokemons:
            print(f"{self}'s pokemons:")
            for owned_pokemon in self.pokemons:
                print(f"{self.pokemons.index(owned_pokemon)+1} - {owned_pokemon}")
        else:
            print(f"{self} doesn't have any pokemons.")

    def random_pokemon_choosing(self):
        if self.pokemons:
            self.show_pokemons()
            while True:
                chosen_pokemon = random.choice(self.pokemons)
                return chosen_pokemon
        else:
            print('Error: This player does not have any pokemons.')
            

class Player(Person):
    type = 'player'

    def __init__(self, name=None, pokemons=None, coins=100):
        super().__init__(name=name, pokemons=pokemons)
        self.coins = coins

    def show_coins(self):
        print(f"You have {self.coins} coins.")

    def earn_coins(self, amount_of_coins):
        self.coins += amount_of_coins
        print(f"You won {amount_of_coins} coins.")
        self.show_coins()

    def capture(self, pokemon_to_be_captured):
        self.pokemons.append(pokemon_to_be_captured)
        print(f"{self} captured {pokemon_to_be_captured}!")

    def pokemon_choosing(self):
        if self.pokemons:
            self.show_pokemons()
            while True:
                choice = input('Choose one: ')
                try:
                    chosen_pokemon = self.pokemons[int(choice)-1]
                    return chosen_pokemon
                except ValueError:
                    print('Your choice must be a number.')
                except IndexError:
                    print('Pokemon not find.')
        else:
            print('Error: You does not have any pokemons.')

    def explore(self):
        print('Going to explore the world...')
        print('Which type of exploration would you like to do now ()?')
        print(f"1 - Soft exploration (costs 50 coins)")
        print(f"2 - Normal exploration (costs 100 coins)")
        print(f"3 - Intense exploration (costs 500 coins)")
        print(f"4 - God exploration (costs 2000 coins)")
        while True:
            exploration_choice = input('Choose one: ')
            unlucky_factor = 0.96
            soft_exploration_gen_probability = 0.7
            normal_exploration_gen_probability = 1
            hard_exploration_gen_probability = 1.3
            god_exploration_gen_probability = 2
            if exploration_choice == '1':
                if random.random() <= unlucky_factor:
                    pokemon_found = Pokemon(gen_probability=soft_exploration_gen_probability)
                    print(f"You found {pokemon_found}!")
                    if random.random() <= unlucky_factor:
                        self.capture(pokemon_found)
                    else:
                        print('Unlucky! You let the pokemon escape.')
                else:
                    print('Ohh, unlucky! You do not find any pokemons.')
            elif exploration_choice == '2':
                if random.random() <= unlucky_factor:
                    pokemon_found = Pokemon(gen_probability=normal_exploration_gen_probability)
                    print(f"You found {pokemon_found}!")
                    if random.random() <= unlucky_factor:
                        self.capture(pokemon_found)
                    else:
                        print('Unlucky! You let the pokemon escape.')
                else:
                    print('Ohh, unlucky! You do not find any pokemons.')
            elif exploration_choice == '3':
                if random.random() <= unlucky_factor:
                    pokemon_found = Pokemon(gen_probability=hard_exploration_gen_probability)
                    print(f"You found {pokemon_found}!")
                    if random.random() <= unlucky_factor:
                        self.capture(pokemon_found)
                    else:
                        print('Unlucky! You let the pokemon escape.')
                else:
                    print('Ohh, unlucky! You do not find any pokemons.')
            elif exploration_choice == '4':
                if random.random() <= unlucky_factor:
                    pokemon_found = Pokemon(gen_probability=god_exploration_gen_probability)
                    print(f"You found {pokemon_found}!")
                    if random.random() <= unlucky_factor:
                        self.capture(pokemon_found)
                    else:
                        print('Unlucky! You let the pokemon escape.')
                else:
                    print('Ohh, unlucky! You do not find any pokemons.')
            else:
                print('That is not an option...')

    def battle(self, opponent):
        print(f"{c.blue}{self}{c.reset} started a battle against {opponent}.")
        opponent_pokemon = opponent.random_pokemon_choosing()
        print(f"{opponent} choose {opponent_pokemon}")
        player_pokemon = self.pokemon_choosing()
        print(f"{self} choose {player_pokemon}")

        if opponent_pokemon and player_pokemon:
            while True:
                player_pokemon.attack(opponent_pokemon)
                if opponent_pokemon.health_points <= 0:
                    print(f"{opponent_pokemon} defeated.")
                    print(f"{self} won.")
                    self.earn_coins(opponent_pokemon.level*100)
                    break
                opponent_pokemon.attack(player_pokemon)
                if player_pokemon.health_points <= 0:
                    print(f"{player_pokemon} defeated.")
                    print(f"{player_pokemon} IS FUCKING DEAD.")
                    print(f"{opponent} won.")
                    break
        else:
            print('Battle cancelled: someone does not have any pokemons.')


class Enemy(Person):
    type = 'enemy'

    def __init__(self, name=None, pokemons=None):
        if pokemons is None:
            pokemons = []
            for i in range(5):
                pokemons.append(Pokemon())
        super().__init__(name=name, pokemons=pokemons)