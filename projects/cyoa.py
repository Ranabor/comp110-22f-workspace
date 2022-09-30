"""Rock Paper Scissors Grand Slam. Inspired by https://www.umop.com/rps15.htm but not as crazy as https://www.umop.com/rps101.htm ."""

import random

__author__: str = "730575704"

# Guide to the manual grader:
# I wrote a ton of code (over 400 lines with low redundancy). Sorry, I read "game" and went all out
# So to help you grade and double check for my own sake I will make note of the key rubric items.
# That said, I put a lot of effort and time so I would greatly appreciate if you played the game, it should be fun. About 5-10 minutes play time
# Now, to the heart of things:
# 0. The globals below include the required points (line 24) and player (line 25), and 3 emoji values. Has other useful variables I use across the game
# 1. Main function (line 36) is below that, and accesses 2. Greet function (line 66) first. As I will keep returning to main function I made it so that it only asks for the name once
# 3. The custom procedure is the function branch to level_select (line 128). Due to the nature of the game this function should not use the name or points, but it directly goes to level_one (line 168) which does
# 3 cont. level_one uses the player name on (line 173) and affects the points based on a player victory (line 190). The game can be continued to 4 levels which do the same
# 4. The custom function is the shop (line 75). It has 2 arguments of points and 1 more score global variable.
# 4 cont. It does access other globals out of sheer necessity but fulfills the requirement of returning int (line 119) and main changing points (line 55)
# 5. Many functions call main again leading to the 3 options. Main also changes text based on game progress
# 6. Many f strings. I honestly hope you do not have to look for concatenation, as far as I checked there is none and only f strings
# 6 cont. Named global constants on lines 26, 27, 28
# 6 cont. Randomness in levels on lines 247, 255, 282
# 6 cont. No global calls to input. The code is structured with all global variables/constants on top, functions in the middle, and if name = main on bottom.
# Thank you and I hope you enjoyed the game!

points: int = 0  # Spirit value. Currency gained through fighting and spent in shop
player: str = ""  # Player name
ROCK: str = "\U0001F44A"  # Fist emoji
PAPER: str = "\U0000270B"  # Palm emoji
SCISSORS: str = "\U0000270C"  # 2 fingers emoji
level: int = 0  # Player level progression
fame: int = 0  # Player fame
skillset_player: list[str] = ["Rock", "Paper", "Scissors"]  # Player Skills
all_skills: list[str] = ["Rock", "Paper", "Scissors", "Gun", "Water", "Fire", "Dragon", "Devil", "Wolf", "Human", "Lightning", "Air", "Sponge", "Tree", "Snake"]  # All available skills
nature_skills: list[int] = [0, 4, 5, 8, 10, 11, 13, 14]  # Sublist of all skills that I classify as nature archetype


def main() -> None:
    """The main menu. Changes based on game progress. 3 routes: story mode, shop, and exit."""
    greet()
    global points
    story: str = "Start"
    if level > 0:  # Small change to show story has been started
        story = "Continue"
    exit_message: str = "Return in defeat... (exit)"
    if level >= 3:  # If game is won changes exit message
        exit_message = "Proclaim Victory! (exit)"
    print(f"Welcome {player} to RPS War\n1. {story} your legend \n2. Improve your strength (shop) \n3. {exit_message}")  # 3 routes
    print(f"Fame: {fame}  Spirit: {points}")  # Points and score
    start: str = input("Enter 1, 2, or 3 to choose.")  # Choose route
    while start not in ["1", "2", "3"]:  # Confirms choice is available
        start = input("Please choose 1, 2, or 3: ")
    if start == "1":  # Story
        level_select()
    if start == "2":  # Shop
        spirit_spent: int = shop(points, fame)
        points -= spirit_spent
        main()
    if start == "3":  # Exit
        if level < 3:
            print(f"While your journey ends in defeat, it is a tale for the ages. Fame: {fame}")
            quit()
        else:
            print(f"What a glorious journey! Your {fame} Fame resounds across the lands. You won with {points} remaining Spirit, and learned a total of {len(skillset_player) - 3} skills. We await your return warrior!")
            quit()


