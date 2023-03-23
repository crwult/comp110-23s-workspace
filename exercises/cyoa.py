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
            playing = False
        print(f"Your score is {points}")
    return points


def fight(fight_points: int, kop: int, fight_num: int, fight_level: int, player_name: str) -> int:
    """Runs the fight."""
    if kop == 1:
        starter_name: str = "Fire Lizard"
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
        starter_name: str = "Electro rat"
        max_health = 80 + fight_level
        attack = 120 + fight_level
    health: int = max_health
    enemies = ["Worm", "Conjoined Ostriches", "Firefox", "Ghost Ball", "Raddish", "Sentient Noodles", "EGGS", "Short Monkey", "Spiky Snail", "Ice Seal", "Snorlax"]
    opponent = random.choice(enemies)
    o_max_health = 80 + 12 * fight_num
    o_attack = 80 + 12 * fight_num
    o_health = o_max_health
    while (o_health >= 0) and (health >= 0):
        print(f"\n                 Fight {fight_num}: {starter_name} vs {opponent}")
        print(f"{starter_name} health: {health}/{max_health}              {opponent} health: {o_health}/{o_max_health}")
        print(f"{starter_name} attack: {attack}                  {opponent} attack: {o_attack}")
        move = int(input(f"{player_name}, what move do you want to make \n1. Heal \n2. Attack\n3. Attack boost \n4. Point boost"))
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
    return(fight_points)







def boss_fight(fight_points: int, kop: int, boss_fight_num: int, fight_level: int, player_name: str) -> int:
    """Runs the fight."""
    global points
    if kop == 1:
        starter_name: str = "Fire Lizard"
        max_health = 80 + fight_level
        attack = 120 + fight_level
    if kop == 2:
        starter_name: str = "Grass Frog"
        max_health = 100 + fight_level
        attack = 100 + fight_level
    if kop == 3:
        starter_name: str = "a turtle"
        max_health = 120 + fight_level
        attack = 80 + fight_level
    if kop == 4:
        starter_name: str = "Electro rat"
        max_health = 80 + fight_level
        attack = 120 + fight_level
    health: int = max_health
    enemies = ["Ice Bird", "God", "Rocky Kangaroo", "a Creepy Mime", "Big Pile of Mud", "Palm Tree With Googly Eyes", "Regular Pterodactyl", "Blue Dinosaur", "Purple Dinosaur", "4-Armed Bodybuilder", "3 Moles"]
    opponent = random.choice(enemies)
    o_max_health = 80 + 36 * boss_fight_num
    o_attack = 80 + 36 * boss_fight_num
    o_health = o_max_health
    while (o_health >= 0) and (health >= 0):
        print(f"\n              Boss Fight {boss_fight_num}: {starter_name} vs {opponent}")
        print(f"{starter_name} health: {health}/{max_health}              {opponent} health: {o_health}/{o_max_health}")
        print(f"{starter_name} attack: {attack}                  {opponent} attack: {o_attack}")
        move = int(input(f"{player_name}, what move do you want to make? \n1. Heal \n2. Attack\n3. Attack boost \n4. Point boost"))
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
        print(f"{opponent} fainted. You gained 3000 points \n You have beat the boss!")
        points += 3000
    else:
        print(f"{starter_name} fainted. You lost")


    

if __name__ == "__main__":
    main()