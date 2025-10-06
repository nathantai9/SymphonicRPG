from classesandsuch import *

import colorama

import player
colorama.init()

# ----------- World Building -----------

# Main Land: Harmonia
harmonia = Region("Harmonia",
    "The heart of music magic, filled with rolling fields, festivals, and creative energy.")

# Sub-regions
dissonant_desert = Region("Dissonant Desert",
    "A harsh, sandy land where chaotic music rules and harmony is rare.")
string_haven = Region("String Haven",
    "A peaceful area famed for master violinists and magical string instruments.")
windwoodspire = Region("Windwoodspire",
    "Towering forests where wind musicians and flutists play melodies that travel for miles.")
brass_citadel = Region("Brass Citadel",
    "A fortified city where brass bands and trumpeters create powerful music.")
rhythmic_realms = Region("Rhythmic Realms",
    "Underground lands pulsing with drums, beats, and the spirit of rhythm.")

# Connect main regions
harmonia.neighbors = [dissonant_desert, string_haven, windwoodspire, brass_citadel, rhythmic_realms]

# Bustling cities for each region
harmonia.cities = [
    City("Melody Market", harmonia, "A bustling center for musicians, traders, and festivals."),
    City("Harmony Fields", harmonia, "Sweeping fields where music grows wild."),
    City("Festival Square", harmonia, "The biggest stage in all of Harmonia, always busy.")
]
dissonant_desert.cities = [
    City("Sandstorm City", dissonant_desert, "A city of wandering musicians and wild sound experiments.")
]
string_haven.cities = [
    City("Violin Village", string_haven, "Home to legendary string instrument makers."),
    City("Cello Crossing", string_haven, "A peaceful town by a river, famous for cello duels.")
]
windwoodspire.cities = [
    City("Flute Falls", windwoodspire, "A city built around waterfalls and flute music."),
    City("Whistling Woods", windwoodspire, "A town in the trees, always breezy and melodic.")
]
brass_citadel.cities = [
    City("Trumpet Town", brass_citadel, "The loudest city in Harmonia, famous for parades."),
    City("Horn Heights", brass_citadel, "High towers and echoing music halls.")
]
rhythmic_realms.cities = [
    City("Beat Borough", rhythmic_realms, "Underground city where drummers hold competitions."),
    City("Percussion Plaza", rhythmic_realms, "A gathering place for all things rhythm.")
]

# ----------- NPCs -----------

# NPCs (add more for each city)
harmonia.cities[0].npcs.append(NPC("Maestro Melody", "Festival Conductor", harmonia.cities[0]))
harmonia.cities[1].npcs.append(NPC)
string_haven.cities[0].npcs.append(NPC("Viola Virtuoso", "String Instructor", string_haven.cities[0]))
windwoodspire.cities[0].npcs.append(NPC("Flora Flutist", "Forest Guide", windwoodspire.cities[0]))
brass_citadel.cities[0].npcs.append(NPC("Sir Trumpet", "Parade Leader", brass_citadel.cities[0]))
rhythmic_realms.cities[0].npcs.append(NPC("DJ Beat", "Rhythm Champion", rhythmic_realms.cities[0]))

# ----------- Bosses -----------

dissonant_desert.bosses.append(Boss("Sand Siren", dissonant_desert, 4))
string_haven.bosses.append(Boss("Broken Bow", string_haven, 3))
windwoodspire.bosses.append(Boss("Wind Wraith", windwoodspire, 5))
brass_citadel.bosses.append(Boss("Brass Bully", brass_citadel, 6))
rhythmic_realms.bosses.append(Boss("Drum Demon", rhythmic_realms, 7))

def main():
    print("World building complete. Ready for expansion!")

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