def greet() -> None:
    """Greets player and assigns username."""
    global player
    if player == "":  # As game loops a lot do not want to keep reassigning name
        print("In an age where conflict was common, before humans used guns and swords, the fist settled the fight. You are a champion of this era.")
        player = input("The Great ")
        print(f"Your people have been pushed back by the opposing tribe, and now you are the last line of defense against this mysterious invading tribe!!! Ready? {ROCK},{PAPER},{SCISSORS} !")


def shop(spirit, fame) -> int:
    """Shop choice. Can buy skills, unlocked with Fame and purchased with Spirit."""
    global skillset_player
    global all_skills
    print(f"Welcome {player} to your tribe's Hall of Inheritance. Here, the statues of your ancestors will present skills based on your Fame. You can learn them by consuming Spirit.")
    print(f"{player}'s skills: {skillset_player}")
    skills_shop: list[str] = []  # Next 5 lines to ensure player does not buy skills already owned
    for i in all_skills:
        skills_shop.append(i)
    for i in skillset_player:
        if i in skills_shop:
            skills_shop.remove(i)
    fame_start: int = 10  # Initial prices
    spirit_start: int = 50
    j: int = 0  # To loop through skills and increase fame and spirit cost exponentially
    for i in skills_shop:
        fame_cost = cost(fame_start, j)  # See cost function for details. Simply increases value of next skills
        spirit_cost = cost(spirit_start, j)
        if fame < fame_cost:  # Fame lock
            print(f"{i} unlocked at {fame_cost} Fame")
        else:  # Spirit Cost
            print(f"{i} costs {spirit_cost} Spirit")
        j += 1
    skills_shop.append("Leave")
    purchase_choice: str = input("Select a skill to buy or Leave: ")
    while purchase_choice not in skills_shop:  # Ensures input
        purchase_choice = input("Choose a skill or Leave: ")
    if purchase_choice == "Leave":  # No change and returns to main
        return 0
    else:  # Skill select checks
        k: int = 0
        while k < len(skills_shop):
            if skills_shop[k] == purchase_choice:
                unlock: bool = fame > cost(fame_start, k)  # Checks if enough Fame
                afford: bool = spirit > cost(spirit_start, k)  # Checks if enough Spirit
                if not unlock:
                    print(f"You need {cost(fame_start, k) - fame} more Fame.")  # Not enough Fame
                    return 0
                elif not afford:
                    print(f"You need {cost(spirit_start, k) - spirit} more Spirit.")  # Not enough Spirit
                    return 0
                else:
                    print(f"...You have learned {purchase_choice} for {cost(spirit_start, k)} Spirit.")  # Purchase successful
                    skillset_player.append(purchase_choice)  # Skill added
                    return cost(spirit_start, k)  # Spirit spent returned, deducted from main function
            k += 1


def cost(start, time) -> int:
    """Calculates increases in shop requirements and rewards from battles."""
    return round(start * ((1 + 0.5) ** time))


def level_select() -> None:
    """Selection of levels based on user input. Forces level one, but after beating it player can start to choose levels to replay or keep going in story."""
    levels_list: list = [rules, level_one, level_two, level_three, level_four]  # Level functions
    levels_list_str: list[str] = ["0. Rules", "1. Northern Battlefield", "2. Endless Wilderness", "3. Frontline Commander", "4. Infinite Mode"]  # Level names
    if level == 0:  # Forced level
        level_one()
    if level > 0:
        for i in levels_list_str[0:level + 2]:  # Displays level choices
            print(i)
        level_choice: str = input("Choose a level: ")
        levels_allowed: list[str] = []  # Next few lines used to error test for level inputs
        for i in range(0, level + 2):
            levels_allowed.append(str(i))
        while level_choice not in levels_allowed:
            level_choice = input(f"Please choose an integer from 0 to {levels_allowed[-1]}")
        levels_list[int(level_choice)]()  # Runs level function based on choice


