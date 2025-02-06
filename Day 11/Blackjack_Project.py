import random
import time

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score based on the player's cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compares scores to determine the winner."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😉"
    elif user_score > 21:
        return "You went over. You lose 😢"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😍"
    else:
        return "You lose 💀"

def print_card(card):
    """Generates ASCII art for a card."""
    if card == 11:
        value = "A"
    else:
        value = str(card)

    return f"""
    .------.
    |{value}     |
    |      |
    |  ♠♣♦♥  |
    |      |
    |     {value}|
    `------`
    """

def display_hands(user_cards, computer_cards, hide_computer_card=True):
    """Displays the current hands of the user and computer in ASCII."""
    print("\n======================== BLACKJACK ========================")

    print("\nDealer's Hand:")
    if hide_computer_card:
        print(print_card(computer_cards[0]))  # Show only the first card
        print("Hidden Card: [ ? ]")
    else:
        for card in computer_cards:
            print(print_card(card))

    print("\nYour Hand:")
    for card in user_cards:
        print(print_card(card))

    print("==========================================================")

def play_game():
    """Main game logic for Blackjack."""
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        display_hands(user_cards, computer_cards, hide_computer_card=True)

        print(f"\nYour current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())  
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())  
        computer_score = calculate_score(computer_cards)

    display_hands(user_cards, computer_cards, hide_computer_card=False)

    print(f"\nYour final score: {user_score}")
    print(f"Dealer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 5)
    play_game()





