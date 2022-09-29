"""Rock Paper Scissors Grand Slam. Inspired by https://www.umop.com/rps15.htm but not as crazy as https://www.umop.com/rps101.htm ."""

import random

__author__: str = "730575704"

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


def  main() -> None:
    greet()
    global points
    story: str = "Start"
    if level > 0:
        story = "Continue"
    exit_message: str = "Return in defeat... (exit)"
    if level >= 3:
        exit_message = "Proclaim Victory! (exit)"
    print(f"Welcome {player} to RPS War\n1. {story} your legend \n2. Improve your strength \n3. {exit_message}")
    print(f"Fame: {fame}  Spirit: {points}")
    start: str = input("Enter 1, 2, or 3 to choose.")
    while start not in ["1","2","3"]:
        start = input("Please choose 1, 2, or 3.")
    if start == "1":
        level_select()
    if start == "2":
        spirit_spent:int = shop(points, fame)
        points -= spirit_spent
        main()
    if start == "3":
        if level < 3:
            print(f"While your journey ends in defeat, it is a tale for the ages. Fame: {fame}")
            quit()
        else:
            print(f"What a glorious journey! Your {fame} Fame resounds across the lands. You won with {points} remaining Spirit, and learned a total of {len(skillset_player) - 3} skills. We await your return warrior!")
            quit()


def greet() -> None:
    global player
    if player == "":
        print("In an age where conflict was common, before humans used guns and swords, the fist settled the fight. You are a champion of this era.")
        player = input("The Great ")
        print(f"Your people have been pushed back by the opposing tribe, and now you are the last line of defense against this mysterious invading tribe!!! Ready? {ROCK},{PAPER},{SCISSORS} !")


def shop(spirit, fame) -> int:
    global skillset_player
    global all_skills
    print(f"Welcome {player} to your tribe's Hall of Inheritance. Here, the statues of your ancestors will present skills based on your Fame. You can learn them by consuming Spirit.")
    print(f"{player}'s skills: {skillset_player}")
    skills_shop: list[str] = []
    for i in all_skills:
        skills_shop.append(i)
    for i in skillset_player:
        if i in skills_shop:
            skills_shop.remove(i)
    fame_start: int = 10
    spirit_start: int = 50
    j: int = 0  # To loop through skills and increase fame and spirit cost exponentially
    for i in skills_shop:
        fame_cost = cost(fame_start, j)
        spirit_cost = cost(spirit_start, j)
        if fame < fame_cost:
            print(f"{i} unlocked at {fame_cost} Fame")
        else:
            print(f"{i} costs {spirit_cost} Spirit")
        j += 1
    skills_shop.append("Leave")
    purchase_choice: str = input("Select a skill to buy or Leave: ")
    while purchase_choice not in skills_shop:
        purchase_choice = input("Choose a skill or Leave: ")
    if purchase_choice == "Leave":
        return 0
    else:
        k: int = 0
        while k < len(skills_shop):
            if skills_shop[k] == purchase_choice:
                unlock: bool = fame > cost(fame_start, k)
                afford: bool = spirit > cost(spirit_start, k)
                if not unlock:
                    print(f"You need {cost(fame_start, k) - fame} more Fame.")
                    return 0
                elif not afford:
                    print(f"You need {cost(spirit_start, k) - spirit} more Spirit.")
                    return 0
                else:
                    print(f"...You have learned {purchase_choice} for {cost(spirit_start, k)} Spirit.")
                    skillset_player.append(purchase_choice)
                    return cost(spirit_start, k)
            k += 1


def cost(start, time) -> int:
    """Calculates increases in shop requirements and rewards from battles"""
    return round(start * ((1 + 0.5) ** time))


def  level_select() -> None:
    levels_list: list[function] = [rules, level_one, level_two, level_three, level_four]
    levels_list_str: list[str] = ["0. Rules", "1. Northern Battlefield", "2. Endless Wilderness", "3. Frontline Commander", "4. Infinite Mode"]
    if level == 0:
        level_one()
    if level > 0:
        for i in levels_list_str[0:level + 2]:
            print(i)
        level_choice: int = int(input("Choose a level: "))  # Case for string
        levels_list[level_choice]()


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


def  level_one() -> None:
    """First level."""
    global level
    global points
    global fame
    print(f"Welcome to the Northern Battlefield {player}. The defense line has worn thin and you are here to push the enemy back. You quickly engage with the first enemy, the renowned warrior Dwayne the {ROCK} Johnson. Ready? {ROCK},{PAPER},{SCISSORS} !")
    for i in skillset_player:
        print(i)
    player_choice: str = input("Choose your skill: ")
    while player_choice not in skillset_player:
        player_choice = input("Choose a skill you know: ")
    while player_choice == all_skills[0]:
        player_choice = input("Its a tie, choose again: ")
    battle: int = skills(all_skills[0], player_choice)
    if battle == 1:
        print(f"You chose {player_choice} while Dwayne the {ROCK} Johnson chose {all_skills[0]}. Guess you can't choose {all_skills[0]} every time.")
        if level == 0:
            level += 1
        fame_gain: int = 10
        spirit_gain: int = 50
        print(f"{player}'s feat turns the tide of battle! You gain {fame_gain} Fame and {spirit_gain} Spirit! Spirit and Fame are gained through defeating strong enemies and can unlock new skills.")
        fame += fame_gain
        points += spirit_gain
        main()
    else:
        defeat: int = int(input(f"You chose {player_choice} while Dwayne the {ROCK} Johnson chose {all_skills[0]}. 1. Fight again or 2. retreat?"))
        while defeat not in [1,2]:
            defeat = int(input("Choose to 1. Fight or 2. Retreat"))
        if defeat == 1:
            level_one()
        else:
            main()


