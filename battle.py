from goblin import Goblin
from hero import Hero
from boss import Boss
import random


def battle(hero:Hero, enemy:Goblin, enemy2:Goblin):
    while hero.is_alive() and (enemy.is_alive() or enemy2.is_alive()):
        print("===========================")
        print("")


        rand=random.randint(1,3)
        rand2=random.randint(1,3)

        if enemy.is_alive():
            if rand==1 or rand==2:
                hero_damage=hero.attack()
                enemy.take_damage(hero_damage)
            else:
                hero_damage=hero.magic()
                enemy.take_damage(hero_damage)
        
        if enemy2.is_alive():
            if rand2==1 or rand2==2:
                hero_damage=hero.attack()
                enemy2.take_damage(hero_damage)
            else:
                hero_damage=hero.magic()
                enemy2.take_damage(hero_damage)

        
        if enemy.is_alive():
            enemy_damage=enemy.attack()
            hero.take_damage(enemy_damage)
        if  enemy2.is_alive():
            enemy2_damage=enemy2.attack()
            hero.take_damage(enemy2_damage)


    if hero.is_alive():
        print(f"{hero.name} has {hero.health} health remaining.")
        print(f"{hero.name} Wins!")
    else:
        print("DEFEATED")
        print(f"{enemy.name} and {enemy2.name} Win!")


def boss_battle(hero:Hero, boss:Boss):
        print("")
        print("===========================")
        hero.health=120
        print(f"{hero.name} has recovered from their injuries")

        print(" **THUD** ")
        print(" **THUD** ")
        print(" **THUD** ")
        print(f"The presence of the arena changes as {boss.name} enters")

        while hero.is_alive() and boss.is_alive():
            print("===========================")
            print("")


            rand=random.randint(1,3)
            rand2=random.randint(1,5)

            if boss.is_alive():
                if rand==1 or rand==2:
                    hero_damage=hero.attack()
                    boss.take_damage(hero_damage)
                else:
                    hero_damage=hero.magic()
                    boss.take_damage(hero_damage)

        
            if boss.is_alive():
                if rand2==1 or rand2==2 or rand2==3:
                    boss_damage=boss.norm_attack()
                    hero.take_damage(boss_damage)
                else:
                    boss_damage=boss.big_attack()
                    hero.take_damage(boss_damage)


        if hero.is_alive():
            print(f"{hero.name} has {hero.health} health remaining.")
            print(f"{hero.name} Wins!")
        else:
            print("DEFEATED")
            print(f"{boss.name} Wins!")