# # SymphonicRPG - Harmonia World Building Template
# # High school level Python, ready for you to expand and fill in story, logic, and features!


import colorama
colorama.init()


# Example: Print a welcome message in green using colorama
print(colorama.Fore.GREEN + "Welcome to SymphonicRPG!" + colorama.Style.RESET_ALL)


# ----------- Data Structures -----------

class Region:
    def __init__(self, name, description, neighbors=None):
        self.name = name
        self.description = description
        self.neighbors = neighbors if neighbors else []
        self.cities = []
        self.npcs = []
        self.enemies = []

class City:
    def __init__(self, name, region, description):
        self.name = name
        self.region = region
        self.description = description
        self.npcs = []
        self.enemies = []

class NPC:
    def __init__(self, name, role, city, defaultdialogue="Hello!"):
        self.name = name
        self.role = role
        self.city = city
        self.defaultdialogue = defaultdialogue

class Boss: # add more attributes as needed
    def __init__(self, name, region, strength):
        self.name = name
        self.region = region
        self.strength = strength

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