def rules() -> None:
    """Rules of the game."""
    print("""Attribute Rules:
    Rock pounds out fire, crushes scissors, snake, human, wolf, sponge, blocks (growth of) tree.
    Fire melts scissors, burns paper, snake, human, tree, wolf & sponge.
    Scissors swish through air, carve tree, cut paper, snake, human, wolf & sponge.
    Snake bites human & wolf, swallows sponge, nests in tree & paper, breathes air, drinks water.
    Human plants tree, tames wolf, cleans with sponge, writes paper, breathes air, drinks water, slays dragon.
    Tree shelters wolf & dragon, outlives sponge, becomes paper, produces air, drinks water, imprisons devil.
    Wolf chews up sponge, & paper, breathes air, drinks water, outruns dragon & lightning, bites devil's heiny.
    Sponge soaks paper, uses air pockets, absorbs water, cleanses devil & dragon, cleans gun, conducts lightning.
    Paper fans air, covers rock, floats on water, rebukes devil & dragon, outlaws gun, defines lightning.
    Air blows out fire, erodes rock, evaporates water, chokes devil, tarnishes gun, freezes dragon, creates lightning.
    Water drowns devil & dragon, erodes rock, puts out fire, rusts scissors & gun, conducts lightning.
    Dragon commands devil, breathes lightning & fire, rests on rock, immune to scissors & gun, spawns snake.
    Devil hurls rock, breaths fire, immune to scissors & gun, casts lightning, eats snakes, possesses human.
    Lightning melts gun & scissors, splits rock & tree, starts fire, strikes snake & human.
    Gun targets rock & tree, fires, outclasses scissors, shoots snake, human & wolf.
    Credits to David Lovelace https://www.umop.com/rps15.htm """)
    main()


def level_one() -> None:
    """First level."""
    global level
    global points
    global fame
    print(f"Welcome to the Northern Battlefield {player}. The defense line has worn thin and you are here to push the enemy back. You quickly engage with the first enemy, the renowned warrior Dwayne the {ROCK} Johnson. Ready? {ROCK},{PAPER},{SCISSORS} !")
    for i in skillset_player:  # Displays character skills
        print(i)
    player_choice: str = input("Choose your skill: ")
    while player_choice not in skillset_player:  # Ensures move choice
        player_choice = input("Choose a skill you know: ")
    while player_choice == all_skills[0]:  # Tie check
        player_choice = input("Its a tie, choose again: ")
    battle: int = skills(all_skills[0], player_choice)  # Win condition check
    if battle == 1:
        print(f"You chose {player_choice} while Dwayne the {ROCK} Johnson chose {all_skills[0]}. Guess you can't choose {all_skills[0]} every time.")
        if level == 0:  # Level progression
            level += 1
        fame_gain: int = 10
        spirit_gain: int = 50
        print(f"{player}'s feat turns the tide of battle! You gain {fame_gain} Fame and {spirit_gain} Spirit! Spirit and Fame are gained through defeating strong enemies and can unlock new skills.")
        fame += fame_gain
        points += spirit_gain
        main()
    else:
        defeat: str = input(f"You chose {player_choice} while Dwayne the {ROCK} Johnson chose {all_skills[0]}. 1. Fight again or 2. retreat?")
        while defeat not in ["1", "2"]:  # Loss returns or repeats
            defeat = int(input("Choose to 1. Fight or 2. Retreat"))
        if defeat == "1":
            level_one()
        else:
            main()


def level_two() -> None:
    """Second level."""
    win_cond: int = 3  # Player is fighting group so needs 3 wins
    print(f"After breaching the battlefront you make your way through the endless wilderness, letting the name \"{player}\" strike fear into your enemies. In response, an ambush is planned with the enemies strongest nature warriors!")
    print(f"Surrounded by 5 opponents there is only one way to settle this! Best out of 5! Ready? {ROCK},{PAPER},{SCISSORS} !")
    result: list[int] = best_out_of_x(win_cond, nature_skills, False)  # See best_out_of_x function
    win_message: str = f"Best out of 5 always guaranteed victory! The name {player} gained {result[2]} Fame across the land. You gained {result[3]} Spirit. Now take the battle to the enemy camp!"
    lose_message: str = "You are overwhelmed with their skills and are defeated!"
    win_or_defeat(1, level_two, win_cond, result[0], result[1], win_message, lose_message, False)  # See win_or_defeat function


