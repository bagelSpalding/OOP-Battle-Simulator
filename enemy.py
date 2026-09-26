import random


class Goblin:

    def __init__(self, name, health=50, attack_power=7):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.full_flinch = False
        self.half_flinch = False

    def attack(self):
        gabbo_damage=random.randint(1, self.attack_power)

        if self.full_flinch:
            gabbo_damage = 0
            self.full_flinch = False
            print(f"{self.name} flinched and could not attack!")
            return gabbo_damage
        
        if self.half_flinch:
            gabbo_damage = gabbo_damage // 2
            self.half_flinch = False
            print(f"{self.name}'s attack was halved!")
            return gabbo_damage
        else:
            return gabbo_damage

    def gabbo_Armor(self):
        return random.randint(0,3)

    def full(self):
        self.full_flinch=True
        print(f"{self.name} flinched!")

    def half(self):
        self.half_flinch=True
        print(f"{self.name} flinched!")

    def take_damage(self, damage):
        armor=self.gabbo_Armor()
        dmg_actual=max(0,damage-armor)
        self.health = max(0, self.health - dmg_actual)
        print(f"{self.name} takes {damage} damage. Armor blocked {armor} damage Health: {self.health}")

    def is_alive(self):
        return self.health > 0
