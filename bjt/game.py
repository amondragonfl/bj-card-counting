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
    clear_terminal()
    config = configparser.ConfigParser()
    config.read("config.ini")

    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ["♠", "♥", "♦", "♣"]

    card_values = dict()
    card_values.update(dict.fromkeys(['2', '3', '4', '5', '6'], 1))
    card_values.update(dict.fromkeys(['7', '8', '9'], 0))
    card_values.update(dict.fromkeys(['10', 'A', 'K', 'Q', 'J'], -1))

    count = 0
    card_rank = None
    log = []

    for i in range(int(config["game"]["card_amount"])):
        old = card_rank
        card_rank = random.choice(card_ranks)
        while card_rank == old:
            card_rank = random.choice(card_ranks)
        card_suit = random.choice(card_suits)
        card_value = card_values[card_rank]

        log.append((card_rank, card_suit, card_value))
        count += card_value
        display_card(card_rank, card_suit)
        time.sleep(float(config["game"]["seconds_between_cards"]))
        clear_terminal()

    while True:
        try:
            guess = float(input("Enter count: "))
            break
        except ValueError:
            print("Please enter a valid value!")

    if guess == count:
        print("That is correct!!!")
    else:
        print(f"Wrong answer, actual count was {count}")

    show_log = input("Do you wish to analyze the log (y/n): ").lower()
    if show_log == "y":
        log_count = 0
        for card in log:
            display_card(card[0], card[1])
            print(f"Card value: {card[2]}")
            log_count += card[2]
            print(f"Current count: {log_count}")
        print(f"Final count {log_count}")


if __name__ == '__main__':
    main()