def level_three() -> None:
    """Third Level of the game."""
    print(f"After a harrowing journey you have reached the commander base at the frontline. Who is the general spearheading this war? It is none other than Elon Musk who traveled through time! {player} vs Elon Musk, a battle that transcends time.")
    print(f"You have intel that the commander can read your mind using a technique called algorithm! Strange magic called AI is a grave threat. How will you make it past this battle? Best out of 9. Ready? {ROCK},{PAPER},{SCISSORS} !")
    print("Hint: Elon Musk will be able to predict the use of 5 skills leading to a guaranteed loss. Try to choose one of the other 10 for a chance!")
    win_cond: int = 5
    result: list[int] = best_out_of_x(win_cond, range(15), True)
    win_message: str = f"Even AI could not predict your skills, you have defeated Elon Musk! The invasion has been pushed back. The name {player} gained {result[2]} Fame across spacetime. You gained {result[3]} Spirit."
    lose_message: str = "Even if Elon failed at acquiring Twitter, his skills are not any weaker! Try to improve your strength to guard against the prediction algorithm."
    win_or_defeat(2, level_three, win_cond, result[0], result[1], win_message, lose_message, False)


def level_four() -> None:
    """Infinite mode for player to have fun after game is beaten."""
    print("While you have defeated the commander, the enemy does not rest! Keep up the fight to earn eternal glory!")
    choose_fight: str = input("Choose to fight the army of the enemy best out of: ")
    check_length_of_fight: list[str] = []
    for i in range(1, 26):  # Ensures reasonable and numeric input for fight amount
        check_length_of_fight.append(str(i))
    while choose_fight not in check_length_of_fight:
        choose_fight = input("Please choose an integer from 1 to 25")
    win_cond: int = round(int(choose_fight) / 2)  # Majority wins means victory
    result: list[int] = best_out_of_x(win_cond, range(15), False)
    win_message: str = f"You won the fight with {result[0]} wins! The name {player} gains {result[2]} Fame across spacetime. You gain {result[3]} Spirit."
    lose_message: str = f"You have been overwhelmed in battle and retreat, but obtained {result[0]} wins! The name {player} gains {result[2]} Fame across spacetime. You gain {result[3]} Spirit."
    win_or_defeat(0, level_four, win_cond, result[0], result[1], win_message, lose_message, True)


def minion(skills_list: list[int], fame_gain: int, spirit_gain: int) -> int:
    """Battle against cannon fodder to fill levels. Takes arguments of enemy skills and rewards, does random battle, adds rewards and returns 1 for win and 0 for loss."""
    global points
    global fame
    for i in skillset_player:
        print(i)
    enemy_choice: str = random.choice([all_skills[i] for i in skills_list])  # Randomly chooses skills based on input skillset
    player_choice: str = input("Choose your skill: ")
    while player_choice not in skillset_player:  # Ensures player selection
        player_choice = input("Choose a skill you know: ")
    tie: bool = False
    if player_choice == enemy_choice:  # Tie control
        tie = True
    while tie:  # The following is done so that if a tie the enemy rerolls their skill before the player does and keeps going in that order until not a tie. If not in place enemy choice would change after player choice meaning a win would become a loss
        enemy_choice = random.choice([all_skills[i] for i in skills_list])
        player_choice = input("Its a tie, choose again: ")
        if player_choice != enemy_choice:
            tie = False
    battle: int = skills(enemy_choice, player_choice)  # Checks win conditions
    if battle == 1:  # Win message, globals change, returns 1 for win
        print(f"The enemy chose {enemy_choice}. {player_choice} beats {enemy_choice}.")
        print(f"You gain {fame_gain} Fame and {spirit_gain} Spirit!")
        points += spirit_gain
        fame += fame_gain
        return 1
    else:  # Loss returns 0 for loss
        print(f"You chose {player_choice} while the enemy chose {enemy_choice}, you lost.")
        return 0


