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

marvin = Robots("Marvin")

six = Robots("Six")


class Dinos:
    def __init__(self):
        self.name = ''
        self.type = ''
        self.health = 100
        self.energy = 100
        self.attack = ''


def set_name(self):
    self.name = input("enter dino name")
    print("Dino name:", self.name)


rodan = Dinos("Rodan")

grumpy = Dinos("Grumpy")

gorgo = Dinos("Gorgo")

yoshi = Dinos("Yoshi")


def power_dinos(self, amount, account):
    if account == 1:
        self.health.add(amount)
    else:
        self.power_level.add(amount)
    return self


def get_random_attack(min_value, max_value):
    return random.randint(min_value, max_value)


def get_attack_from_collection(options):
    random_int = get_random_attack(0, len(options) - 1)
    return options(random_int)


def attack_assignment():
    weapons = ('razor claws', 'spike tail', 'sonic blast', 'thunderous stomp')

    satisfied = 'no'

    while satisfied != 'yes':
        chosen_attack = get_attack_from_collection(attack)

        satisfied = input(f"Your attack is {chosen_attack}. Is this deadly enough?")
