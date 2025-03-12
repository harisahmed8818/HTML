import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.attack_power = self.set_attack_power()
        self.inventory = []
        self.experience = 0
        self.level = 1

    def set_attack_power(self):
        if self.character_class == "Warrior":
            return random.randint(15, 25)
        elif self.character_class == "Mage":
            return random.randint(10, 20)
        elif self.character_class == "Rogue":
            return random.randint(12, 22)

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount}. Health is now {self.health}.")

    def attack(self, other):
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        other.take_damage(self.attack_power)

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience!")
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 20
        self.attack_power += 5
        print(f"{self.name} leveled up! Now at level {self.level}. Health is now {self.health}.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for item in self.inventory:
                print(f"- {item}")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.attack_power = random.randint(5, 15)

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def attack(self, other):
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        other.take_damage(self.attack_power)

class Game:
    def __init__(self):
        self.player = None
        self.enemies = [Enemy("Goblin"), Enemy("Orc"), Enemy("Troll")]
        self.current_enemy = None
        self.locations = {
            "forest": "You are in a dark forest. You can hear strange noises.",
            "cave": "You are in a damp cave. It's cold and eerie.",
            "village": "You are in a small village. People are bustling around.",
        }
        self.current_location = "forest"

    def create_character(self):
        name = input("Enter your character's name: ")
        character_class = input("Choose your class (Warrior, Mage, Rogue): ")
        self.player = Character(name, character_class)
        print(f"{self.player.name} the {self.player.character_class} has been created!")

    def choose_enemy(self):
        self.current_enemy = random.choice(self.enemies)
        print(f"A wild {self.current_enemy.name} appears!")

    def combat(self):
        while self.player.is_alive() and self.current_enemy.is_alive():
            action = input("Do you want to (A)ttack, (H)eal, or (I)nventory? ").lower()
            if action == 'a':
                self.player.attack(self.current_enemy)
                if self.current_enemy.is_alive():
                    self.current_enemy.attack(self.player)
            elif action == 'h':
                self.player.heal(random.randint(10, 20))
                if self.current_enemy.is_alive():
                    self.current_enemy.attack(self.player)
            elif action == 'i':
                self.player.show_inventory()
            else:
                print("Invalid action. Please choose again.")

        if self.player.is_alive():
            print(f"You defeated the {self.current_enemy.name}!")
            self.player.gain_experience(50)
            loot = random.choice(["Health Potion", "Gold Coin", "Magic Scroll"])
            self.player.add_to_inventory(loot)
        else:
                        print("You have been defeated... Game Over.")

    def explore(self):
        print(f"You are currently in the {self.current_location}.")
        print(self.locations[self.current_location])
        action = input("Do you want to (E)xplore another location or (C)ontinue fighting? ").lower()
        if action == 'e':
            self.change_location()
        elif action == 'c':
            return
        else:
            print("Invalid action. Please choose again.")

    def change_location(self):
        print("Available locations:")
        for location in self.locations.keys():
            print(f"- {location}")
        new_location = input("Where do you want to go? ").lower()
        if new_location in self.locations:
            self.current_location = new_location
            print(f"You travel to the {self.current_location}.")
            self.choose_enemy()
            self.combat()
        else:
            print("Invalid location. Please choose again.")

    def play(self):
        self.create_character()
        while self.player.is_alive():
            self.explore()
            if self.player.is_alive():
                continue_game = input("Do you want to continue exploring? (Y/N) ").lower()
                if continue_game != 'y':
                    break
        print("Thank you for playing!")

if __name__ == "__main__":
    game = Game()
    game.play() 