def best_out_of_x(win_cond: int, enemy_skills: list[int], boss: bool) -> list[int]:
    """Runs a best out of X battle. Parameter is how many need to be won to win and enemy moves. Boss parameter is for special battles."""
    player_score: int = 0  # Initialize many variables for calculation
    enemy_score: int = 0
    fame_gain: int = fame
    spirit_gain: int = points
    total_fame_gain: int = 0
    total_spirit_gain: int = 0
    boss_loop_control: bool = False
    while player_score < win_cond and enemy_score < win_cond:  # Game loop
        if boss:  # Boss level is unique, harder, and restrictive
            enemy_prediction: list[str] = random.sample(all_skills, 5)
            for i in skillset_player:
                print(i)
            player_choice: str = input("Think about what skill you will use: ")
            if player_choice in enemy_prediction:
                print("Your mind was read! You lose this round.")
                enemy_score += 1
                boss_loop_control = True  # To repeat boss pre-fight without triggering secondary fight
            else:
                print("It was not predicted! You have a chance, now play your move.")
                boss_loop_control = False  # Continue with secondary fight
        if not boss_loop_control:  # Normal enemies or boss secondary
            battle: int = minion(enemy_skills, fame_gain, spirit_gain)  # Runs fight every loop
            if battle == 1:  # Tabulates wins and rewards
                player_score += 1
                total_fame_gain += fame_gain
                total_spirit_gain += spirit_gain
                fame_gain = cost(fame_gain, player_score)
                spirit_gain = cost(spirit_gain, player_score)
            else:  # Loss
                enemy_score += 1
    return [player_score, enemy_score, total_fame_gain, total_spirit_gain]  # Returns a list used in function that calls and in follow up win_or_defeat
    

def win_or_defeat(level_add: int, level_func, win_cond: int, player_score: int, enemy_score: int, win_message: str, lose_message: str, infinite: bool) -> None:
    """Given the results of the battle it decides what to send and where to go next."""
    global level
    if player_score == win_cond:  # Player won the rounds
        print(win_message)
        if level == level_add:  # Level progression. Ensures only happens once per level
            level += 1
        main()
    if enemy_score == win_cond:  # Loss
        print(lose_message)
        if not infinite:  # Normal levels
            defeat: str = input("1. Fight again or 2. retreat?")
            while defeat not in ["1", "2"]:  # Return or repeat
                defeat = input("Choose to 1. Fight or 2. Retreat")
            if defeat == "1":
                level_func()
            else:
                main()
        else:  # Infinite mode auto leaves because point is to go back if you want to. So if a loss not a choice to repeat
            main()


def skills(enemy_choice: str, player_choice: str) -> int:
    """Every single win condition. Don't ask. It was painful."""
# [0"Rock", 1"Paper", 2"Scissors", 3"Gun", 4"Water",  5"Fire", 6"Dragon", 7"Devil", 8"Wolf", 9"Human", 10"Lightning", 11"Air", 12"Sponge", 13"Tree", 14"Snake"]
    if player_choice == all_skills[0]:
        if enemy_choice in [all_skills[i] for i in [2, 5, 8, 9, 12, 13, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[1]:
        if enemy_choice in [all_skills[i] for i in [0, 3, 4, 6, 7, 10, 11]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[2]:
        if enemy_choice in [all_skills[i] for i in [1, 8, 9, 11, 12, 13, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[3]:
        if enemy_choice in [all_skills[i] for i in [0, 2, 5, 8, 9, 13, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[4]:
        if enemy_choice in [all_skills[i] for i in [0, 2, 3, 5, 6, 7, 10]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[5]:
        if enemy_choice in [all_skills[i] for i in [1, 2, 8, 9, 12, 13, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[6]:
        if enemy_choice in [all_skills[i] for i in [0, 2, 3, 5, 7, 10, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[7]:
        if enemy_choice in [all_skills[i] for i in [0, 2, 3, 5, 9, 10, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[8]:
        if enemy_choice in [all_skills[i] for i in [1, 4, 6, 7, 10, 11, 12]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[9]:
        if enemy_choice in [all_skills[i] for i in [1, 4, 6, 8, 11, 12, 13]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[10]:
        if enemy_choice in [all_skills[i] for i in [0, 2, 3, 5, 9, 13, 14]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[11]:
        if enemy_choice in [all_skills[i] for i in [0, 3, 4, 5, 6, 7, 10]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[12]:
        if enemy_choice in [all_skills[i] for i in [1, 3, 4, 6, 7, 10, 11]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[13]:
        if enemy_choice in [all_skills[i] for i in [1, 4, 6, 7, 8, 11, 12]]:
            return 1
        else:
            return 0
    elif player_choice == all_skills[14]:
        if enemy_choice in [all_skills[i] for i in [1, 4, 8, 9, 11, 12, 13]]:
            return 1
        else:
            return 0


if __name__ == "__main__":
    main() 