import random
import os
import sys
from art import logo

# Define the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Initialize player and computer hands as empty lists
player = []
computer = []

# Function to draw a card from the deck
def card():
    return random.choice(cards)

# Function to add a card to a player's hand
def add_card(list):
    list.append(card())

# Function to calculate the score of a hand
def score(list):
    score = 0
    for i in list:
        score += i
    return score

# Function to clear player and computer hands
def clear_list():
    player.clear()
    computer.clear()

# Function to determine the winner and display the results
def winner(list1, list2):
    sum_list1 = score(list1)
    sum_list2 = score(list2)
    print(f"Your final hand: {player}, final score: {score(player)}")
    print(f"Computer's final hand: {computer}, final score: {score(computer)}")
    if sum_list1 > 21:
        print("You lose 😤")
    elif sum_list2 > 21:
        print("You win 😁")
    elif sum_list2 <= 17:
        add_card(computer)
        sum_list2 = score(list2)
        if sum_list1 > sum_list2:
            print("You win 😁")
        else:
            print("You lose 😤")
    elif sum_list1 > sum_list2:
        print("You win 😁")
    else:
        print("You lose 😤")

# Initialize the game loop
play = True

# Function to start a new game or exit
def still_playing():
    clear_list()
    ans = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if ans == "y":
        play = True
    else:
        play = False
        sys.exit()
    add_card(player)
    add_card(computer)
    os.system('clear')

# Main game loop
while play is True:
    still_playing()
    print(logo)
    add_card(player)
    add_card(computer)
    print(f"\tYour cards: {player}, current score is: {score(player)}")
    print(f"\tComputer's First choice is: {computer[0]}")
    ans = input("Type 'y' to get another card, type 'n' to pass: ")
    
    # Player's turn to draw cards
    while ans == "y":
        add_card(player)
        print(f"\tYour cards: {player}, current score is: {score(player)}")
        print(f"\tComputer's First choice is: {computer[0]}")
        
        # Check if the player's score exceeds 21
        if score(player) > 21:
            ans = "n"
        else:
            add_card(computer)
            ans = input("Type 'y' to get another card, type 'n' to pass: ")
    
    # Determine the winner
    winner(player, computer)
