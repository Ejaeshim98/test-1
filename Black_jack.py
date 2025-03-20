#3/20/25
#Little Game of Blackjack
import random

def deal():
    #this returns a random card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal())
    computer_cards.append(deal())

def calculate_score(cards):
    #take list of cards and take score
    if sum(cards) == 21 and len(cards) == 1:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw \n"
    elif c_score == 0:
        return "You lose \n"
    elif u_score == 0:
        return "Win! Blackjack! \n"
    elif u_score > 21:
        return "Bust! You lose! \n"
    elif c_score >21:

        return "Opponent Bust! You win! \n"
    elif u_score > c_score:
        return "You win! \n"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your hand: {user_cards}, current score: {user_score}")
        print(f"Computer's hand: {computer_cards}, current score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: \n")
            if user_deal == "y":
                user_cards.append(deal())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score:{user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play? Type 'y' or 'n': "):
    #print("\n")
    play_game()