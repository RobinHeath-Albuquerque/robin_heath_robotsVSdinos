import random


class Robots:
    def __init__(self, name, health, power_level, weapon, ):
        self.name = ''
        self.health = 100
        self.power_level = 100
        self.weapon = weapon


def set_name(self):
    self.name = input("enter robot name")
    print("Robot name:", self.name)


def power_robot(self, amount, account):
    if account == 1:
        self.health.add(amount)
    else:
        self.power_level.add(amount)
    return self


def get_random_weapon(min_value, max_value):
    return random.randint(min_value, max_value)


def get_weapon_from_collection(options):
    random_int = get_random_weapon(0, len(options) - 1)
    return options(random_int)


def weapon_assignment():
    weapons = ('laser', 'machine gun', 'heat ray')

    satisfied = 'no'

    while satisfied != 'yes':
        chosen_weapon = get_weapon_from_collection(weapons)

        satisfied = input(f"You  are assigned {chosen_weapon}. Is this deadly enough?")


calculon = Robots("Calculon")

bender = Robots("Bender")


