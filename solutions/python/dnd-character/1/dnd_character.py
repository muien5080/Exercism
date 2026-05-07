import random
import math

class Character:
    def __init__(self):
        # The test expects a method called 'ability'
        # We call it here to set our attributes
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Rolls 4d6, drops lowest, returns sum (3-18)."""
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort()
        return sum(rolls[1:])

def modifier(value):
    """(Value - 10) / 2 rounded down."""
    return math.floor((value - 10) / 2)