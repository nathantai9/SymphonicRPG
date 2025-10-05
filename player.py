# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.current_city = None
        self.inventory = []
        self.level = 1
        self.experience = 0

    def move_to_city(self, city):
        self.current_city = city
        print(f"{self.name} has moved to {city.name}.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to {self.name}'s inventory.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} has gained {amount} experience points.")
        self.check_level_up()

    def check_level_up(self):
        level_threshold = self.level * 100  # Example threshold for leveling up
        if self.experience >= level_threshold:
            self.level += 1
            self.experience -= level_threshold
            print(f"{self.name} has leveled up to level {self.level}!")