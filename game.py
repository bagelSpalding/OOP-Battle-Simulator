from goblin import Goblin
from hero import Hero
from boss import Boss
from battle import battle
from battle import boss_battle
import random


ARENA_NAME = "The Cube of DOOM and DESPAIR"




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
    print("* * * * *")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    battle(hero, goblin, goblin2)
    if hero.is_alive():
        boss_battle(hero, boss)

    #heroAttack=hero.attack()
    #goblin.take_damage(heroAttack)
    #scribAtk=goblin2.attack()
    #goblin2.take_damage(heroAttack)
    #heroDamage=hero.take_damage(scribAtk)

if __name__ == "__main__":
    main()
