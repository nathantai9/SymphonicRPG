# website: https://www.tonegym.co/tool/item?id=chord-analyser&root=C&chord=major&inversion=0

class BattleItems:
    def __init__(self, name, damage, weight, description):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.description = description
    
    class damageSpSpells:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

        def keyOfCThreeNoteDmgSpellChords(self):
            self.CM = ("C Major", 25)
            self.Cm = ("C Minor", 27.5)
            self.Cdim = ("C Diminished", 30)
            self.Caug = ("C Augmented", 35)
            self.Csus2 = ("C Suspended 2nd", 37.5)
            self.Csus4 = ("C Suspended 4th", 38.7)
            self.Cb5 = ("C Flat 5th", 27.5)

        def keyOfCFourNoteDmgSpellChords(self):
            self.C7 = ("C Dominant 7th", 