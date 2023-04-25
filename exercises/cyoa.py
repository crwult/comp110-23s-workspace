<<<<<<< HEAD
"""Choose your own Adventure: Definately not pokemon."""
__author__: str = "730552290"

import random
TURTLE: str = "\U0001F422"
FIRE: str = "\U0001F525"
LIGHTNING: str = "\U0001F5F2"
GRASS: str = "\U0001318F"
points: int = 0
player: str = ""
starter: int = 0


def main() -> None:
    """Runs the program."""
    greet()
    choose_pokemon()
    print(f"Game over, your score is {game_loop()}.")
    
    
def greet() -> None:
    """Gets player name and intorduces them to game."""
    global player
    print("Welcome to Kopemon, a game that is nothing like the popular video game series pokemon.")
    player = str(input("What is your name young handler? "))


def choose_pokemon() -> None:
    """Pick which Pokemon you will be using."""
    global starter
    global TURTLE
    global FIRE
    global LIGHTNING
    global GRASS
    starter = int(input(f"Really? {player}, thats an ... interesting name. Choose your starter kopemon. \n1. Fire Lizard \n2. Grass Frog \n3. a turtle\n"))
    while type(starter) != int:
        starter = input("choose the number listed before the kopemon")
    if starter == 1:
        print(f"You chose Fire Lizard {FIRE}!")
    elif starter == 2:
        print(f"You chose Grass Frog {GRASS}!")
    elif starter == 3:
        print(f"You chose a turtle {TURTLE}!")
    else:
        print(f"You were supposed to pick 1-3. Heres a rat \nYou got electro rat {LIGHTNING}!")


def game_loop() -> int:
    """Creates a loop where the player chooses a fight, a boss fight or to run away."""
    playing: int = 0
    global starter
    global points
    global player
    fight_number: int = 1
    boss_fight_number: int = 1
    level: int = 0 
    while playing == 0:
        print(f"Your kopemon is level {level}")
        fof: int = int(input("Do you want to \n1. Give up \n2. Fight a normal fight \n3. Fight a boss"))
=======
"""Choose your own Adventure: Definately not pokemon"""
__author__ = "730552290"

turtle: str = "\U0001F422"
fire: str = "\U0001F525"
lightning: str = "\U0001F5F2"
grass: str = "\U0001318F"
import random
points: int = 0
player: str = ""
starter: int = 0
def main() -> None:
    """Runs the program"""
    global points
    points = 0
    greet()
    print(f"Game over, your score is {game_loop()}.")
    
    

def greet() -> None:
    """Gets player name and intorduces them to game"""
    global player
    global starter
    global turtle
    global fire
    global lightning
    global grass
    player = str(input("Welcome to Kopemon, a game that is nothing like the popular video game series pokemon. \nWhat is your name young handler? "))
    starter = int((input(f"Really? {player}, thats an ... interesting name. Choose your starter kopemon. \n1. Fire Lizard \n2. Grass Frog \n3. a turtle\n")))
    while (starter < 1) or (starter > 4):
        starter = int(input("choose the number listed before the kopemon"))
    if starter == 1:
        print(f"You chose Fire Lizard {fire}!")
    if starter == 2:
        print(f"You chose Grass Frog {grass}!")
    if starter == 3:
        print(f"You chose a turtle {turtle}!")
    if starter == 4:
        print(f"You weren't supposed to pick 4. Heres a rat \nYou got electro rat {lightning}!")

def game_loop() -> int:
    "Creates a loop where the player chooses a fight, a boss fight or to run away"
    playing = True
    global starter
    global points
    global player
    fight_number = 1
    boss_fight_number = 1
    level = 0 
    while playing == True:
        print(f"Your kopemon is level {level}")
        fof = int(input("Do you want to \n1. Give up \n2. Fight a normal fight \n3. Fight a boss"))
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        while (fof < 1) or (fof > 3):
            fof = int(input("choose the number listed before the option"))
        if fof == 2:
            points += fight(points, starter, fight_number, level, player)
            fight_number += 1
            level += 2
        if fof == 3:
            boss_fight(points, starter, boss_fight_number, level, player)
            fight_number += 1
            level += 3
        if fof == 1:
<<<<<<< HEAD
            playing = 1
