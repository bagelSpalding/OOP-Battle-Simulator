import random


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def gabbo_Armor(self):
        return random.randint(0,3)

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage+self.gabbo_Armor())
        print(f"{self.name} takes {damage} damage. Armor blocked {self.gabbo_Armor()} damage Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
