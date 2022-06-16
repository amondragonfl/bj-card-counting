import time
import random
import configparser


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
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_values = dict()
    card_values.update(dict.fromkeys(['2', '3', '4', '5', '6'], 1))
    card_values.update(dict.fromkeys(['7', '8', '9'], 0))
    card_values.update(dict.fromkeys(['10', 'A', 'K', 'Q', 'J'], -1))


if __name__ == '__main__':
    main()
