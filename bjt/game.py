import time
import random
import configparser
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_card(rank: str, suit: str) -> None:
    print('┌─────────┐')
    print(f'│{rank}        │') if rank != "10" else print(f'│{rank}       │')
    print('│         │')
    print('│         │')
    print(f'│    {suit}    │')
    print('│         │')
    print('│         │')
    print(f'│        {rank}│') if rank != "10" else print(f'│       {rank}│')
    print('└─────────┘')


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ["♠", "♥", "♦", "♣"]

    card_values = dict()
    card_values.update(dict.fromkeys(['2', '3', '4', '5', '6'], 1))
    card_values.update(dict.fromkeys(['7', '8', '9'], 0))
    card_values.update(dict.fromkeys(['10', 'A', 'K', 'Q', 'J'], -1))

    count = 0
    card = None

    for i in range(int(config["game"]["card_amount"])):
        old = card
        card = random.choice(card_ranks)
        while card == old:
            card = random.choice(card_ranks)
        count += card_values[card]
        display_card(card, random.choice(card_suits))
        time.sleep(int(config["game"]["seconds_between_cards"]))
        clear_terminal()

    while True:
        try:
            guess = int(input("Enter count: "))
            break
        except ValueError:
            print("Please enter a valid value!")

    if guess == count:
        print("That is correct!!!")
    else:
        print(f"Wrong answer, actual count was {count}")


if __name__ == '__main__':
    main()
