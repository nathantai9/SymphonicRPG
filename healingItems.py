# self knowledge

class HealingItems:
    def __init__(self, name, healing_amount, weight, description):
        self.name = name
        self.healing_amount = healing_amount
        self.weight = weight
        self.description = description

    class healingSpells:
        def __init__(self, name, healing_amount):
                self.name = name
                self.healing_amount = healing_amount
            
        def healingSpellChords(self):
            self.minorSecond = ("Minor Second", 5) # deals 5 damage
            self.majorSecond = ("Major Second", 7.5) # deals 7.5 damage
            self.minorThird = ("Minor Third", 6.25) # deals 6.25 damage
            self.majorThird = ("Major Third", 8.75) # deals 8.75 damage
            self.perfectFourth = ("Perfect Fourth", 10)
            self.tritone = ("Tritone", 12.5)
            self.perfectFifth = ("Perfect Fifth", 15)
            self.minorSixth = ("Minor Sixth", 13.25)
            self.majorSixth = ("Major Sixth", 15.75)
            self.minorSeventh = ("Minor Seventh", 17.5)
            self.majorSeventh = ("Major Seventh", 20)
            self.octave = ("Octave", 50) 