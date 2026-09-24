import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 17
        self.level=1

    def crit(self):
        if random.randint(0,50)%3==True:
            
            return random.randint(3,6)
        else:
            return 0

    def attack(self):
        crit_dmg=self.crit()
        self.attack_power2=self.attack_power+crit_dmg
        if crit_dmg>0:
            print(f"{self.name} swings with their sword")
            print(f"Critical Hit! {crit_dmg}+ damage done.")
        else:
            print(f"{self.name} swings with their sword")
        return random.randint(5,self.attack_power2)

    def magic(self):
        rand=random.randint(0,50)
        crit_dmg=self.crit()
        print(f"{self.name} casts a spell")
        if rand%2==1 or rand%5==1 or rand%3==1:
            if crit_dmg>0:
                print(f"Critical Hit! {crit_dmg+crit_dmg}+ damage done.")
            return(random.randint(15,30)+crit_dmg+crit_dmg)
        else:
            print("Miss")
            return 0
            
        
    def hero_Armor(self):
        if random.randint(1,20)%2==True:
            return random.randint(1,3)
        else:
            return 0

    def take_damage(self, damage):
        armor=self.hero_Armor()
        dmg_actual=max(0,damage,armor)
        self.health = max(0, self.health - dmg_actual)
        print(f"{self.name} takes {damage} damage. Armor blocked {armor} damage. Health: {self.health}")

    def is_alive(self):
        return self.health>0


    pass
