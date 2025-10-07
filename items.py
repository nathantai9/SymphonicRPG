# website: https://www.tonegym.co/tool/item?id=chord-analyser&root=C&chord=major&inversion=0

class BattleItems:
    def __init__(self, name, damage, weight, description):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.description = description
    
    class chordSpells:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

        def threeNoteChordSpells(self):
            self.CM = ("C Major", 25) # deals 25 damage
            self.Cm = ("C Minor", 22.5) # deals 22.5 damage
            self.Cdim = ("C Diminished", 30) # deals 30 damage
            self.Caug = ("C Augmented", 35) # deals 35 damage
            self.Csus2 = ("C Suspended 2nd", 20) # deals 20 damage
            self.Csus4 = ("C Suspended 4th", 20) # deals 20 damage
            self.Cb5 = ("C Flat 5th", 27.5) # deals 27.5 damage

class HealingItems:
    def __init__(self, name, healing_amount, weight, description):
        self.name = name
        self.healing_amount = healing_amount
        self.weight = weight
        self.description = description

        def Spells(self, name, healing_amount):
            self.name = name
            self.healing_amount = healing_amount

        class healingSpells:
            def twoNoteChordSpells(self):
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