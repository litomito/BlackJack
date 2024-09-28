# Importing necessary modules
import random
import time
from ind_uppgift.player import Players
from typing import Union


# Create two players with class attributes from classes.py
player: Players = Players("Player", [])
computer: Players = Players("Computer", [])

# Variables to store the total sum of the player and computer's hand
player_score: int = 0
computer_score: int = 0

# Function to calculate the score of players hand
def calculate_score(hand: list) -> int:
    score: int = 0
    for card in hand:
        score += card
    return score

# List of cards in a deck A = 14 or 1, J = 11, Q = 12, K = 13
cards: list[Union[int, str]] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "A"]

# Start the game if the user wants to play 
def start_game() -> None:
    # The question to ask the user if they want to play a game
    question: str = input("Do you want to play a game of swedish blackjack? (y/n): ")
    if question.lower() == "y":
        print("Game started!")
        player.add_card(draw_card(True))
        computer.add_card(draw_card(False))
        update_score()
        print(f"Computer hand: {computer.hand}")
        print(f"Your hand: {player.hand}")
        player_turn()
        computer_turn()
        check_game_status()

# Draw a card for the player or computer and return the card value
def draw_card(is_player: bool) -> int:
    # Randomly choose a card from the list of cards
    card: Union[int, str] = random.choice(cards)

    # If the card is an A, ask the player or computer to choose between 1 or 14, and return the chosen value as an integer
    if card == "A":
        # If the player is the one drawing the card, ask the player to choose between 1 or 14
        if is_player:
            while True:
                try:
                    random_option: int = int(input("Woow an A!!\nDo you want the A card to be 1 or 14? (1/14): "))
                    if random_option == 1:
                        return 1
                    elif random_option == 14:
                        return 14
                    else:
                        print("Please choose 1 or 14")
                except ValueError:
                    print("Please choose 1 or 14")
        else:
            return random.choice([1, 14])
    return card

# Function to check game status and print the winner of the game
def check_game_status() -> None:
    global player_score, computer_score
    if player_score <= 21 and computer_score <= 21:
        if player_score > computer_score:
            print(f"You won!\nYour hand: {player.hand} = {player_score}")
        elif player_score < computer_score:
            print(f"Computer won!\nComputer hand: {computer.hand} = {computer_score}")
        else:
            print(f"{computer.label} won!\nComputer hand: {computer.hand} = {computer_score} VS Your hand: {player.hand} = {player_score}")

# Players turn to draw or stop drawing cards
def player_turn() -> None:
    global player_score
    while True:
        draw: str = input("Do you want to draw a card? (y/n): ")
        if draw.lower() == "y":
            player.add_card(draw_card(True))
            update_score()
            print(f"Your hand: {player.hand} = {player_score}")
            if player_score > 21:
                break
        else:
            break

# Computer turn to draw or stop drawing cards based on the player's score and the computer score
def computer_turn() -> None:
    global computer_score, player_score
    if player_score > 21:
        return
    while True:
        time.sleep(1)
        if (computer_score < 17 and computer_score < player_score):
            computer.add_card(draw_card(False))
            update_score()
            print(f"{computer.label} hand: {computer.hand} = {computer_score}")
            if computer_score > 21:
                print(f"{computer.label} lost!\n{computer.label} hand: {computer.hand} = {computer_score}\nYou Won!\nYour hand: {player.hand} = {player_score}")
                break
        else:
            break

# Update the score of the player and computer after each draw of a card
def update_score() -> None:
    global player_score, computer_score
    player_score = calculate_score(player.hand)
    computer_score = calculate_score(computer.hand)

# Start the game if the file is run as a script
if __name__ == "__main__":
    start_game()
    print("Game ended!")