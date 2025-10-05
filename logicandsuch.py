from classesandsuch import *

import colorama

import player
colorama.init()

# ----------- Boss Battle Logic -----------

def start_boss_battle(player, Boss):
    print(colorama.Fore.RED + f"A wild {Boss.name} appears!" + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + f"--------------------------------------" + colorama.Style.RESET_ALL)
    while Boss.strength > 0 and player.level > 0:
        action = input("Choose your action: (1) Attack (2) Run Away\n")
        if action == "1":
            damage = player.level * 10  # Example damage calculation
            Boss.strength -= damage
            print(f"You dealt {damage} damage to {Boss.name}.")
        elif action == "2":
            print("You ran away!")
            break
        else:
            print("Invalid action.")
    if Boss.strength <= 0:
        print(f"You defeated {Boss.name}!")
    elif player.level <= 0:
        print("You have been defeated!")

# ----------- Game Map Overview Function -----------

def show_world_map():
    print(colorama.Fore.CYAN + "Welcome to the Land of Harmonia!" + colorama.Style.RESET_ALL)
    print("Main Area:", colorama.Fore.YELLOW + harmonia.name + colorama.Style.RESET_ALL)
    print(harmonia.description)
    print("\nSurrounding Regions:")
    for region in harmonia.neighbors:
        print("-", colorama.Fore.MAGENTA + region.name + colorama.Style.RESET_ALL + ":", region.description)
        if region.cities:
            print("  Cities:")
            for city in region.cities:
                print("   *", colorama.Fore.GREEN + city.name + colorama.Style.RESET_ALL + ":", city.description)
        if region.enemies:
            print("  Enemies:")
            for enemy in region.enemies:
                print("   X", colorama.Fore.RED + enemy.name + colorama.Style.RESET_ALL)
    print("\nBustling Cities in Harmonia:")
    for city in harmonia.cities:
        print(" *", colorama.Fore.GREEN + city.name + colorama.Style.RESET_ALL + ":", city.description)
    print(colorama.Fore.CYAN + "\nExplore, make friends, battle enemies, and find your musical path!" + colorama.Style.RESET_ALL)

# ----------- Usage -----------

print(colorama.Fore.RED + f"A wild {Boss.name} appears!" + colorama.Style.RESET_ALL)
print(colorama.Fore.RED + f"--------------------------------------" + colorama.Style.RESET_ALL)

# if __name__ == "__main__":
#     show_world_map()
#     # TODO: Add game loop, character creation, movement, battles, quests, etc.