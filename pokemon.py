import random

from colors import c


pokemon_types = ['Electric', 'Fire', 'Water', 'Grass', 'Psychic', 'Ghost', 'Dragon', 'Normal']

with open('pokemons/electric_pokemons.txt', 'r') as file:
    electric_pokemons = []
    for line in file.readlines():
        electric_pokemons.append(line.strip())
    electric_attacks = []
    for line in file.readlines():
        electric_attacks.append(line.strip())

with open('pokemons/fire_pokemons.txt', 'r') as file:
    fire_pokemons = []
    for line in file.readlines():
        fire_pokemons.append(line.strip())

with open('pokemons/fire_attacks.txt', 'r') as file:
    fire_attacks = []
    for line in file.readlines():
        fire_attacks.append(line.strip())

with open('pokemons/water_pokemons.txt', 'r') as file:
    water_pokemons = []
    for line in file.readlines():
        water_pokemons.append(line.strip())

with open('pokemons/water_attacks.txt', 'r') as file:
    water_attacks = []
    for line in file.readlines():
        water_attacks.append(line.strip())

with open('pokemons/grass_pokemons.txt', 'r') as file:
    grass_pokemons = []
    for line in file.readlines():
        grass_pokemons.append(line.strip())

with open('pokemons/grass_attacks.txt', 'r') as file:
    grass_attacks = []
    for line in file.readlines():
        grass_attacks.append(line.strip())
        
with open('pokemons/psychic_pokemons.txt', 'r') as file:
    psychic_pokemons = []
    for line in file.readlines():
        psychic_pokemons.append(line.strip())

with open('pokemons/psychic_attacks.txt', 'r') as file:
    psychic_attacks = []
    for line in file.readlines():
        psychic_attacks.append(line.strip())

with open('pokemons/ghost_pokemons.txt', 'r') as file:
    ghost_pokemons = []
    for line in file.readlines():
        ghost_pokemons.append(line.strip())

with open('pokemons/ghost_attacks.txt', 'r') as file:
    ghost_attacks = []
    for line in file.readlines():
        ghost_attacks.append(line.strip())

with open('pokemons/dragon_pokemons.txt', 'r') as file:
    dragon_pokemons = []
    for line in file.readlines():
        dragon_pokemons.append(line.strip())

with open('pokemons/dragon_attacks.txt', 'r') as file:
    dragon_attacks = []
    for line in file.readlines():
        dragon_attacks.append(line.strip())

with open('pokemons/normal_pokemons.txt', 'r') as file:
    normal_pokemons = []
    for line in file.readlines():
        normal_pokemons.append(line.strip())

with open('pokemons/normal_attacks.txt', 'r') as file:
    normal_attacks = []
    for line in file.readlines():
        normal_attacks.append(line.strip())


def randomPokemon(pokemon_type=None):
    pokemons = []
    if not pokemon_type:
        pokemon_type = random.choice(pokemon_types)
    if pokemon_type == 'Electric':
        pokemons = electric_pokemons
    elif pokemon_type == 'Fire':
        pokemons = fire_pokemons
    elif pokemon_type == 'Water':
        pokemons = water_pokemons
    elif pokemon_type == 'Grass':
        pokemons = grass_pokemons
    elif pokemon_type == 'Psychic':
        pokemons = psychic_pokemons
    elif pokemon_type == 'Ghost':
        pokemons = ghost_pokemons
    elif pokemon_type == 'Dragon':
        pokemons = dragon_pokemons
    elif pokemon_type == 'Normal':
        pokemons = normal_pokemons
    return pokemon_type, random.choice(pokemons)


class Pokemon:
    def __init__(self, pokemon_type=None, pokemon_name=None, pokemon_level=None, gen_probability=1):
        if pokemon_type:
            self.type = pokemon_type
            if pokemon_name:
                self.name = pokemon_name
            else:
                self.name = randomPokemon(pokemon_type)[1]
        else:
            random_pokemon = randomPokemon()
            self.type = random_pokemon[0]
            self.name = random_pokemon[1]
        if pokemon_level:
            self.level = pokemon_level
        else:
            probability = random.random()*gen_probability
            if probability <= 0.70:
                self.level = random.randint(1, 20)
            elif 0.70 < probability <= 0.84:
                self.level = random.randint(20, 35)
            elif 0.84 < probability <= 0.91:
                self.level = random.randint(35, 50)
            elif 0.91 < probability <= 0.96:
                self.level = random.randint(50, 65)
            elif 0.96 < probability <= 0.99:
                self.level = random.randint(65, 80)
            else:
                self.level = random.randint(80, 100)

        self.attack_points = self.level * 5
        self.health_points = self.level * 10

    def __str__(self):
        return f"{self.name}({self.level})"

    def attack(self, target):
        attacks = []
        if self.type == 'Electric':
            attacks = electric_attacks
        elif self.type == 'Fire':
            attacks = fire_attacks
        elif self.type == 'Water':
            attacks = water_attacks
        elif self.type == 'Grass':
            attacks = grass_attacks
        elif self.type == 'Psychic':
            attacks = psychic_attacks
        elif self.type == 'Ghost':
            attacks = ghost_attacks
        elif self.type == 'Dragon':
            attacks = dragon_attacks
        elif self.type == 'Normal':
            attacks = normal_attacks
        attack_strength = int(self.attack_points * random.random() * 1.3)
        target.health_points -= attack_strength
        if target.health_points <= 0:
            target.health_points = 0
        print(f"{self} launched a {random.choice(attacks)} on {target} with strength of {attack_strength}!")
        print(f"{target} remaining health: {target.health_points}")


class ElectricPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Electric', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class FirePokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Fire', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class WaterPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Water', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class GrassPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Grass', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class PsychicPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Psychic', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class GhostPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Ghost', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class DragonPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Dragon', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


class NormalPokemon(Pokemon):
    def __init__(self, pokemon_name=None, pokemon_level=None):
        super().__init__(pokemon_type='Normal', pokemon_name=pokemon_name, pokemon_level=pokemon_level)


def main():
    print(__name__)


if __name__ == '__main__':
    main()