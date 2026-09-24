from goblin import Goblin
from hero import Hero
from boss import Boss
import random


ARENA_NAME = "The Cube of DOOM and DESPAIR"

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


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    goblin2=Goblin("Scribble Gibble the Majestic")
    hero=Hero("Kaleb the Silly")
    boss=Boss("Gorg the Almighty")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")
    print("")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    battle(hero, goblin, goblin2)

    #heroAttack=hero.attack()
    #goblin.take_damage(heroAttack)
    #scribAtk=goblin2.attack()
    #goblin2.take_damage(heroAttack)
    #heroDamage=hero.take_damage(scribAtk)

if __name__ == "__main__":
    main()
