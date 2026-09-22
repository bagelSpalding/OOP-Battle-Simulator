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
        print(f"{enemy.name} and {enemy2.name} Win!")