=======
            playing = False
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        print(f"Your score is {points}")
    return points


def fight(fight_points: int, kop: int, fight_num: int, fight_level: int, player_name: str) -> int:
    """Runs the fight."""
    if kop == 1:
        starter_name: str = "Fire Lizard"
<<<<<<< HEAD
        max_health = 80 + 2 * fight_level
        attack = 120 + 2 * fight_level
    elif kop == 2:
        starter_name: str = "Grass Frog"
        max_health = 100 + fight_level
        attack = 100 + fight_level
    elif kop == 3:
        starter_name: str = "a turtle"
        max_health = 120 + fight_level
        attack = 80 + fight_level
    else:
=======
        max_health = 80 + 2 *fight_level
        attack = 120 + 2* fight_level
    if kop == 2:
        starter_name: str = "Grass Frog"
        max_health = 100 + fight_level
        attack = 100 + fight_level
    if kop == 3:
        starter_name: str = "a turtle"
        max_health = 120 + fight_level
        attack = 80 + fight_level
    if kop == 4:
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        starter_name: str = "Electro rat"
        max_health = 80 + fight_level
        attack = 120 + fight_level
    health: int = max_health
<<<<<<< HEAD
    enemies: list[str] = ["Worm", "Conjoined Ostriches", "Firefox", "Ghost Ball", "Raddish", "Sentient Noodles", "EGGS", "Short Monkey", "Spiky Snail", "Ice Seal", "Snorlax"]
    opponent: str = random.choice(enemies)
    o_max_health: int = 80 + 12 * fight_num
    o_attack: int = 80 + 12 * fight_num
    o_health: int = o_max_health
=======
    enemies = ["Worm", "Conjoined Ostriches", "Firefox", "Ghost Ball", "Raddish", "Sentient Noodles", "EGGS", "Short Monkey", "Spiky Snail", "Ice Seal", "Snorlax"]
    opponent = random.choice(enemies)
    o_max_health = 80 + 12 * fight_num
    o_attack = 80 + 12 * fight_num
    o_health = o_max_health
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
    while (o_health >= 0) and (health >= 0):
        print(f"\n                 Fight {fight_num}: {starter_name} vs {opponent}")
        print(f"{starter_name} health: {health}/{max_health}              {opponent} health: {o_health}/{o_max_health}")
        print(f"{starter_name} attack: {attack}                  {opponent} attack: {o_attack}")
<<<<<<< HEAD
        move: int = int(input(f"{player_name}, what move do you want to make \n1. Heal \n2. Attack\n3. Attack boost \n4. Point boost"))
=======
        move = int(input(f"{player_name}, what move do you want to make \n1. Heal \n2. Attack\n3. Attack boost \n4. Point boost"))
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        while (move < 1) or (move > 4):
            move = int(input("choose the number listed before the option"))
        if move == 1:
            if health <= int(.8 * max_health):
                health += int(.2 * max_health)
            else:
                health = max_health 
            print(f"{starter_name} used HEAL")
        if move == 2:
            o_health -= int(attack * .25)
            print(f"{starter_name} used ATTACK")
        if move == 3:
            attack += 5
            print(f"{starter_name} used ATTACK BOOST")
        if move == 4:
            fight_points += 100
            print(f"{starter_name} used POINT BOOST")
        o_move = random.randint(1, 6)
        if o_move == 1:
            if o_health <= int(.8 * o_max_health):
                o_health += int(.2 * o_max_health)
            else:
                o_health = o_max_health 
            print(f"{opponent} used HEAL")
        if (o_move == 2) or (o_move == 5) or (o_move == 6):
            health -= int(o_attack * .25)
            print(f"{opponent} used ATTACK")
        if o_move == 3:
            o_attack += 5
            print(f"{opponent} used ATTACK BOOST")
        if o_move == 4:
            print(f"{opponent} fell down")
        print("")
    if o_health <= 0:
        print(f"{opponent} fainted. You gained 1000 points")
        fight_points += 1000
    else:
        print(f"{starter_name} fainted. You lost")
<<<<<<< HEAD
    return (fight_points)
=======
    return(fight_points)





>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80