def minion(skills_list: list[int], fame_gain: int, spirit_gain: int) -> int:
    """Battle against cannon fodder to fill levels. Takes arguments of enemy skills and rewards, does random battle, adds rewards and returns 1 for win and 0 for loss."""
    global points
    global fame
    for i in skillset_player:
        print(i)
    enemy_choice: str = random.choice([all_skills[i] for i in skills_list])
    player_choice: str = input("Choose your skill: ")
    while player_choice not in skillset_player:
        player_choice = input("Choose a skill you know: ")
    tie: bool = False
    if player_choice == enemy_choice:
        tie = True
    while tie:
        enemy_choice = random.choice([all_skills[i] for i in skills_list])
        player_choice = input("Its a tie, choose again: ")
        if player_choice != enemy_choice:
            tie = False
    battle: int = skills(enemy_choice, player_choice)
    if battle == 1:
        print(f"The enemy chose {enemy_choice}. {player_choice} beats {enemy_choice}.")
        print(f"You gain {fame_gain} Fame and {spirit_gain} Spirit!")
        points += spirit_gain
        fame += fame_gain
        return 1
    else:
        print(f"You chose {player_choice} while the enemy chose {enemy_choice}, you lost.")
        return 0


def level_two() -> None:
    global level
    global points
    global fame
    print(f"After breaching the battlefront you make your way through the endless wilderness, letting the name \"{player}\" strike fear into your enemies. In response, an ambush is planned with the enemies strongest nature warriors!")
    print(f"Surrounded by 5 opponents there is only one way to settle this! Best out of 5! Ready? {ROCK},{PAPER},{SCISSORS} !")
    player_score: int = 0
    enemy_score: int = 0
    fame_gain: int = fame
    total_fame_gain: int = 0
    spirit_gain: int = points
    total_spirit_gain: int = 0
    while player_score < 3 and enemy_score < 3:
        battle: int = minion(nature_skills, fame_gain, spirit_gain)
        if battle == 1:
            player_score += 1
            total_fame_gain += fame_gain
            total_spirit_gain += spirit_gain
            fame_gain = cost(fame_gain, player_score)
            spirit_gain = cost(spirit_gain, player_score)
        else:
            enemy_score += 1
    win_message: str = f"Best out of 5 always guaranteed victory! The name {player} gained {total_fame_gain} Fame across the land. You gained {total_spirit_gain} Spirit. Now take the battle to the enemy camp!"
    lose_message: str = "You are overwhelmed with their skills and are defeated!"
    best_out_of_x(1, level_two, 3, player_score, enemy_score, total_fame_gain, total_spirit_gain, lose_message, win_message)


def level_three() -> None:
    """Third Level of the game."""
    global level
    global points
    global fame
    print("After a harrowing journey you have reached the commander base at the frontline. ")
    print("You have intel that the commander can read your mind! How will you make it past this battle?")
    print("Hint: ... will be able to predict the use of 5 skills leading to a guaranteed loss. Try to choose one of the other 10 for a chance!")
    fame_gain: int = fame
    total_fame_gain: int = 0
    spirit_gain: int = points
    total_spirit_gain: int = 0
    player_score: int = 0
    enemy_score: int = 0
    while player_score < 5 and enemy_score < 5:
        enemy_prediction: list[str] = random.sample(all_skills, 5)
        for i in skillset_player:
          print(i)
        player_choice: str = input("Think about what skill you will use: ")
        if player_choice in enemy_prediction:
            print("Your mind was read! You lose this round.")
            enemy_score += 1
        else:
            print("It was not predicted! You have a chance, now play your move.")
            battle: int = minion(range(0, 15, 1), fame_gain, spirit_gain)
            if battle == 1:
                player_score += 1
                total_fame_gain += fame_gain
                total_spirit_gain += spirit_gain
                fame_gain = cost(fame_gain, player_score)
                spirit_gain = cost(spirit_gain, player_score)
            else:
                enemy_score += 1
    win_message: str = ""
    lose_message: str = ""
    best_out_of_x(2, level_three, 5, player_score, enemy_score, total_fame_gain, total_spirit_gain, lose_message, win_message)


def level_four() -> None:
    """Infinite mode for player to have fun after game is beaten."""


def best_out_of_x(level_add: int, level_func, win_cond: int, player_score: int, enemy_score: int, total_fame_gain: int, total_spirit_gain: int, lose_message: str, win_message: str) -> int:
    global level
    if player_score == win_cond:
        print(win_message)
        if level == level_add:
            level += 1
        main()
    if enemy_score == win_cond:
        print(lose_message)
        defeat: str = input(f"1. Fight again or 2. retreat?")
        while defeat not in ["1","2"]:
            defeat = input("Choose to 1. Fight or 2. Retreat")
        if defeat == "1":
            level_func()
        else:
            main()


def skills(enemy_choice: str, player_choice: str) -> int:
# Every single win condition. Don't ask. It was painful.
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