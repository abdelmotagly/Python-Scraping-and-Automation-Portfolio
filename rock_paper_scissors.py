import random

# الرسوم النصية للعبة
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art_array = {
    "Rock": rock,
    "Paper": paper,
    "Scissors": scissors,
}

choses = ["Rock", "Paper", "Scissors"]

print("welcome to the rock, paper, scissors game: ")
rules_or_start = input("press enter to continue or type(help) for the rules: ").lower()

if rules_or_start == "help":
    print("\t**********rules**********\t\t")
    print("\t1-you choose and the computer chooses.")
    print("\t2-rock smashes scissors -> rock wins.")
    print("\t3-scissors cut paper -> scissors win.")
    print("\t4-paper covers rock -> paper wins.\n")

if rules_or_start == "" or rules_or_start == "help":
    player_choice = input("enter your choice (rock, paper, scissors): ").capitalize()
    
    if player_choice not in choses:
        print("invalid choice! please run the program again and choose rock, paper, or scissors")
    else:
        print(f"you choose:\n{art_array[player_choice]}")
        
        com_choice = random.choice(choses)
        print(f"and the computer chooses:\n{art_array[com_choice]}")
        
        if (player_choice == "Rock" and com_choice == "Scissors") or \
           (player_choice == "Paper" and com_choice == "Rock") or \
           (player_choice == "Scissors" and com_choice == "Paper"):
            result = "player wins"
        elif player_choice == com_choice:
            result = "it's draw"
        else:
            result = "computer wins"
            
        if result == "player wins":
            print(f"you win! {player_choice} beats {com_choice}")
        elif result == "it's draw":
            print(f"it's draw! you choose {player_choice} and the computer {com_choice}")
        else:
            print(f"the computer wins! {com_choice} beats {player_choice}")
else:
    print("invalid input!")