def boss_fight(fight_points: int, kop: int, boss_fight_num: int, fight_level: int, player_name: str) -> int:
    """Runs the fight."""
    global points
    if kop == 1:
        starter_name: str = "Fire Lizard"
        max_health = 80 + fight_level
        attack = 120 + fight_level
<<<<<<< HEAD
    elif kop == 2:
        starter_name: str = "Grass Frog"
        max_health = 100 + fight_level
        attack = 100 + fight_level
    elif kop == 3:
        starter_name: str = "a turtle"
        max_health = 120 + fight_level
        attack = 80 + fight_level
    else:
=======
    if kop == 2:
        starter_name: str = "Grass Frog"
        max_health = 100 + fight_level
        attack = 100 + fight_level
    if kop == 3:
        starter_name: str = "a turtle"
        max_health = 120 + fight_level
        attack = 80 + fight_level
    if kop == 4:
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        starter_name: str = "Electro rat"
        max_health = 80 + fight_level
        attack = 120 + fight_level
    health: int = max_health
<<<<<<< HEAD
    enemies: list[str] = ["Ice Bird", "God", "Rocky Kangaroo", "a Creepy Mime", "Big Pile of Mud", "Palm Tree With Googly Eyes", "Regular Pterodactyl", "Blue Dinosaur", "Purple Dinosaur", "4-Armed Bodybuilder", "3 Moles"]
    opponent: str = random.choice(enemies)
    o_max_health: int = 80 + 36 * boss_fight_num
    o_attack: int = 80 + 36 * boss_fight_num
    o_health: int = o_max_health
=======
    enemies = ["Ice Bird", "God", "Rocky Kangaroo", "a Creepy Mime", "Big Pile of Mud", "Palm Tree With Googly Eyes", "Regular Pterodactyl", "Blue Dinosaur", "Purple Dinosaur", "4-Armed Bodybuilder", "3 Moles"]
    opponent = random.choice(enemies)
    o_max_health = 80 + 36 * boss_fight_num
    o_attack = 80 + 36 * boss_fight_num
    o_health = o_max_health
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
    while (o_health >= 0) and (health >= 0):
        print(f"\n              Boss Fight {boss_fight_num}: {starter_name} vs {opponent}")
        print(f"{starter_name} health: {health}/{max_health}              {opponent} health: {o_health}/{o_max_health}")
        print(f"{starter_name} attack: {attack}                  {opponent} attack: {o_attack}")
<<<<<<< HEAD
        move: int = int(input(f"{player_name}, what move do you want to make? \n1. Heal \n2. Attack\n3. Attack boost \n4. Point boost"))
=======
        move = int(input(f"{player_name}, what move do you want to make? \n1. Heal \n2. Attack\n3. Attack boost \n4. Point boost"))
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        while (move < 1) or (move > 4):
            move = int(input("choose the number listed before the option"))
        if move == 1:
            if health <= int(.8 * max_health):
                health += int(.2 * max_health)
            else:
                health = max_health 
            print(f"{starter_name} used HEAL")
        if move == 2:
            o_health -= int(attack * .25)
            print(f"{starter_name} used ATTACK")
        if move == 3:
            attack += 5
            print(f"{starter_name} used ATTACK BOOST")
        if move == 4:
            points += 100
            print(f"{starter_name} used POINT BOOST")
<<<<<<< HEAD
        o_move: int = random.randint(1, 6)
=======
        o_move = random.randint(1, 6)
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        if o_move == 1:
            if o_health <= int(.8 * o_max_health):
                o_health += int(.2 * o_max_health)
            else:
                o_health = o_max_health 
            print(f"{opponent} used HEAL")
        if (o_move == 2) or (o_move == 5) or (o_move == 6):
            health -= int(o_attack * .25)
            print(f"{opponent} used ATTACK")
        if o_move == 3:
            o_attack += 5
            print(f"{opponent} used ATTACK BOOST")
        if o_move == 4:
            print(f"{opponent} fell down")
        print("")
    if o_health <= 0:
        print(f"{opponent} fainted. You gained 3000 points \n You have beat the boss!")
        points += 3000
    else:
        print(f"{starter_name} fainted. You lost")
<<<<<<< HEAD
 
=======


    
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80

if __name__ == "__main__":
    main()