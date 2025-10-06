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

        def twoNoteChordSpells(self):
            self.minorSecond = chordSpells("Minor Second", 5)