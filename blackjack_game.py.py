import os
import random
import time

logo = """
 .------.            .------.

 |2_  _ |            |A_  _ |
 | ( \/ )|           | ( \/ )|
 |  \  / |           |  \  / |
 |   \/ 2|           |   \/ A|
 `------'            `------'
"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_results(player_score, com_score):
    conditions = {
        "draw": "it's a draw!\n",
        "player_win": "congratulations you win (: \n",
        "com_win": "the computer wins! ): \n",
        "player_blackjack": "you win with blackjack!\n",
        "com_blackjack": "the computer wins with blackjack!\n",
        "player_over21": "you went over 21! \n",
        "com_over21": "computer went over 21!\n",
    }
    
    if player_score == 0:
        return conditions["player_blackjack"]
    elif com_score == 0:
        return conditions["com_blackjack"]
    elif player_score > 21:
        return conditions["player_over21"]
    elif com_score > 21:
        return conditions["com_over21"]
    elif player_score > com_score:
        return conditions["player_win"]
    elif player_score == com_score:
        return conditions["draw"]
    else:
        return conditions["com_win"]

def game21():
    menu_choice = input("choose a game to start...\n\n1-froggy\n2-twenty one\n3-snake\n\nYour choice: ")
    
    if menu_choice == "twenty one" or menu_choice == "2":
        time.sleep(2)
        clear_screen()
        print(logo)
        time.sleep(2)
        
        player_cards = [draw_card() for _ in range(2)]
        com_cards = [draw_card() for _ in range(2)]
        game_continue = True
        
        while game_continue:
            player_score = calculate_score(player_cards)
            com_score = calculate_score(com_cards)
            time.sleep(2)
            print(f"\n\nyour cards are {player_cards}, and your score {player_score}")
            time.sleep(1)
            print(f"computer first's card is {com_cards[0]}")
            
            if player_score == 0 or com_score == 0 or player_score > 21 or com_score > 21:
                game_continue = False
            else:
                draw_player_another_card = input("do you want another card (y/n): ").lower()
                if draw_player_another_card == "y":
                    player_cards.append(draw_card())
                else:
                    game_continue = False
                    
        player_score = calculate_score(player_cards)
        
        if player_score <= 21 and player_score != 0:
            while com_score != 0 and com_score < 17:
                com_cards.append(draw_card())
                com_score = calculate_score(com_cards)
                
        print(f"your final hand: {player_cards} with score {player_score}")
        print(f"and computer's final hand: {com_cards} with score {com_score}")
        print(compare_results(player_score, com_score))
        time.sleep(2)

game21()
