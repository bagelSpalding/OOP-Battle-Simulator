import random


class Boss:

    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = 20

    def crit(self):
        if random.randint(0,50)%3==True:
            return random.randint(3,6)
        else:
            return 0

    def norm_attack(self):
        return random.randint(15, self.attack_power)

    def big_attack(self):
        rand=random.randint(1,3)
        crit_dmg=self.crit()
        dmg=random.randint(15,30)
        print(f"{self.name} uses a heavy attack")
        if rand==1:
            if crit_dmg>0:
                print(f"Critical Hit! {crit_dmg}+ damage done.")
                return(dmg+crit_dmg)
            return dmg
        else:
            print("Miss")
            return 0

    def boss_Armor(self):
        return random.randint(2,5)

    def take_damage(self, damage):
        armor=self.boss_Armor()
        dmg_actual=max(0,damage-armor)
        self.health = max(0, self.health - dmg_actual)
        print(f"{self.name} takes {damage} damage. Armor blocked {armor} damage Health: {self.health}")

    def is_alive(self):
        return self.health > 0
